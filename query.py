import os
import cv2
from os import listdir
from descriptors import bitdesc, glcm, haralick_with_mean, haralick_glcm, haralick_bitdesc,bit_glcm
from paths import kth_dir, kth_path, data_base_feachures_paht, data_base_feachures_dir
import pandas as pd
import numpy as np
from scipy.spatial import distance
from distances import distance_selection

path_list = list()
class_list = list()
sign_list = list()
ListOfDescriptors = (("bitdesc",bitdesc), 
                         ("glcm", glcm), 
                         ("haralick_with_mean", haralick_with_mean), 
                         ("haralick_glcm", haralick_glcm), 
                         ("haralick_bitdesc", haralick_bitdesc), 
                         ("bitdesc_glcm", bit_glcm))
def  Compute_distance(search_number, img,typ_distance, option_descriptor) :
    distancesList = list()
    path_list.clear()
    query = 'upload_images/query_image.png'
    #signatures = np.load('kth_signatures_bitdesc_new.npy')
    #Read my numpy file .._signatures_....npy
    for signature, containt in zip(listdir(data_base_feachures_paht), data_base_feachures_dir):
        option = containt.split("signatures_")
        option = option[1].split(".")
        if option[0] == option_descriptor.lower():
            #signatures = signature     
            signatures = np.load(f"Data_Base_Feachures/{signature}")
    #print('signature**************************',signatures)
    #Read image choise with a descriptor
    for descrip_name, descriptor in ListOfDescriptors:
        if option_descriptor.lower() == descrip_name :
            descriptor_choice = descriptor
            bit_feat = descriptor_choice(img)
    #print('descriptors************************',descriptor_choice)
    
    #print('bit_feat************************',bit_feat)
    # Compute distance (Similarity)
    for sign in signatures:
        sign = np.array(sign)[0 : -2].astype('float')
        sign = sign.tolist()
        #print('sign************************',sign)
        # Compute cityblock
        dis = distance_selection(typ_distance, bit_feat, sign)
        distancesList.append(dis)
    minDistances = list()
    for i in range(search_number):
        array = np.array(distancesList)
        minDistances.append(np.argmin(array))
        max = array.max()
        distancesList[np.argmin(array)] = max
    for small in minDistances:
        path = signatures[small][-1]
        class_name = signatures[small][-2 : -1]
        sign = signatures[small][0 : -3]
        path_list.append(path)
        class_list.append(path)
        sign_list.append(path)
    return path_list


#test =Compute_distance( 5)
