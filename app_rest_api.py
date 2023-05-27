from flask import Flask,request, jsonify
from query import  Compute_distance
import numpy as np
#using for xamarin.form
import base64
app = Flask(__name__)
@app.route('/modelCBIR',methods=["POST"])
def main():
   
    """if not request or not request.method == 'POST' or not request.is_json:
        return jsonify({'error': 'Invalid request'}), 400"""
    
    requests_data = request.get_json(force=True)
    search_number = requests_data["search_number"]
    distance_typ = requests_data["distance"]
    descriptor = requests_data["descriptors"]
    img_feachure = np.array(requests_data["img_feachures"])
    path_list = Compute_distance( search_number, img_feachure, distance_typ, descriptor)
    print('papaapapapapappa', path_list)  
    return {"path": path_list}

@app.route('/upload', methods=['POST'])
def upload():
    print("/***********************************************/")
    #Récupération de l'image encodée en base64 depuis la requête POST
    image_data = request.files['image'].read()

    #Décodage de l'image depuis la base64
    decoded_image_data = base64.b64decode(image_data)

    # Écriture de l'image dans un fichier PNG
    #with open('uploaded_image.png', 'wb') as f:
        #f.write(decoded_image_data)
    #requests_data = request.get_json(force=True)
    #if requests_data["image"] ==2:
    return {"image":'Image uploaded successfully'}




if __name__ == "__main__":
    app.run(port=8008, debug=True)
    