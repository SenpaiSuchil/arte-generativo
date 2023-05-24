import PIL.Image
from glitch_this import ImageGlitcher
import random



def glitchImage(path):
    glitcher=ImageGlitcher()
    try:
        image=PIL.Image.open(path)
    except:
        print("ruta no valida")
        return
    img=noise(image)
    glitchImage=glitcher.glitch_image(img, 4, color_offset=True)
    
    glitchImage.save("test_images/glitch.jpg")


def noise(img):
    for i in range( round(img.size[0]*img.size[1]/3) ):
        img.putpixel(
            (random.randint(0, img.size[0]-1), random.randint(0, img.size[1]-1)),
            (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        )
    return img
