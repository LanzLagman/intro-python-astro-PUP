"""
Generate a PHYSICALLY REALISTIC SIMULATED Pleiades field, used only as an
emergency fallback when the live Gaia query is unavailable.

This is NOT real Gaia data. Run scripts/cache_data.py on a machine with
internet access to overwrite data/gaia_pleiades.csv with the real thing.

The simulation is tuned so that every teaching beat in the workshop still
works: a clean main sequence in the CMD, a tight proper-motion clump, a
parallax overdensity at ~7.4 mas, and a realistic field-star background.
"""

import numpy as np
import pandas as pd

RNG = np.random.default_rng(45)  # M45

# --- Pleiades (M45) literature values -------------------------------------
RA0, DEC0 = 56.75, 24.1167      # deg
PLX0 = 7.36                      # mas  -> d ~ 136 pc
PMRA0, PMDEC0 = 19.9, -45.5      # mas/yr
DM = 5 * np.log10(1000.0 / PLX0 / 10.0)   # distance modulus
RADIUS = 1.0                     # deg cone

N_MEM = 620
N_FIELD = 7600

# --- Empirical Pleiades main sequence: BP-RP -> absolute G ----------------
_BPRP = np.array([-0.20, 0.00, 0.20, 0.40, 0.60, 0.80, 1.00, 1.20, 1.40,
                  1.60, 1.80, 2.00, 2.40, 2.80, 3.20, 3.60, 4.00])
_MG = np.array([-0.90, 0.75, 1.60, 2.35, 3.15, 4.05, 5.05, 5.90, 6.60,
                7.35, 8.10, 8.90, 10.30, 11.55, 12.60, 13.50, 14.30])


def main_sequence(bp_rp):
    return np.interp(bp_rp, _BPRP, _MG)


def sample_in_cone(n, radius_deg):
    """Uniform on a spherical cap around (RA0, DEC0)."""
    theta = radius_deg * np.sqrt(RNG.random(n))       # deg from centre
    phi = RNG.uniform(0, 2 * np.pi, n)
    ddec = theta * np.cos(phi)
    dra = theta * np.sin(phi) / np.cos(np.radians(DEC0))
    return RA0 + dra, DEC0 + ddec


def make_members(n):
    # Colour distribution: mass function makes faint red stars dominate.
    bp_rp = np.clip(RNG.gamma(2.2, 0.55, n) - 0.15, -0.15, 4.0)
    mg = main_sequence(bp_rp)

    # ~22% unresolved binaries sit up to 0.75 mag above the single-star track
    is_bin = RNG.random(n) < 0.22
    mg = mg - is_bin * RNG.uniform(0.15, 0.75, n)
    mg += RNG.normal(0, 0.06, n)            # photometric + depth scatter

    # Cluster has real line-of-sight depth (~4 pc half-width)
    d_pc = 1000.0 / PLX0 + RNG.normal(0, 4.0, n)
    plx_true = 1000.0 / d_pc
    g = mg + 5 * np.log10(d_pc / 10.0)

    # Astrometric errors grow steeply with magnitude (Gaia-like)
    plx_err = 0.017 * 10 ** (0.20 * np.clip(g - 15.0, -4, 5))
    plx_err = np.clip(plx_err, 0.012, 0.9)
    pm_err = plx_err * 1.25

    ra, dec = sample_in_cone(n, 0.85 * RADIUS)   # members centrally concentrated
    # pull members toward the centre
    ra = RA0 + (ra - RA0) * RNG.beta(1.6, 2.0, n) * 1.9
    dec = DEC0 + (dec - DEC0) * RNG.beta(1.6, 2.0, n) * 1.9

    return pd.DataFrame({
        "ra": ra,
        "dec": dec,
        "parallax": plx_true + RNG.normal(0, 1, n) * plx_err,
        "parallax_error": plx_err,
        # internal velocity dispersion ~0.5 mas/yr, plus measurement error
        "pmra": PMRA0 + RNG.normal(0, 0.55, n) + RNG.normal(0, 1, n) * pm_err,
        "pmdec": PMDEC0 + RNG.normal(0, 0.55, n) + RNG.normal(0, 1, n) * pm_err,
        "pmra_error": pm_err,
        "pmdec_error": pm_err,
        "phot_g_mean_mag": g,
        "bp_rp": bp_rp,
        "ruwe": RNG.normal(1.02, 0.10, n).clip(0.75, 2.6),
        "_truth": 1,
    })


def make_field(n):
    # Field stars: magnitude-limited sample, mostly faint and distant
    g = np.clip(RNG.normal(17.2, 1.7, n), 9.0, 20.0)
    bp_rp = np.clip(RNG.normal(1.15, 0.62, n), -0.1, 4.2)

    # Distances: broad, peaking well beyond the cluster
    d_pc = np.clip(RNG.lognormal(np.log(950), 0.85, n), 25, 12000)
    plx_true = 1000.0 / d_pc

    plx_err = 0.017 * 10 ** (0.20 * np.clip(g - 15.0, -4, 5))
    plx_err = np.clip(plx_err, 0.012, 1.1)
    pm_err = plx_err * 1.25

    ra, dec = sample_in_cone(n, RADIUS)

    return pd.DataFrame({
        "ra": ra,
        "dec": dec,
        "parallax": plx_true + RNG.normal(0, 1, n) * plx_err,
        "parallax_error": plx_err,
        "pmra": RNG.normal(1.5, 7.5, n) + RNG.normal(0, 1, n) * pm_err,
        "pmdec": RNG.normal(-4.0, 7.5, n) + RNG.normal(0, 1, n) * pm_err,
        "pmra_error": pm_err,
        "pmdec_error": pm_err,
        "phot_g_mean_mag": g,
        "bp_rp": bp_rp,
        "ruwe": RNG.normal(1.10, 0.22, n).clip(0.75, 3.5),
        "_truth": 0,
    })


def main():
    df = pd.concat([make_members(N_MEM), make_field(N_FIELD)], ignore_index=True)
    df = df.sample(frac=1.0, random_state=45).reset_index(drop=True)

    df.insert(0, "source_id", 66000000000000000 + np.arange(len(df)) * 977)
    df["parallax_over_error"] = df["parallax"] / df["parallax_error"]
    df["phot_bp_mean_mag"] = df["phot_g_mean_mag"] + 0.55 * df["bp_rp"]
    df["phot_rp_mean_mag"] = df["phot_bp_mean_mag"] - df["bp_rp"]

    cols = ["source_id", "ra", "dec", "parallax", "parallax_error",
            "parallax_over_error", "pmra", "pmdec", "pmra_error", "pmdec_error",
            "phot_g_mean_mag", "phot_bp_mean_mag", "phot_rp_mean_mag",
            "bp_rp", "ruwe"]

    truth = df["_truth"].to_numpy()
    out = df[cols].round(6)
    out.to_csv("data/gaia_pleiades.csv", index=False)

    # "Published" member list: incomplete on purpose (85% recovery), plus a
    # small number of spurious entries. Students score against this in NB05.
    mem_ids = df.loc[truth == 1, "source_id"].to_numpy()
    keep = RNG.random(len(mem_ids)) < 0.85
    published = list(mem_ids[keep])
    fld_ids = df.loc[truth == 0, "source_id"].to_numpy()
    published += list(RNG.choice(fld_ids, 12, replace=False))

    pd.DataFrame({"source_id": sorted(published)}).to_csv(
        "data/pleiades_members_published.csv", index=False)

    print(f"data/gaia_pleiades.csv              {len(out):6d} rows")
    print(f"data/pleiades_members_published.csv {len(published):6d} rows")
    print(f"true members in field: {truth.sum()}   distance modulus: {DM:.2f}")


if __name__ == "__main__":
    main()
