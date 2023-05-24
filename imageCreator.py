import PIL.Image
from glitch_this import ImageGlitcher
import random


def imageCreator(path):
    try:
        image=PIL.Image.open(path)
    except:
        print("ruta no valida")
        return
    print(image.size[0])
    print(image.size[1])

    #de la tupla que regresa size la primera es width y la segunda es height
    crop=image.crop()