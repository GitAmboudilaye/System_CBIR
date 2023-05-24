import os
import cv2
from os import listdir
from descriptors import bitdesc, glcm, haralick_with_mean, haralick_glcm, haralick_bitdesc,bit_glcm
from paths import kth_dir, kth_path
import pandas as pd
import numpy as np
# Extract features with haralick
def main():
    listOflists = list()
    ListOfNames = list()
    ListOfClasses = list()
    ListOfDescriptors = (("bitdesc",bitdesc), 
                         ("glcm", glcm), 
                         ("haralick_with_mean", haralick_with_mean), 
                         ("haralick_glcm", haralick_glcm), 
                         ("haralick_bitdesc", haralick_bitdesc), 
                         ("bit_glcm", bit_glcm))
    for descrip_name, descriptor in ListOfDescriptors:
        print('Extracting features ...')
        for kth_class in kth_dir:
            print('Current class: ', kth_class) 
            for filename in listdir(kth_path + kth_class + "/"):
                #print(kth_class, kth_dir.index(kth_class), filename)
                img_name = kth_path + kth_class + "/" + filename
                ListOfNames.append(img_name)
                ListOfClasses.append(kth_class)
                #print(img_name, kth_dir.index(kth_class))
                # Read image
                img = cv2.imread(img_name, 0) 
                #extraction           
                features = descriptor(img) + [kth_class] + [img_name]
                #print(features)
                listOflists.append(features)
                print(f'Current folder: {kth_class}')
        final_array = np.array(listOflists)
        #Save feachures in specificity forlder
        folder = "Data_Base_Feachures"
        if not os.path.exists(folder):
            os.makedirs(folder)
        #Build  numpy file path
        file_path = os.path.join(folder, f'kth_signatures_{descrip_name}.npy')
        #Save file
        np.save(file_path, final_array)
        listOflists.clear()
        ListOfNames.clear()
        ListOfClasses.clear()
    
        print(f'Extraction {descrip_name} concluded successfully!')
  
if __name__ == '__main__':
    main()