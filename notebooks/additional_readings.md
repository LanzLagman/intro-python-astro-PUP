# Additional Readings

**Computational and Data-driven Astrophysics: A Practical Python Workshop**
PUP Physics Society, 15 August 2026

Everything listed here is free to read online. Links were checked in August 2026.

The workshop notebooks follow Carroll & Ostlie, *An Introduction to Modern Astrophysics*
(2nd ed.) for the physics. This file covers the other half: the Python and the astronomical
software. Each notebook has its own section, and the sources are ordered roughly by how
directly they follow on from what you just did.

> **A note on our PDF of Carroll & Ostlie.** It is the Pearson reprint, which assembles the
> book chapter by chapter and prints chapters *without their numbers*. So section 3.1 appears
> as plain "1", equation 3.6 as "(6)", and figure 1.13 as "FIGURE 13". Navigate by chapter
> title (*The Celestial Sphere*, *Celestial Mechanics*, *The Continuous Spectrum of Light*,
> and so on) rather than by chapter number.

---

## Start here, whatever you are working on

**Learn Astropy**
<https://learn.astropy.org/>
The official tutorial collection, rebuilt in late 2025 with a topical search sidebar. Every
tutorial is available both as a rendered web page and as a downloadable Jupyter notebook, so
you can pull cells straight into your own work. Start with whichever topic you need; it is
not meant to be read front to back.

**Pasha & Agostino, *Python for Astronomers: An Introduction to Scientific Computing***
Site: <https://prappleizer.github.io/>
PDF: <https://prappleizer.github.io/textbook.pdf>
3rd edition, 2020. Written for astronomy students with no prior programming experience, with
astronomical examples throughout. This is the gentlest on-ramp on this list.

**Pasha & Geha, *Astro 330: Scientific Computing in Astrophysics* (Yale)**
<https://astro-330.github.io/intro.html>
The sequel to the textbook above, and the single best next step after this workshop. Pasha
describes the gap it fills as "the second mile": the distance between knowing basic Python
and being able to carry a research project to completion. Full lectures, labs, solutions and
short "Quick Tips" articles, all open. Assumes you can already use NumPy arrays and make a
basic matplotlib plot, which after Notebooks 01 to 04 you can.

**Astropy Workshop materials**
Linked from <https://learn.astropy.org/>
A one-day workshop packaged for reuse in classrooms and coding clubs. Useful if you ever run
something like this yourself.

---

## Notebook 01: Setup and Astropy Fundamentals

**Learn Astropy, tutorial series on `astropy.coordinates`**
<https://learn.astropy.org/tutorials/index-coordinates.html>
Four parts. Part 1 builds a `SkyCoord`, converts between frames, and then uses it to query
the Gaia archive, which is exactly the bridge from our Part 6 into Notebook 02. Parts 2 to 4
cover coordinate transformations, velocity data, and catalogue cross-matching.

**Pasha & Agostino, Python Bootcamp Day 1 and Day 2**
<https://prappleizer.github.io/>
If any of the plain-Python syntax in this notebook felt fast, start here.

**Astropy documentation: `units` and `constants`**
<https://docs.astropy.org/en/stable/>
The reference for everything in our Part 2. Worth reading the section on how `Quantity`
propagates units through arithmetic, since that is the whole reason we use it.

---

## Notebook 02: Downloading Datasets with `astroquery`

**Gaia Archive help hub**
<https://www.cosmos.esa.int/web/gaia-users/archive/help>
The canonical index. The official Gaia DR3 documentation points here for all user tutorials,
including ADQL syntax, advanced ADQL features, pre-computed cross-matches, and catalogue
combination.

**ADQL query examples**
<https://gea.esac.esa.int/archive-help/adql/examples/>
Copy-pasteable cone searches against `gaiadr3.gaia_source`, the same shape as the query we
wrote in Part 2. The fastest way to learn ADQL is to read ten of these.

**How to write ADQL queries for Gaia data**
<https://www.cosmos.esa.int/web/gaia-users/archive/writing-queries>
A gentle ramp for anyone without SQL background. The archive implements ADQL 2.1.

**Gaia Archive use cases**
<https://www.cosmos.esa.int/web/gaia-users/archive/use-cases>
Contains an official Pleiades cluster analysis walkthrough: query by position and proper
motion, retrieve the average parallax of the members with ADQL, then cross-match against
2MASS. Available in both GUI and Python form. This is our exact target using our exact
method, done by the people who built the archive. Read it after you finish Notebook 05.

**Learn Astropy, Coordinates 4: Cross-matching catalogues**
<https://learn.astropy.org/tutorials/4_Coordinates-Crossmatch.html>
Directly supports the VizieR member-list matching in Part 4.

---

## Notebook 03: Solving ODEs with NumPy and SciPy

**Zingale, *Tutorial on Computational Astrophysics***
<https://zingale.github.io/comp_astro_tutorial/intro.html>
Two chapters map onto this notebook almost exactly:

- *Basic Methods for ODEs*
  <https://zingale.github.io/comp_astro_tutorial/basics/ODEs/ODEs-partI.html>
  Uses the same Earth-orbit test case and the same "watch it spiral outward" argument we
  used in Part 2, on the grounds that we have strong physical intuition for what a correct
  answer looks like.
- *Higher-order Accurate ODE Integration*
  <https://zingale.github.io/comp_astro_tutorial/basics/ODEs/ODEs-partII.html>
  Midpoint and Runge-Kutta methods, then adaptive timestepping. Its closing exercise is
  "integrate an orbit with a large eccentricity ($e = 0.8$)", which is our Part 4.

Every notebook there has a launch button for Colab or Binder.

**Zingale, *AST 390: Computational Astrophysics***
<https://zingale.github.io/computational_astrophysics/intro.html>
The newer and more actively maintained course book from the same author. Broader than the
tutorial above: derivatives, integration, root finding, ODEs and linear algebra first, then
astrophysical applications.

**SciPy documentation: `solve_ivp`**
Read the method comparison for RK45, DOP853, Radau and LSODA. Knowing which solver to reach
for when a system turns stiff is the single most transferable thing in this notebook.

---

## Notebook 04: Data Visualization

**Rougier, *Scientific Visualization: Python + Matplotlib***
Open access landing page: <https://www.labri.fr/perso/nrougier/scientific-visualization.html>
Sources and code: <https://github.com/rougier/scientific-visualization-book>
Part 1 covers figure anatomy, coordinate systems, scales, projections, typography and
colour, which is our Part 1. Part 2 covers rules for better figures, the matplotlib styling
system and layout, which is our Part 5. Parts 3 and 4 go into 3D, animation and showcases.
Assumes intermediate Python and beginner NumPy.

**Matplotlib cheatsheets**
<https://matplotlib.org/cheatsheets/>
Print one and put it next to your monitor. Seriously.

**Learn Astropy, tutorial series on `astropy.modeling`**
<https://learn.astropy.org/tutorials/index-models.html>
Fitting models to data, including error bars and comparing different fitters. Relevant to
our Part 4 distinction between a model figure and a data figure, and it is the natural
bridge into the main-sequence fit in Notebook 05.

---

## Notebook 05: Traditional ML in Astrophysics

**Ting (2025), *Statistical Machine Learning for Astronomy: A Textbook***
<https://arxiv.org/abs/2506.12230>
677 pages, 152 figures, free, with code and tutorials linked from the abstract page. Builds
everything through a consistently Bayesian lens, moving from probability theory through
regression *with measurement uncertainties*, classification, PCA, clustering, MCMC, Gaussian
processes and neural networks. The treatment of measurement uncertainty as first-class is
precisely the gap identified in our Part 5. **If you read one thing on this list, read this
one.**

**astroML interactive book**
<http://www.astroml.org/astroML-notebooks/>
Notebooks following the chapters of the Ivezic et al. textbook below, reproducing its
figures on real astronomical datasets. Runnable in the browser, or via Binder or Colab.

**Ivezic, Connolly, VanderPlas & Gray, *Statistics, Data Mining, and Machine Learning in
Astronomy***
<https://www.astroml.org/>
The book the notebooks accompany. 2nd edition (2019) adds deep learning, hierarchical Bayes
and approximate Bayesian computation. Errata are maintained on GitHub. The site also lists
the preferred citation format for both the book and the `astroML` package.

**scikit-learn user guide: *Clustering* and *Model selection***
The reference for DBSCAN, the alternatives to it, and the train/test discipline in our
Part 3.

---

## Notebook 06: Responsible Use of AI

This notebook deliberately has no textbook anchor. These are the sources that give its four
points formal footing, and all three are citable in a thesis.

**The Turing Way: a handbook for reproducible, ethical and collaborative data science**
<https://book.the-turing-way.org/>
Community-written, CC-BY 4.0, citable via Zenodo (DOI 10.5281/zenodo.3233853). The *Guide
for Reproducible Research* is our section 3 in full: version control, testing, reproducible
computational environments. Explicitly not meant to be read start to finish; open it at the
concept you need today.

**FORCE11 Software Citation Principles (2016)**
<https://force11.org/info/software-citation-principles-published-2016/>
Six principles: importance, credit and attribution, unique identification, persistence,
accessibility, specificity. Gives our section 4 something concrete to point at. Note their
own caveat, which is worth internalising: citing software is *necessary* for reproducibility
but not *sufficient*, since configuration and platform matter too.

**Astropy citation and acknowledgement guidance**
<https://www.astropy.org/>
Together with the citation block on <https://www.astroml.org/>, a good model for what a
preferred citation actually looks like in practice.

---

## Tooling for the Part 2 papers

Part 2 is a strategizing session built on three published papers (see
`strategizing_session.md`). These are the packages and data sources you will need if you decide
to write the code as well as the plan.

### Open clusters: Liu et al. (2025), Gaia DR3 within 200 pc

- The Gaia Archive Pleiades cluster analysis use case listed under Notebook 02.
- scikit-learn user guide, *Clustering*, for HDBSCAN and Gaussian Mixtures.
- astroML, clustering and density estimation chapters.

**Isochrones**, for overlaying a fitted age on the colour-magnitude diagram:

- **CMD 3.9 web interface** (Girardi, Osservatorio Astronomico di Padova)
  <https://stev.oapd.inaf.it/cgi-bin/cmd>
  The standard source for PARSEC isochrones. Choose your age, metallicity and photometric
  system, and it returns a table.
- **`ezpadova`** <https://mfouesneau.github.io/ezpadova/>
  Queries that interface from Python instead of the web form. Supports
  `photsys_file='gaiaEDR3'`, so you get isochrones directly in Gaia bands with no colour
  conversion, which saves a great deal of pain.
- Cite Bressan et al. (2012), MNRAS 427, 127 for PARSEC itself, plus whatever the CMD site
  currently asks for.

### Exoplanets: Huang et al. (2018), pi Mensae c

- **Lightkurve tutorials** <https://lightkurve.github.io/lightkurve/tutorials/>
  Start with *Identifying transiting exoplanet signals in a light curve*, which uses the
  `astropy.timeseries` Box Least Squares implementation.
- **MAST TESS tutorials** <https://heasarc.gsfc.nasa.gov/docs/tess/tutorial_landing.html>
  Target pixel files, full frame images, aperture photometry and noise removal. Note that
  MAST runs TIKE, a browser-based JupyterHub preconfigured for TESS, if installation is a
  problem.

### Gravitational waves: the LIGO-Virgo data analysis guide

- **GW Open Data Workshop** <https://learn.gwosc.org/>
  The current course home. Crash course in GW data analysis, with a data challenge at the
  end.
- **Workshop notebooks on GitHub**: the `gw-odw/odw-2023` repository, with Colab links in
  every notebook. Tutorial 1.2 is open data access with GWpy.
- **GWOSC standalone tutorials** <https://gwosc.org/tutorials/>
  Including matched filtering to find signals.

Remember that gravitational-wave strain data does not come through `astroquery`. It is a
continuous time series rather than a catalogue of objects, and it needs `gwpy`.

---

## Licensing, since it matters if you reuse any of this

| Resource | Licence | What that means for you |
|---|---|---|
| Pasha & Agostino | CC BY-NC-SA 4.0 | Credit them, no commercial use, and anything you build on it carries the same licence |
| Rougier | Open access, sources on GitHub | Check the repository for the current terms before redistributing |
| Zingale | Open, notebooks on GitHub | Check the repository |
| The Turing Way | CC-BY 4.0 | Credit required, commercial use allowed |
| Learn Astropy, Gaia, GWOSC, MAST | Own terms per page | Do not assume a blanket Creative Commons licence; check the specific page you are adapting |

Share-alike propagates. A free student workshop is squarely within CC BY-NC-SA terms. A paid
bootcamp built on the same material would not be.

---

*Compiled for the PUP Physics Society workshop.*
*Lanz Anthonee Avila Lagman, MSc, PhD Data Science, University of the Philippines Diliman*
