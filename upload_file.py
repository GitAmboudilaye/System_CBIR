import streamlit as st
from PIL import Image
import os

def upload_file():
    global file_path
    # Upload a file using Streamlit
    upload_file = st.file_uploader("Choose an image file", type=["png","jpg","jpeg"])
    
    if upload_file is not None:
        # Specify a new file name
        new_file_name = "query_image.png" # You can also keep the original file extension

        # Construct the file path the new file name
        folder = "upload_images"
        if not os.path.exists(folder):
            os.makedirs(folder)
        file_path = os.path.join(folder, new_file_name)

        # Write the upload file with the new name
        with open(file_path, "wb") as f:
            f.write(upload_file.getbuffer())

        # Read the image using PIL
        image = Image.open(file_path)

        # Display the image in Streamlit
        st.image(image, caption="Uploaded Query Image")
        return file_path

    else:
        return None