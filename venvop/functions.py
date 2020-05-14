'''
En esta seccion se observan las clases donde estan las operaciones que se pueden realizar con el objeto imagen
'''

import cv2
import numpy as np


class Filters:
    def __init__(self, img):
        self.img = img

    def img_to_gray_scale(self):
        """
        Recibe un objeto imagen y devuleve la imagen en blanco y negro
        """
        gray_img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        return gray_img

    def img_to_vintage(self):
        """
        Recibe un objeto imagen y devuleve la imagen con un filtro vintage
        """
        rows, cols = self.img.shape[:2]
        # Create a Gaussian filter
        kernel_x = cv2.getGaussianKernel(cols, 200)
        kernel_y = cv2.getGaussianKernel(rows, 200)
        kernel = kernel_y * kernel_x.T
        filter = 255 * kernel / np.linalg.norm(kernel)
        vintage_img = np.copy(self.img)
        # for each channel in the input image, we will apply the above filter
        for i in range(3):
            vintage_img[:, :, i] = vintage_img[:, :, i] * filter
        return vintage_img

    def edge_detector(self):
        """
        Recibe el objeto imagen y contrasta los bordes del objeto
        """
        edges = cv2.Canny(self.img, 100, 300)
        return edges


class Flip(Filters):
    def __init__(self, img, id):
        super().__init__(img)
        self.id = id

    def flipping_image(self):
        """
        Recibe el objeto imagen y un id donde el id determina la postura del objeto
        """
        if isinstance(self.id, int) and (self.id == 1 or self.id == -1):
            flip1 = cv2.flip(self.img, self.id)
            return flip1
        else:
            return print('valor no aceptado')
