
import numpy as np
import cv2
import matplotlib.pyplot as plt

def convolution(image, kernel):
#aqui se hace la convolucion sin padding usando el alto y ancho de la imagen
    image_row, image_col = image.shape 
    kernel_row, kernel_col = kernel.shape 

#se crea una matriz de ceros usando numpy  
    output = np.zeros(image.shape)

# se obtienen los valores del padding para que sean los mismos a los de la imagen
    pad_height = int((kernel_row - 1) / 2)
    pad_width = int((kernel_col - 1) / 2)

# se crea una matriz usando el padding 
    padded_image = np.zeros((image_row + (pad_height*2), image_col + (pad_width*2)))
    padded_image[pad_height:padded_image.shape[0] - pad_height, pad_width:padded_image.shape[1] - pad_width] = image

#se itera la matriz de la imagen  
    for row in range(image_row):
        for col in range(image_col):
            output[row, col] = np.sum(kernel * padded_image[row: row + kernel_row, col: col + kernel_col])

    return output