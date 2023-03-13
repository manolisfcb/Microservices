from flask import Flask, jsonify, render_template
app = Flask(__name__)



@app.route("/")
def hello_word():
    """
    Creando un endpoint simples para la API
    http://127.0.0.1:5000

    Returns:
        string: Hola mundo
    """
    return "Hello, World!"
    



@app.route("/health")
def health_check():
    """
    Creando un endpoint simples para la API
    http://127.0.0.1:5000/health

    Returns:
        json: {"status": "OK"}
    """

    resp = jsonify({"status": "OK"})
    return resp

@app.route("/details")
def details():
    """
    Creando un endpoint simples para la API
    http://127.0.0.1:5000/details

    Returns:
        trmplate html: index.html
    """
    return render_template("index.html")
    

if __name__ == "__main__":
    app.run()