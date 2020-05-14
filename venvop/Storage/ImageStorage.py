'''
En esta seccion observa la lectura y ek guardado del objeto imagen
'''
import cv2
import re


class ImageStorage:

    @staticmethod
    def read_image(path_img):
        """Leer una imagen desde el disco y devolver in objeto imagen"""
        if isinstance(path_img, str):
            img = cv2.imread(path_img)
            return img
        else:
            print("formato no valido")
            return None

    @staticmethod
    def save_img(img, name_img):
        """Guarda la imagen en el disco y valida el formato"""
        # name_img = name_img + ".jpg"
        try:
            validate = validation_string(name_img)
            if validate:
                cv2.imwrite('imagesOut/' + name_img, img)
            else:
                print('No esta en formato jpg')
        except Exception as e:
            print('El objeto que intenta llamar no se encuentra')


def validation_string(name):
    regex = re.compile("[0-9a-z]*.jpg", re.I)
    match = regex.match(str(name))
    return bool(match)
