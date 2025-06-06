# Eelgrass Classifier

This repository contains scripts to classify eelgrass in drone imagery using a Random Forest model trained on annotated pixel data.

## Problem Statement

Eelgrass is a vital estuarine plant that is natural and critical to the Moro Bay Estuary ecosystem and was at risk of disappearing until recent efforts. Accurately monitoring eelgrass distribution is a goal of the Moro Bay Estuary Program but can be a time-consuming process using traditional methods. 

This project aims to:
 -Automate the classification of eelgrass vs. non-eelgrass in drone imagery.
 -Replace ArcGIS-based workflows with open-source, scriptable, easily repeatable methods.
 -Handle large geospatial raster files using tiling methods to prevent memory issues and enable large raster files to be processed using personal workspaces.

## Methodology

### Data Preprocessing 
 1. Create Ground Truth Points:
	-Create sample pixels labeled as eelgrass (`1`) or non-eelgrass (`0`) based on imagery and denote as 'G_Code'.
	*Optional*: Have multiple users ground truth each point and use only the unanimously agreed points for accuracy. 

 2. Extract Raster Bands:
	- Sample band values (RGB) at each labeled point and create columns: `Band_1`, `Band_2`, `Band_3`.
	-Export as a 'csv' with columns: `G_Code`, `Band_1`, `Band_2`, `Band_3` representing ground truth and the 3 band values from the imagery raster. 

### Model Training (Python)

Script: `src/Train_RandomForest.py`

This script trains a Random Forest classifier using the exported training CSV.

- Input:  
  CSV file with ground truth labels and 3-band values.

- Output:  
  A saved `.pkl` model file.

-Command to run:
python src/Train_RandomForest.py

### Raster Classification (Python)

Script: src/Eelgrass_RandomTrees_Final.py     #update the file paths inside the script before running

This script reads an entire raster image, divides it into appropriately-sized tiles, applies the trained model, and creates pixel-based predictions into the output raster.

- Input:
  A 3-band '.tif' raster
  The '.pkl' trained model 
- Output
  A classified '.tif' raster with values '0' (non-eelgrass) or '1' (eelgrass).

Features: 
 -Tiling function to prevent memory overflow
 -Error handling
 -Adjustable block size to aid with performance

-Command to run:
python src/Eelgrass_RandomTrees_Final.py  #update paths inside the script for your local '.tif' model.

## Results

-Successfully processed a full raster (17.7GB) on a standard laptop.
-Output raster clearly delineated eelgrass zones from non-eelgrass zones.
-Significantly more streamlined and customizable than arduous ArcGIS Pro workflow. 

## Tools and Uses

Python: Core scripting language
scikit-learn: Machine learning 
rasterio: Raster processing
joblib: Model saving and loading
numpy, pandas: Data wrangling
ArcGIS Pro: Ground truth creation, data extraction, and visualization

## Requirements 

Install dependencies with: 
pip install -r requirements.txt

Contents of 'requirements.txt'
pandas>=1.3
numpy>=1.21
scikit-learn>=1.1
rasterio>=1.2
joblib>=1.1

## What I Learned

-How to train and use a machine learning model for a geospatial classification.
-How to efficiently handle and process large raster files.
-How to use open-source and Python workflows instead of ESRI-based workflows.
-How to document and execute version control for geospatial work. 

## Reflection 

This project challenged me to integrate concepts from GIS, coding, and machine learning into one solution to a geospatial problem. I gained valuable experience working with new dependencies, weaning away from my comfort zone in ESRI products, and understanding core python, and machine learning concepts as they apply to geospatial solutions. 