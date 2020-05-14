'''
PROYECTO CON OPENCV
En esta seccion se muestra la parte principal donde se llaman a las demas clases
'''
from Storage.ImageStorage import ImageStorage
from functions import Filters
from functions import Flip

if __name__ == '__main__':
    img = ImageStorage.read_image("images/picture.jpg")
    img_gray = Filters(img).img_to_gray_scale()
    img_vintage = Filters(img).img_to_vintage()
    img_edges = Filters(img).edge_detector()
    img_flip = Flip(img, 1).flipping_image()
    ImageStorage.save_img(img=img_gray, name_img="gray2.jpg")
    ImageStorage.save_img(img=img_vintage, name_img='vintage2.jpg')
    ImageStorage.save_img(img_edges, 'edges.jpg')
    ImageStorage.save_img(img=img_flip, name_img="flip.jpg")
    print("El proyecto corrio exitosamente")
