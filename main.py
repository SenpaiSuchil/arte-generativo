from imageToAscii import *
from randomizer import *
from imageCreator import *

#este archivo planea ser alguna especie de menú para modificar de diferentes maneras una imagen
#planeo hacer image to ascii, glitch art y demas pruebas con pillow



if __name__ == "__main__":
    #imagePath=input("ingrese la ruta de la imagen:\n")
    imagePath="test_images/clown.jpeg"
    # image=imageToAscii(imagePath)
    # glitch=glitchImage(imagePath)
    # file=open("ascii.txt", "w")
    # file.write(image)
    # file.close()
    # print(image)
    applyFilter(imagePath)
