import cv2
from skimage.metrics import structural_similarity as ssim
import numpy as np
import os

# Path to the main map file
main_map_path = '/home/usr/data/matteo_thesis/karto_slam/thesis_ws/willo.pgm'

# Path to the folder containing other .pgm map files
folder_path = '/home/usr/data/matteo_thesis/thesis_ws-tests_and_data/asynchronous_approach/maps/npy_maps_obtained'

# Load the main map file
main_map = cv2.imread(main_map_path, cv2.IMREAD_GRAYSCALE)

# Get the dimensions of the main map
main_map_height, main_map_width = main_map.shape

# Resize the main map to match the dimensions of other map files
main_map_resized = cv2.resize(main_map, (main_map_width, main_map_height))

# Initialize lists to store error values
ssim_scores = []
rmse_values = []
ae_values = []

# Iterate through the files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.pgm'):
        # Load the current map file
        current_map_path = os.path.join(folder_path, filename)
        current_map = cv2.imread(current_map_path, cv2.IMREAD_GRAYSCALE)
        
        # Check if the image is loaded successfully
        if current_map is None:
            print("Failed to load:", current_map_path)
            continue

        # Resize the current map to match the dimensions of the main map
        current_map_resized = cv2.resize(current_map, (main_map_width, main_map_height))

        # Compute SSIM
        ssim_score, _ = ssim(main_map_resized, current_map_resized, full=True)
        ssim_scores.append(ssim_score)

        # Compute RMSE
        rmse = np.sqrt(((main_map_resized - current_map_resized) ** 2).mean())
        rmse_values.append(rmse)

        # Compute Absolute Error (A.E)
        ae = np.abs(main_map_resized.astype(int) - current_map_resized.astype(int)).mean()
        ae_values.append(ae)

# Calculate average errors
avg_ssim = np.mean(ssim_scores)
avg_rmse = np.mean(rmse_values)
avg_ae = np.mean(ae_values)

# Print the average errors
print("Average SSIM:", avg_ssim)
print("Average RMSE:", avg_rmse)
print("Average Absolute Error (A.E):", avg_ae)
