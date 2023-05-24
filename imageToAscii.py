import PIL.Image

#arreglo de caracteres que reemplazaran los pixeles de la imgaen
#cambielos para obtener diferentes resultados

AsciiChars=["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

#funcion que le hace un resize a la imagen

def resizeImage(image, newWidth=100):
    width, height = image.size
    ratio=height/width
    newHeight=int((newWidth*ratio)/2)
    resizedImage=image.resize((newWidth, newHeight))
    return (resizedImage)

#funcion que cambia elc olor de los pixeles a una escala de grises

def grayfy(image):
    grayScaleImage=image.convert("L")
    return (grayScaleImage)


#funcion que cambia pixeles por caracteres dentro de arreglo declarado arriba
def pixelsToAscii(image):
    pixels=image.getdata()
    characters = "".join([AsciiChars[pixel//25] for pixel in pixels])
    return (characters)


def imageToAscii(path, newWidth=100):
    try:
        image=PIL.Image.open(path)
    except:
        print("ruta no valida")
        return
    newImageData=pixelsToAscii(grayfy(resizeImage(image)))
    pixel_count=len(newImageData)
    asciiImage="\n".join(newImageData[i:(i+newWidth)] for i in range(0, pixel_count, newWidth ))

    return(asciiImage)

