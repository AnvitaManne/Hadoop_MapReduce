from __future__ import print_function
import os
import csv
import random 
main_data_folder='seg_train/seg_train'
output_csv_file='geodataset.csv'
try:
    all_data_rows=[]
    for terrain_folder in os.listdir(main_data_folder):
        terrain_type=terrain_folder
        terrain_folder_path=os.path.join(main_data_folder, terrain_folder)
        for image_file in os.listdir(terrain_folder_path):
            all_data_rows.append([image_file, terrain_type])

    random.shuffle(all_data_rows)
    print("\nSample data\n")
    for row in all_data_rows[:5]:
        print(row)
    with open(output_csv_file, 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(['image_id', 'terrain_type'])
        writer.writerows(all_data_rows)
        print("Prepared dataset for Map Reduce task '{0}'.".format(output_csv_file))
except Exception as e:
    print("An error occurred. Make sure you have unzipped the 'archive.zip' file.")
    print("The 'seg_train/seg_train' directory should exist.")
    print("Error details: ", e)
