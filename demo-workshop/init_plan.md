

**Goal:** Try to detect then visualize the 30 open clusters (OCs) discussed from [Liu et, al. (2025)](https://arxiv.org/pdf/2504.08179)

# I. Download Gaia DR3 Dataset Sample

## A. Prepare ADQL Query 

### 1. Get relevant columns from Gaia DR3 to save

### 2. Construct preprocessing component of ADQL

### 3. Finalize ADQL query template

## B. Run ADQL Query

### 1. Perform smoke test; try 100 rows first

#### a. Try to check how many items satisfy ADQL query

### 2. Implement fail-safe ADQL query execution

#### a. Make a function to perform chunking

#### b. Finalize file directory destination

#### c. Implement try/except condition

## C. Save Query Results

### 1. Concatenate chunks

### 2. Visualize initial results

# II. Preprocessing of DR3 Dataset before ML Algo Fitting

## A. Perform Exploratory Data Analysis (EDA)

### 1. Spatial distribution plotss (XYZ. XY. YZ. XZ)

### 2. Proper motion plots

### 3. HR Diagram

## B. Decide on Feature Engineering Steps

## C. Finalize Feature Engineering Pipeline (via SKLearn)

# III. Fit Data into HDBSCAN (or any other unsupervised ML algo)

## A. Fit on DBSCAN (available via SKLearn)

## B. Fit on HDBSCAN (IIRC needs a separate library)

## C. Try to Experiment on Adjusting Hyperparameters 

# IV. Extract Results then Visualize

## A. Save on Output Folder

## B. Initial Visualization of OCs, separating them from background stars

### 1. Spatial distribution plotss (XYZ. XY. YZ. XZ)

### 2. Proper motion plots

### 3. HR Diagram

# V. Perform Data Analysis on Results then Compare to RRL

## A. Perform ADQL Queries to get OC members from other RRLs

## B. Compare HDBSCAN results from RRL

### 1. Try to identify OCs from your run, via RRL

### 2. Compare membership extractions

## C. Characterize spatio-kinematic and photometric properties of OCs