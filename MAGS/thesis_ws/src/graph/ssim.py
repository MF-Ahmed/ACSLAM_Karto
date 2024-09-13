
import os
import cv2
import matplotlib.pyplot as plt
from skimage.metrics import structural_similarity as ssim
import numpy as np
from PIL import Image


def calculate_ssim_alignment_rmse(image_path, master_map, file_name):
    # Load the image in grayscale
    image2 = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    image1 = cv2.imread(master_map_path, cv2.IMREAD_GRAYSCALE)
        
    # Resize the image to match the master map's dimensions (if needed)
    if image2.shape != image1.shape:
        image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))
        
   
    # Binarize the images (you may need to adjust the threshold)
    _, binary_mask1 = cv2.threshold(image1, 100, 255, cv2.THRESH_BINARY)
    _, binary_mask2 = cv2.threshold(image2, 100, 255, cv2.THRESH_BINARY)
    # Display the binary masks

    #print('binary_mask1.shape',binary_mask1.shape)
    #print('binary_mask2.shape',binary_mask2.shape)

    # Resize the image to match the master map's dimensions (if needed)
    if binary_mask2.shape != binary_mask1.shape:
        binary_mask2 = cv2.resize(binary_mask2, (binary_mask1.shape[1], binary_mask1.shape[0]))
        image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

    #cv2.imshow('image1', image1)
    #cv2.imshow('image2', image2)


    #cv2.imshow('binary_mask1', binary_mask1)
    #cv2.imshow('binary_mask2', binary_mask2)


    # Count the number of non-zero pixels
    non_zero_pixel_count1 = 0
    non_zero_pixel_count2 = 0

    # Iterate through the image pixels and count non-zero pixels
    for y in range(binary_mask1.shape[0]):
        for x in range(binary_mask1.shape[1]):
            if binary_mask1[y, x] == 0:
                non_zero_pixel_count1 += 1

    for y in range(binary_mask2.shape[0]):
        for x in range(binary_mask2.shape[1]):
            if binary_mask2[y, x] == 0:
                non_zero_pixel_count2 += 1

    inv_map = 255 - binary_mask1
    inv_image = 255 - binary_mask2  

    # Compute the pixel-wise difference
    difference_map = np.abs(binary_mask1 - binary_mask2)          

    #non_zero_pixel_count1 = cv2.countNonZero(image1)
    #non_zero_pixel_count2 = cv2.countNonZero(image2)

    #print(f'No. of zero (black) pixels for map are {non_zero_pixel_count1}, and that of image are {non_zero_pixel_count2}')
    # Calculate SSIM


    ssim_score = ssim(binary_mask1 ,  binary_mask2, win_size=125)
     # Calculate Alignment Error (assuming both images have the same dimensions)
    alignment_error = np.sum(np.abs(difference_map))
    
    # Calculate RMSE
    rmse_score = np.sqrt(np.mean(binary_mask2  - binary_mask1) ** 2)      


    print(f'image = {file_name}, ssim_score = {ssim_score}, rmse_score = {rmse_score}, alignment_error = {alignment_error}')
    
    return ssim_score, alignment_error, rmse_score
    

'''
master_map_path = "/home/usr/data/catkin_ws/src/aslam_turtlebot_dopt/aslam_turtlebot_dopt/results/office_full_map_gazebo.pgm"
folder_path = "/home/usr/data/catkin_ws/src/aslam_turtlebot_dopt/aslam_turtlebot_dopt/results/office/1_R_Our"
folder_path = "/home/usr/data/catkin_ws/src/aslam_turtlebot/results/simulation/office/maps"
folder_path = "/home/usr/data/catkin_ws/src/aslam_turtlebot_dopt/aslam_turtlebot_dopt/results/office/1_R_AGS"

'''


master_map_path = "/home/usr/data/catkin_ws/src/aslam_turtlebot_dopt/aslam_turtlebot_dopt/results/willowgarage/willow_full_raw.pgm"
#folder_path = "/home/usr/data/catkin_ws/src/aslam_turtlebot_dopt/aslam_turtlebot_dopt/results/willowgarage/1R_our"
#folder_path = "/home/usr/data/catkin_ws/src/aslam_turtlebot_dopt/aslam_turtlebot_dopt/results/willowgarage/1R_AGS"
folder_path = "/home/usr/data/catkin_ws/src/aslam_turtlebot/results/simulation/willowgarage/maps/1R_WG_Frontier"




print(folder_path)

master_map = cv2.imread(master_map_path, cv2.IMREAD_GRAYSCALE)
file_list = os.listdir(folder_path)

results = {}

avg_rmse_list =[]
avg_AE_list =[] 


# Constants to normalize RMSE and Alignment error
max_alignment_error = master_map.size * 255  # Maximum possible alignment error
max_rmse = 100.0  # Maximum possible RMSE for grayscale images

for file_name in file_list:
    file_path = os.path.join(folder_path, file_name)

    if os.path.isfile(file_path):
        ssim_score, alignment_error, rmse_score = calculate_ssim_alignment_rmse(file_path, master_map, file_name)
        
        # Normalize the alignment error and RMSE
        normalized_alignment = alignment_error / max_alignment_error
        normalized_rmse = rmse_score / max_rmse

        results[file_name] = {'SSIM': ssim_score, 'Alignment': normalized_alignment, 'RMSE': normalized_rmse}
        
        avg_rmse_list.append(rmse_score)
        avg_AE_list.append(alignment_error)
        # Display the image
        #image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
        #plt.figure()
        #plt.imshow(image, cmap='gray')
        #plt.title(f'SSIM: {ssim_score:.2f}, Alignment: {normalized_alignment:.2f},RMSE: {normalized_rmse:.2f}, file: {file_name}')
        #plt.show()

# Sort the results by SSIM in descending order
sorted_results = {k: v for k, v in sorted(results.items(), key=lambda item: item[1]['SSIM'], reverse=True)}

# Calculate the average SSIM, normalized Alignment, and normalized RMSE
total_ssim = sum(result['SSIM'] for result in sorted_results.values())

try:
    average_ssim = total_ssim / len(sorted_results)

except ZeroDivisionError as e:
    # Handle the division by zero error
    print("Division by zero error:", e)


total_normalized_alignment = sum(result['Alignment'] for result in sorted_results.values())
average_normalized_alignment = total_normalized_alignment / len(sorted_results)

total_normalized_rmse = sum(result['RMSE'] for result in sorted_results.values())
average_normalized_rmse = total_normalized_rmse / len(sorted_results)

avg_rmse = sum(avg_rmse_list)/len(file_list)
avg_AE = sum(avg_AE_list)/len(file_list)

print(f"Average SSIM: {average_ssim:.2f}")
print(f"Average RMSE: {avg_rmse/10:.2f}")
print(f"Average Alignment: {avg_AE:.2f}")
