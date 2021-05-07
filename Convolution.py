"""
By Abhisek Jana
code taken from https://github.com/adeveloperdiary/blog/tree/master/Computer_Vision/Sobel_Edge_Detection
blog http://www.adeveloperdiary.com/data-science/computer-vision/how-to-implement-sobel-edge-detection-using-python-from-scratch/
Modified by Benjamin Valdes and Joaquin Zermeno
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt

#esta funcion se usa para multiplicar los fragmentos por el kernel
def conv_helper(fragment, kernel):
    f_row, f_col = fragment.shape
    k_row, k_col = kernel.shape 
    result = 0.0
    for row in range(f_row):
        for col in range(f_col):
            result += fragment[row,col] *  kernel[row,col]
    return result

def convolution(image, kernel):
#aqui se hace la convolucion sin padding usando el alto y ancho de la imagen
    image_row, image_col = image.shape 
    kernel_row, kernel_col = kernel.shape 

#se crea una matriz de ceros usando numpy  
    output = np.zeros(image.shape)

#se itera la matriz de la imagen  
    for row in range(image_row):
        for col in range(image_col):
                output[row, col] = conv_helper(
                                    image[row:row + kernel_row, 
                                    col:col + kernel_col],kernel)
    return output