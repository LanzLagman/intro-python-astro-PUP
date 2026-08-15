# Part 2: The Strategizing Session

**Computational and Data-driven Astrophysics: A Practical Python Workshop**
PUP Physics Society

An open Q&A session built around three published papers. There are no notebooks for this
one, and that is the point.

---

## What this session is for

Notebooks 01 to 06 walked you through a sequence somebody else decided. Useful, but you were
being led the whole way.

Research does not arrive as a numbered list of cells. It arrives as a paper you want to
understand and a blank file. The skill nobody teaches is what happens in between: turning
a results section into an ordered list of things you can actually run.

That skill is a **markdown plan**, written by hand, before any code.

---

## Pick your track

You can do any of these. All three are legitimate outcomes for the session.

### Option A: Replicate one figure

Choose a paper below, choose the one figure named in its card, and write the plan to
reproduce it. Not the paper. One figure.

The goal is not to match the published numbers. It is to reach the end of your plan and be
able to say *why* your number differs, which is a harder and more useful skill than agreeing.

### Option B: Plan your own research

If you already have a topic, a thesis idea, or a dataset you have been circling, use the
same template on that instead. The papers below become worked examples of what a good
decomposition looks like rather than the task itself.

### Option C: Both

Replicate a figure first, because it is easier to plan something where the answer is known.
Then turn the same template on your own problem, where it is not.

---

## The plan template

Six headings. Fill them in this order. Sections 1 to 3 are description. Sections 4 to 6 are
where you will actually learn something.

```markdown
# Plan: <paper or project>

## 1. The claim I am reproducing
One sentence. Name the figure or the number.

## 2. Data
Where it lives. The exact query or download. Roughly how many rows.

## 3. Steps
Numbered. One cell or one function each. Each step states its expected output.

## 4. What the paper does not tell me
Every value the paper uses but never states, and every choice it leaves implicit.

## 5. What I expect to go wrong
Be specific. "It might not work" is not an entry.

## 6. How I will know if I am wrong
The check, not the hope. A number to compare against, a conservation law,
a plot that would look obviously broken.
```

**On using AI for this.** Notebook 06 gave a rule: use the model for things you could do but
do not need to, and not for things you cannot do yet.

Sections 1 to 3 are things you could do. Offload them if you like.

Sections 4 to 6 are the ones you cannot do yet, and they are also the ones a model writes
most fluently and most uselessly, because writing them requires having actually read the
paper. Write those by hand. We will read them out loud and argue about them, which is the
session.

---

## Paper 1: Open clusters

**Liu, Fang, Tsai, Pang, Wang & Fu (2025)**
*Revisiting open clusters within 200 pc in the solar neighbourhood with Gaia DR3*
The Astronomical Journal 169, 326
<https://arxiv.org/abs/2504.08179>

**Five points:**

1. They take 30 open clusters within 200 pc from the Hunt & Reffert (2023) catalogue and
   rebuild the membership lists from scratch using Gaia DR3 astrometry.
2. The core idea is the **projection effect**: for a nearby cluster spread over tens of
   degrees of sky, members with identical three-dimensional velocities show *different*
   proper motions purely because of perspective. They correct for this before clustering.
3. The clustering is HDBSCAN in five dimensions (three Cartesian positions plus two
   corrected proper motions), with `min_cluster_size = 80`, `min_samples = 10`, leaf
   selection, and RobustScaler. They sample the cluster radial velocity 100 times and take
   membership probability as the fraction of runs in which a star lands in the cluster.
4. They filter spurious sources using the Rybizki et al. (2022) astrometric fidelity flag
   (v2 >= 0.5) rather than a RUWE cut, and report that this keeps more genuine members.
5. Result: on average roughly 1.5 times more members than Hunt 23, and visible elongated
   structures and tidal tails in eleven clusters including the Pleiades.

**Target figure:** Figure A.1, the Melotte 22 (Pleiades) row. Three panels: sky position,
proper motion, and colour-magnitude diagram, with the members from this paper and from
Hunt 23 overplotted.

**Number to hit:** Table 1 gives 1721 Pleiades members in Hunt 23 and 1763 in this study.

**Your crutches:** NB02 for the query, NB05 for the clustering and the three-panel figure. For
HDBSCAN and for PARSEC isochrones, see the tooling section of `additional_readings.md`.

**Read this before you plan.** Two lines you wrote in the workshop are challenged by this
paper. Notebook 02 cuts on `ruwe`, which point 4 says is the weaker option. Notebook 05
clusters on raw `pmra` and `pmdec`, which point 2 says is wrong for a cluster this close.
Neither of those is a mistake you should feel bad about. Both are simplifications, and
finding out where your own simplifications break is exactly what reading a methods paper is
for.

---

## Paper 2: Exoplanets

**Huang, Burt, Vanderburg, Gunther, Shporer et al. (2018)**
*TESS Discovery of a Transiting Super-Earth in the pi Mensae System*
The Astrophysical Journal Letters 868, L39
<https://arxiv.org/abs/1809.05967>

**Five points:**

1. The first planet discovered by TESS. Eight pages, which is part of why it is on this list.
2. The host, pi Men (HD 39091), is naked-eye bright at V = 5.7 and was already known to host
   a Jovian planet on a highly eccentric 5.7 year orbit.
3. The new planet, pi Men c, has a radius of 2.04 +/- 0.05 Earth radii and an orbital period
   of 6.27 days.
4. The detection method is the one you already know: pull the light curve, detrend it, run a
   Box Least Squares periodogram, fold on the recovered period.
5. Converting transit depth into a planet radius requires the **stellar** radius, which this
   paper does not measure. It comes from elsewhere.

**Target figure:** the phase-folded transit. Recover the period yourself, fold, and plot.

**Number to hit:** P = 6.27 days first. Then attempt 2.04 Earth radii.

**Your crutches:** NB03 for periodic signals, NB04 for the figure. For `lightkurve` and Box
Least Squares, see the tooling section of `additional_readings.md`.

**Expect this to happen.** BLS will find 6.27 days without much fuss. Your radius will be
off, because transit depth depends on how you detrended, and because point 5 means you have
to go find a stellar radius the paper assumed you would look up. Both of those belong in
section 4 of your plan, written *before* you discover them.

---

## Paper 3: Gravitational waves

**LIGO Scientific Collaboration and Virgo Collaboration (2020)**
*A guide to LIGO-Virgo detector noise and extraction of transient gravitational-wave signals*
Classical and Quantum Gravity 37, 055002
<https://arxiv.org/abs/1908.11170>

**Five points:**

1. Not a discovery paper. It is the collaboration's own guide to how their data actually
   works, written because outsiders kept asking.
2. It covers detector noise properties, then the analysis methods used to detect signals and
   infer source properties, all demonstrated on the public O1 and O2 strain data.
3. There is an official companion Jupyter notebook, available on GitHub, Colab and Binder,
   plus a code repository. The answer key exists.
4. Its most useful single lesson for us: without a window applied before the FFT, spectral
   leakage correlates the phases; apply a Tukey window and the phases scatter randomly as
   expected for Gaussian noise. Your plot looks fine either way.
5. Thousands of authors and 54 pages. **Read sections 2 and 4 only.** Do not try to read it
   front to back.

**Target figure:** the whitened, band-passed strain for GW150914 with the chirp visible.

**How we will use this one:** as the worked example, together, at the start of the session.
We write a plan on the board, then open the official notebook and compare. You will see which
of your steps the collaboration also took, which you skipped, and which you invented. That
comparison is the whole exercise, and it only works because the reference implementation
exists.

**Your crutches:** NB03 for time series, NB06 for the verification habit. For `gwpy` and the
GWOSC data, see the tooling section of `additional_readings.md`.

---

## How the session runs

| | |
|---|---|
| Together | Plan the GW figure on the board. Open the official notebook. Compare. |
| In groups | Pick Option A, B or C. Write your plan. |
| Together | Read section 5 of each plan out loud. Argue. |
| Homework | Write the code against your own plan, and record where the plan was wrong. |

The plan is the deliverable, not the code. If you leave with working code and a plan you
never revised, you got the easier half.

---

## One honest warning

You will not reproduce these numbers exactly, and you should not expect to. Papers omit
things. Software versions drift. Data releases get reprocessed. The Pleiades distance we
computed in Notebook 02 was 136 pc against a textbook value of 130 pc, and that gap was real
and explainable.

The measure of a good replication attempt is not agreement. It is whether you can say, in one
sentence, why you disagree.
