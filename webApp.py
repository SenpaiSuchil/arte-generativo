from flask import Flask, render_template, request
import socket
import os
import PIL.Image
from glitch_this import ImageGlitcher
import random
import io

app = Flask(__name__)

@app.route('/')
def index():
    ip_address = socket.gethostbyname(socket.gethostname())
    return render_template('index.html', ip_address=ip_address)

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' in request.files:
        image = request.files['image']
        filename = image.filename
        image.save('uploads/' + filename)
        glitched_image = apply_glitch('uploads/' + filename)
        glitched_filename = 'glitched_' + filename
        glitched_image.save('uploads/' + glitched_filename)
        return render_template('index.html', filename=glitched_filename)
    return 'No se seleccionó ninguna imagen'

def apply_glitch(path):
    try:
        image = PIL.Image.open(path)
    except:
        print("Ruta no válida")
        return

    img = noise(image)
    img = glitch(img)

    # Guardar la imagen con un nombre único
    glitched_filename = generate_filename()
    glitched_save_path = os.path.join('uploads', glitched_filename)
    img.save(glitched_save_path)

    return img  # Retornar la imagen glitcheada en lugar del nombre de archivo

def noise(img):
    for i in range(round(img.size[0] * img.size[1] / random.randint(1, 10))):
        img.putpixel(
            (
                random.randint(0, img.size[0] - 1),
                random.randint(0, img.size[1] - 1),
            ),
            (
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255),
            ),
        )
    return img

def glitch(img):
    booleanRand = random.randint(0, 1)
    colorOffsetVal = True
    if booleanRand == 0:
        colorOffsetVal = False

    glitcher = ImageGlitcher()
    glitchImage = glitcher.glitch_image(
        img, random.uniform(0.1, 10.0), color_offset=colorOffsetVal
    )
    return glitchImage

def generate_filename():
    # Generar un nombre único para la imagen
    return f"glitch_{random.randint(1000, 9999)}.jpg"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)