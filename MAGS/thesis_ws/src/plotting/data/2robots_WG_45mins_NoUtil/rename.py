import os


# Get the directory of the current script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Get a list of all files in the script directory
file_list = os.listdir(script_directory)

# Sort the file list to ensure consistent order
file_list.sort()

# Initialize a counter
counter = 1

# Iterate through the files in the directory
for filename in file_list:
    if filename.endswith('.npy'):  # Filter files by extension, e.g., .txt
        # Generate the new filename
        new_filename = f'sim_{counter}_2_robots-MAGS.npy'  # e.g., new_file_1.txt, new_file_2.txt, ...

        # Build the full paths to the old and new files
        old_path = os.path.join(script_directory, filename)
        new_path = os.path.join(script_directory, new_filename)

        # Rename the file
        os.rename(old_path, new_path)
        print(f'Renamed {filename} to {new_filename}')

        # Increment the counter
        counter += 1
