from flask import Flask, render_template, request
import socket

app = Flask(__name__)

@app.route('/')
def index():
    ip_address = socket.gethostbyname(socket.gethostname())
    return render_template('index.html', ip_address=ip_address)


@app.route('/upload', methods=['POST'])
def upload():
    if 'image' in request.files:
        #image = request.files['image']
        #filename = image.filename
        #image.save('/uploads/' + filename)
        #return render_template('upload.html', filename=filename)
        return "imagen cargada correctamente!\nNacierto, falta agregar esta funcionalidad...jsjsjs"
    return 'No se seleccionó ninguna imagen'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
