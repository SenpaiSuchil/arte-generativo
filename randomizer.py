import PIL.Image
from glitch_this import ImageGlitcher
import random


def applyFilter(path):
    
    try:
        image=PIL.Image.open(path)
    except:
        print("ruta no valida")
        return
    img=noise(image)
    img=glitch(image)
    

def noise(img):
    for i in range( round(img.size[0]*img.size[1]/random.randint(1,10)) ):
        img.putpixel(
            (random.randint(0, img.size[0]-1), random.randint(0, img.size[1]-1)),
            (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        )
    return img

def glitch(img):
    booleanRand=random.randint(0,1)
    colorOffsetVal = True 
    if (booleanRand == 0):
        colorOffsetVal = False

    glitcher=ImageGlitcher()
    glitchImage=glitcher.glitch_image(img, random.uniform(0.1,10.0), color_offset=colorOffsetVal)
    glitchImage.save("test_images/glitch2.jpg")
