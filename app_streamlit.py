# Import Libraries
import pandas as pd
import numpy as np
import streamlit as st
import json
import requests
from upload_file import upload_file
from read_st_functions import read_img
from PIL import Image

#------route-------------

url = "http://localhost:8008/modelCBIR" #Route Predict

def main():
    global img_features
    st.set_option('deprecation.showPyplotGlobalUse', False)
    # Streamlit
    # Set up App
    st.set_page_config(page_title="Content-Based Image Retrieval (CBIR)",
                    layout="centered",
                    initial_sidebar_state="auto")
    # Add title
    st.title("Content-Based Image Retrieval")
    
    # Define sidebar title
    st.sidebar.title("Welcome Amboudilaye")
    # Define sidebar and sidebar options
    search_number = st.sidebar.number_input("Entrez un nombre entier", value=4, step=1, format="%d")
    options_distane = ["Euclidean","Canberra","Manhattan", "Chebyshev", "Minkowsky"]
    selected_option_distance  = st.sidebar.selectbox("Choose distance", options_distane)
    options_Descriptors =["Bitdesc","Bitdesc_glcm", "Haralick_bitdesc", "Haralick_glcm", "Haralick_with_mean", "GLCM"]
    selected_option_Descriptors = st.sidebar.selectbox("Descriptors", options_Descriptors)
    #uplaod image file
    
    file_path = upload_file()
    print("file path************************")
    print(file_path)

    if file_path is not None:
        
        img_features = read_img(file_path)

        jsondata = {
            "search_number": search_number,
            "distance" : selected_option_distance,
            "descriptors": selected_option_Descriptors,
            "img_feachures": img_features.tolist()
        }
        data = json.dumps(jsondata)

        res =  requests.post(url, data)
        response =res.json()
        path_list= response["path"]
        if file_path is not None:
            # Diviser l'espace en 3 colonnes pour afficher 3 images par ligne
            col1, col2, col3, col4 = st.columns(4)
            # Boucler sur les images et les afficher dans des rangées de 4 images par ligne
            for i, image_path in enumerate(path_list):
                img = Image.open(image_path)
                if i % 4 == 0:
                    col1.image(img, caption='Retrieved image')
                elif i % 4 == 1:
                    col2.image(img, caption='Retrieved image')
                elif i % 4 == 2:
                    col3.image(img, caption='Retrieved image')
                else:
                    col4.image(img, caption='Retrieved image')
            path_list.clear()

   
       
    # do    
   
   
       
        

if __name__ == "__main__":
    main()