import json
import figuras_random
import dibuja
from flask import Flask, json, render_template, Response
app = Flask(__name__)

@app.route('/', methods=('GET', 'POST'))
def home():
    return render_template('index.html')

@app.route('/dibuja', methods=('GET', 'POST'))
def db():
    r= Response(response=dibuja.dibuja(), status=200, mimetype="image/png")
    r.headers["Content-Type"] = "image/png"
    return r

@app.route('/figuras', methods=('GET', 'POST'))
def github():
    return json.dumps({
        "figuras": [
            {
                "nombre": "cuadrado",
                "color": "red",
                "lados": 4
                
            },
            {
                "nombre": "trianguloEquilatero",
                "lados": 3
            },
             {
                "nombre": "pentagono",
                "lados": 5
            },
            {
                "nombre": "circulo",
                "lados": 0
            }
           
        ]
    })
    
@app.route('/figuras_random', methods=('GET', 'POST'))
def fr():
    return figuras_random.figuras_random()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
