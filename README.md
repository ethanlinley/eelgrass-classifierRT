# Eelgrass Classifier

This repository contains scripts to classify eelgrass in drone imagery using a Random Forest model trained on annotated pixel data.

## GIS Preprocessing Steps

Before using this eelgrass classification tool, you must prepare your input data using GIS software.

### 1. Generate Labeled Training Points
- Create a point feature class with labeled points (e.g., `1 = eelgrass`, `0 = non-eelgrass`)
- Field names should be standardized (`G_Code`)

### 2. Extract Band Data 

- Use GIS software to extract band from imagery (.tif) data at each point and save as `Band_1`, `Band_2`, `Band_3`

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
