# Computational and Data-driven Astrophysics: A Practical Python Workshop

**PUP Physics Society Programming Seminar / Workshop**
15 August 2026 · Online

**Speaker:** Lanz Anthonee Avila Lagman, MSc
PhD Data Science, University of the Philippines Diliman

**Slide guide:** `workshop_overview.pdf`: the deck that ran alongside the session. It maps
the physics to the notebooks and is released separately.

---

## About this repository

The live session ran last Saturday: a 12-15 minute overview per notebook, showing what
Python can do and the shape of the research problems data-driven and computational
astrophysics work on.

The notebooks have since been revised into **standalone coding templates and reference
helpers**: self-contained patterns (archive queries, ODE integration, a clustering
pipeline, a publication-ready figure) you can lift into your own project once you already
know Python fundamentals.

Still learning Python itself? Start with `notebooks/additional_readings.md` first, then
come back here; these work far better as templates than as a first introduction.

---

## Part 1: Live workshop notebooks

Worked through together during the session. Roughly 12–15 minutes each.

| # | Notebook | What you can do afterwards | Colab |
|---|---|---|---|
| 01 | **Basic Setup and Astropy Fundamentals** | Compute real stellar properties with units that catch your mistakes | [![Open](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lanzlagman/intro-python-astro-PUP/blob/main/notebooks/01_setup_and_astropy_fundamentals.ipynb) |
| 02 | **Downloading Datasets with astroquery** | Pull data from any astronomical archive | [![Open](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lanzlagman/intro-python-astro-PUP/blob/main/notebooks/02_downloading_datasets_astroquery.ipynb) |
| 03 | **Solving ODEs with NumPy and SciPy** | Integrate any dynamical system, and know when not to trust it | [![Open](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lanzlagman/intro-python-astro-PUP/blob/main/notebooks/03_solving_odes_numpy_scipy.ipynb) |
| 04 | **Data Visualization in Astronomy** | Build a figure that makes an argument, not just a plot | [![Open](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lanzlagman/intro-python-astro-PUP/blob/main/notebooks/04_data_visualization_astronomy.ipynb) |
| 05 | **Traditional ML in Astrophysics** | Find structure nobody labelled, and score it honestly | [![Open](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lanzlagman/intro-python-astro-PUP/blob/main/notebooks/05_traditional_ml_astrophysics.ipynb) |
| 06 | **Responsible Use of AI in Astrophysics** | Closing reminders. Feel free to improve further. | [![Open](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lanzlagman/intro-python-astro-PUP/blob/main/notebooks/06_responsible_ai_astrophysics.ipynb) |

### The narrative

Astrophysics has two sources of data: you **download** it (NB02) or you **generate it from
the physics** (NB03). NB04 looks at both. NB05 learns from both. NB01 gives you the
vocabulary and NB06 is about not lying with any of it.

The whole of Part 1 works one dataset: a Gaia cone search on the **Pleiades (M45)**,
Carroll & Ostlie's own worked example of an open cluster. Notebook 02
downloads it, Notebook 04 plots it, Notebook 05 clusters it.

---

## Part 2: The strategizing session

There are no notebooks for Part 2, and that is the point. Notebooks 01–06 walked through a
sequence somebody else had already decided. Part 2 is the opposite exercise: take a published
paper (or your own research idea) and write, by hand, the coding plan you would need before
writing any code: a six-section markdown template covering the claim, the data, the steps,
the paper's unstated assumptions, what you expect to break, and how you would know if you were
wrong.

It ran as an open forum around three papers on open clusters, exoplanets and gravitational
waves. Full details, the plan template, and the three paper picks are in
[`notebooks/strategizing_session.md`](notebooks/strategizing_session.md).

### `demo-workshop/`: the code-along output from that session

`demo-workshop/init_plan.md` is the plan the speaker wrote live during Part 2, targeting a
Gaia DR3 open-cluster detection and characterization project
([Liu et al. 2025](https://arxiv.org/pdf/2504.08179)). It is a worked example of the template
above, not a polished notebook. It is deliberately left as a planning artifact.

Read the outline structurally, not as a table of contents: each **Roman-numeral heading**
(I, II, III…) marks a notebook that would eventually get built, and the lettered/numbered
**subsections underneath it** are the sections that notebook would contain. So "I. Download
Gaia DR3 Dataset Sample" is notebook-to-be-written #1, and "A. Prepare ADQL Query" /
"B. Run ADQL Query" / "C. Save Query Results" are its planned sections, the same
decompose-before-you-code habit Notebooks 01–06 tried to build, applied to a real research
problem rather than a teaching example.

`demo-workshop/Data/` holds the `Input/` and `Output/` scratch folders used while working
through that plan.

---

## Running locally instead of Colab

```bash
git clone https://github.com/lanzlagman/intro-python-astro-PUP.git
cd intro-python-astro-PUP
python -m venv .venv && source .venv/bin/activate    # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter lab
```

Run notebooks from the repository root, or from `notebooks/`, so the relative data paths
resolve; if no local copy is found they are fetched from GitHub automatically.

---

## Offline / bad-Wi-Fi mode

Every network call in this repository is wrapped in `try / except`. If the live Gaia query
fails, or forty people query ESA simultaneously and get throttled, the notebooks fall back to
a cached copy and **everything still runs**.

To force offline mode, set this near the top of Notebook 02:

```python
TRY_LIVE_QUERY = False
```

### Where the cached data comes from

The `load_workshop_data()` helper in Notebooks 02, 04 and 05 looks for `data/<file>` and then
`../data/<file>` on disk, and if neither exists it downloads from this repository's `data/`
directory on GitHub. That makes Colab and local runs behave identically without shipping the
CSVs in the clone.

To build a local cache yourself, run either script once from the repository root:

```bash
python scripts/cache_data.py               # real Gaia DR3 + published member list
python scripts/make_synthetic_fallback.py  # physically realistic simulation, no network needed
```

`cache_data.py` needs internet and writes genuine archive results. `make_synthetic_fallback.py`
writes a simulation, not real Gaia rows: it reproduces the cluster's parallax (~7.4 mas),
proper motion (~+19.9, −45.5 mas/yr), main sequence and field contamination, so every teaching
beat behaves correctly. Use the real data for anything beyond teaching.

---

## Repository layout

```
intro-python-astro-PUP/
├── README.md
├── workshop_overview.pdf       # slide guide for the live session
├── requirements.txt            # loose floors, safe on Colab
├── requirements-frozen.txt     # exact versions, for reproducing results
├── LICENSE
├── notebooks/                       # Part 1, outputs cleared - run these
│   ├── 01-06 ...ipynb
│   ├── strategizing_session.md      # Part 2: the plan template and paper picks
│   ├── additional_readings.md       # further reading, indexed per notebook
│   └── data/                        # written at runtime by NB02 (not tracked)
├── solutions/                  # Part 1, Notebooks 01-05 with exercises filled in and executed
│                                #   (NB06 has no exercises, so no solutions copy exists for it)
├── demo-workshop/              # speaker's own Part 2 code-along output
│   ├── init_plan.md            # the coding plan written live during the session
│   └── Data/                   # Input/ and Output/ scratch data for that plan
└── scripts/
    ├── cache_data.py                     # build the cache from the real archives
    └── make_synthetic_fallback.py        # generate the simulated fallback
```

Look at `solutions/` **after** you have tried the exercises, not before.

---

## Carroll & Ostlie cross-reference

Every demo problem in Part 1 comes from **Carroll, B. W. & Ostlie, D. A., *An Introduction to
Modern Astrophysics*, 2nd ed. (Pearson Addison-Wesley, 2007)**, and each notebook states its
sections in a markdown cell before the code.

**Notebook 01** draws on §1.3 *Positions on the Celestial Sphere*, §3.1 *Stellar Parallax*,
§3.2 *The Magnitude Scale*, §3.4 *Blackbody Radiation* and §3.6 *The Color Index*. Its worked
exercise is **Problem 9** of the Chapter 3 problem set, modelling Dschubba (δ Sco) as a
spherical blackbody. **Notebook 02** revisits §1.3 and §3.6 alongside §8.2 *The
Hertzsprung–Russell Diagram* and §13.3 *Stellar Clusters*. **Notebook 03** works from §2.1
*Elliptical Orbits* and §2.3 *Kepler's Laws Derived*; its Parts 4 and 6 are adapted from that
chapter's problem set rather than reproducing a numbered problem. **Notebook 04** uses §3.2,
§3.6, §8.2 and §13.3, and **Notebook 05** uses §8.1 *The Formation of Spectral Lines*, §8.2,
§13.3 and §25.1 *The Hubble Sequence*. Notebook 06 cites no textbook sections.

| Section | Page |
|---|---|
| §1.3 Positions on the Celestial Sphere | 14 |
| §2.1 Elliptical Orbits | 31 |
| §2.3 Kepler's Laws Derived | 47 |
| §3.1 Stellar Parallax | 69 |
| §3.2 The Magnitude Scale | 72 |
| §3.4 Blackbody Radiation | 80 |
| §3.6 The Color Index | 87 |
| Problem 9 (Dschubba, δ Sco) | 94 |
| §8.1 The Formation of Spectral Lines | 230 |
| §8.2 The Hertzsprung–Russell Diagram | 247 |
| §13.3 Stellar Clusters | 520 |
| §25.1 The Hubble Sequence | 956 |

> **Note on numbering.** Some print runs are Pearson reprints that assemble the book chapter
> by chapter and print chapters without their numbers, so §3.1 appears as plain "1", equation
> 3.6 as "(6)", and figure 1.13 as "FIGURE 13". Navigate by chapter title rather than by
> chapter number. Standard 2nd-edition numbering is used throughout this repository.

---

## Attribution and licence

Workshop material is released under **CC BY-NC-SA 4.0**; see `LICENSE`.

This workshop draws on these open resources, all **CC BY-NC-SA 4.0**. The share-alike
condition propagates, which is why this repository carries the same licence:

- **Pasha, I. & Agostino, C.**, *Python for Astronomers* · <https://prappleizer.github.io/>
- **Zingale, M.**, *Tutorial on Computational Astrophysics* · <https://zingale.github.io/comp_astro_tutorial/>
- **Rougier, N. P.**, *Scientific Visualization: Python + Matplotlib* · <https://github.com/rougier/scientific-visualization-book>
- **Learn Astropy** · <https://learn.astropy.org/>

Also recommended, and referenced in the notebooks:

- **Ting, Y.-S. (2025)**, *Statistical Machine Learning for Astronomy* · <https://arxiv.org/abs/2506.12230>
- **Astro-330**, Scientific Computing in Astrophysics (Yale) · <http://Astro-330.github.io>
- **astroML** · <http://www.astroml.org/astroML-notebooks/>

### Required data acknowledgement

If you publish anything using Gaia data pulled with these notebooks:

> This work has made use of data from the European Space Agency (ESA) mission
> [Gaia](https://www.cosmos.esa.int/gaia), processed by the Gaia Data Processing and
> Analysis Consortium ([DPAC](https://www.cosmos.esa.int/web/gaia/dpac/consortium)).
> Funding for the DPAC has been provided by national institutions, in particular the
> institutions participating in the Gaia Multilateral Agreement.

Please also cite Astropy, NumPy, SciPy, matplotlib and scikit-learn. Each publishes a
preferred citation.

### AI Disclosure

Generative AI tools assisted in drafting and revising portions of the notebook content and
this documentation, including code comments, explanatory text and structural suggestions.
All code was written, run and checked against the cited textbook sections and archive
schemas before inclusion. Any errors that remain are the author's, not the tool's.

---

## Contact

**Lanz Anthonee Avila Lagman, MSc**
PhD Data Science, University of the Philippines Diliman
GitHub: [@lanzlagman](https://github.com/lanzlagman) · LinkedIn: [lanz-anthonee-lagman](https://linkedin.com/in/lanz-anthonee-lagman)

Issues and pull requests welcome. If a notebook breaks in a future library version, open an
issue: a notebook that throws an import error in 2028 is worse than no notebook, because it
teaches students the material is inaccessible rather than that the environment drifted.
