# Eelgrass Classifier

This repository contains scripts to classify eelgrass in drone imagery using a Random Forest model trained on annotated pixel data.

## Overview

- `Train_RandomForest.py`  
   Trains a Random Forest model using extracted band values and eelgrass labels from a CSV.

- `Eelgrass_RandomTrees_Final.py`  
   Applies the trained model to classify eelgrass vs. non-eelgrass in a raster tile-by-tile.

---

## File Descriptions

### `Train_RandomForest.py`

**Inputs:**
- A CSV file with fields `G_Code`, `Band_1`, `Band_2`, `Band_3`

**Outputs:**
- A saved Random Forest model (`eelgrass_model.pkl`)

### `Eelgrass_RandomTrees_Final.py`

**Inputs:**
- The trained model (`.pkl`)
- A 3-band raster (`.tif`)

**Outputs:**
- A classified raster (`.tif`) with 0 = non-eelgrass, 1 = eelgrass

---

## Usage

### Train the model:

```bash
python Train_RandomForest.py

Update the file paths in `Train_RandomForest.py` to your actual CSV location and column names, then run:

```bash
python Train_RandomForest.py
