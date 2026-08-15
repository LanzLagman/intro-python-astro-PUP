"""
Refresh the offline cache with REAL archive data.

Run this ONCE from the repository root on a machine with a working internet
connection, ideally the day before the workshop:

    python scripts/cache_data.py

It overwrites:
    data/gaia_pleiades.csv                (Gaia DR3 cone search on M45)
    data/pleiades_members_published.csv   (published membership list, VizieR)

Until you run it, those files hold a physically realistic SIMULATION produced by
scripts/make_synthetic_fallback.py, so the notebooks work offline but the numbers
are not real measurements.
"""

import os
import sys

import pandas as pd

# Pleiades (M45), matching the SkyCoord built in Notebook 01
RA, DEC = 56.75, 24.116667
RADIUS = 1.0          # degrees
MAG_LIMIT = 18.0
ROW_LIMIT = 8000

ADQL = f"""
SELECT TOP {ROW_LIMIT}
    source_id, ra, dec,
    parallax, parallax_error, parallax_over_error,
    pmra, pmdec, pmra_error, pmdec_error,
    phot_g_mean_mag, phot_bp_mean_mag, phot_rp_mean_mag, bp_rp,
    ruwe
FROM gaiadr3.gaia_source
WHERE 1 = CONTAINS(
        POINT('ICRS', ra, dec),
        CIRCLE('ICRS', {RA}, {DEC}, {RADIUS}))
    AND parallax IS NOT NULL
    AND phot_g_mean_mag < {MAG_LIMIT}
"""


def cache_gaia(outdir):
    from astroquery.gaia import Gaia

    print("querying gaiadr3.gaia_source ... (this can take 30-90 seconds)")
    job = Gaia.launch_job_async(ADQL)
    df = job.get_results().to_pandas()

    if "parallax_over_error" not in df.columns:
        df["parallax_over_error"] = df["parallax"] / df["parallax_error"]

    path = os.path.join(outdir, "gaia_pleiades.csv")
    df.to_csv(path, index=False)
    print(f"  wrote {len(df):5d} rows -> {path}")

    near = df[(df["parallax"] > 6) & (df["parallax"] < 9)]
    print(f"  sanity: {len(near)} stars between 6 and 9 mas "
          f"(the cluster sits near 7.4 mas)")
    return df


def cache_members(outdir):
    from astroquery.vizier import Vizier

    print("\nquerying VizieR for a published membership list ...")
    v = Vizier(columns=["Source"], row_limit=-1)

    # Cantat-Gaudin & Anders (2020), Gaia DR2 open cluster members.
    # Melotte 22 is the Pleiades.
    for catalog, cluster in [("J/A+A/633/A99", "Melotte_22"),
                             ("J/A+A/628/A66", "Melotte_22")]:
        try:
            res = v.query_constraints(catalog=catalog, Cluster=cluster)
            if len(res) == 0:
                continue
            df = res[0].to_pandas()
            col = "Source" if "Source" in df.columns else df.columns[0]
            out = pd.DataFrame({"source_id": df[col].astype("int64")})
            path = os.path.join(outdir, "pleiades_members_published.csv")
            out.to_csv(path, index=False)
            print(f"  wrote {len(out):5d} members from {catalog} -> {path}")
            return out
        except Exception as err:
            print(f"  {catalog} failed: {type(err).__name__}: {err}")

    print("  WARNING: no membership catalogue retrieved; existing file kept.")
    return None


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    outdir = os.path.join(root, "data")
    os.makedirs(outdir, exist_ok=True)

    print(f"caching into {outdir}\n")
    try:
        gaia = cache_gaia(outdir)
    except Exception as err:
        print(f"\nGaia query FAILED: {type(err).__name__}: {err}")
        print("The existing cache was left untouched. Check your connection "
              "and try again.")
        sys.exit(1)

    members = cache_members(outdir)

    print("\n" + "=" * 62)
    print("Cache refreshed with REAL archive data.")
    print(f"  Gaia rows       : {len(gaia)}")
    print(f"  published members: {len(members) if members is not None else 'unchanged'}")
    print("\nNow open notebooks/02 and re-run it end to end to confirm.")
    print("=" * 62)


if __name__ == "__main__":
    main()
