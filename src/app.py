from flask import Flask, jsonify, render_template
app = Flask(__name__)

"""
Creando un endpoint simples para la API
http://127.0.0.1:5000

Returns:
    string: Hola mundo
"""

@app.route("/")
def hello_word():
    return "Hello, World!"
    

@app.route("/health")
def health_check():
    resp = jsonify({"status": "OK"})
    return resp

@app.route("/details")
def details():
    return render_template("index.html")
    

if __name__ == "__main__":
    app.run()