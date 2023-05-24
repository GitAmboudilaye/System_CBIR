import mahotas.features as ft #haralick
from skimage.feature import graycomatrix, graycoprops # Scikit-image
from BiT import biodiversity, taxonomy # Bitdesc
import numpy as np

#Define Haralick 
def haralick(data):
    all_statistics = ft.haralick(data)
    return all_statistics
def haralick_with_mean(data):
    all_statistics = ft.haralick(data).mean(0)
    return all_statistics.tolist()


# Define Bitdesc
def bitdesc(data):
    bio = biodiversity(data)
    taxo = taxonomy(data)
    all_statistics = bio + taxo # concatenation
    return all_statistics

# Define GLCM
def glcm(data):
    glcm = graycomatrix(data, [2], [0], 256, symmetric=True, normed=True)
    diss = graycoprops(glcm, 'dissimilarity')[0,0]
    cont = graycoprops(glcm, 'contrast')[0,0]
    corr = graycoprops(glcm, 'correlation')[0,0]
    ener = graycoprops(glcm, 'energy')[0,0]
    homo = graycoprops(glcm, 'homogeneity')[0,0]
    all_features = [diss, cont, corr, ener, homo]
    return all_features

#Define bitdesc + glcm
def bit_glcm(data):
    all_features = bitdesc(data) + glcm(data)
    return all_features

#Define haralick + bitdesc
def haralick_bitdesc(data):
    all_statistics = haralick_with_mean(data) + bitdesc(data)
    return all_statistics

#Define haralick + glcm
def haralick_glcm(dada):
    all_features = haralick_with_mean(dada) + glcm(dada)
    return all_features
    

