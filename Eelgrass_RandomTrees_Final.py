import rasterio
from rasterio.windows import Window
import numpy as np
from joblib import load
import os
import warnings

# Ignore Warning
warnings.filterwarnings("ignore", message="X does not have valid feature names")

# Paths -adjust as needed
input_raster = r"C:\Users\ethan\Downloads\eelgras23.tif"
model_path = r"C:\Users\ethan\Downloads\eelgrass_model.pkl"
output_raster = r"C:\Users\ethan\Downloads\classified_eelgrass_full.tif"

# Load Model
clf = load(model_path)
print("Model loaded.")

# Open Raster
with rasterio.open(input_raster) as src:
    profile = src.profile
    width = src.width
    height = src.height
    block_size = 128  # Adjust as needed

    # Tiles
    total_rows = (height + block_size - 1) // block_size
    total_cols = (width + block_size - 1) // block_size
    total_tiles = total_rows * total_cols

    # Output Update Raster
    profile.update(
        count=1,
        dtype=rasterio.uint8,
        compress='lzw'
    )

    # Create Output Raster
    with rasterio.open(output_raster, 'w', **profile) as dst:
        print(f"Starting full classification: {total_tiles} tiles...")

        tile_num = 0
        for row in range(0, height, block_size):
            for col in range(0, width, block_size):
                tile_num += 1
                print(f"Tile {tile_num} of {total_tiles} — row={row}, col={col}")

                win = Window(
                    col_off=col,
                    row_off=row,
                    width=min(block_size, width - col),
                    height=min(block_size, height - row)
                )

                try:
                    img = src.read(window=win)
                except Exception as e:
                    print(f"Read error at tile {tile_num}: {e}")
                    continue

                if img.shape[0] != 3:
                    print(f"Skipping incomplete tile {tile_num} — row={row}, col={col}")
                    continue

                tile_data = img.reshape(3, -1).T

                try:
                    preds = clf.predict(tile_data)
                    classified = preds.reshape(img.shape[1], img.shape[2]).astype(np.uint8)
                except Exception as e:
                    print(f"Prediction error at tile {tile_num}: {e}")
                    continue

                try:
                    dst.write(classified, 1, window=win)
                except Exception as e:
                    print(f"Write error at tile {tile_num}: {e}")
                    continue

        print("Full classification complete. Output saved to:", output_raster)