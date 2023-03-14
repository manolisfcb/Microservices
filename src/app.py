from flask import Flask, jsonify, render_template
import socket
app = Flask(__name__)

def fetchDetails():
    """
    It returns the hostname and IP address of the machine on which the function is executed.
    :return: The hostname and IP address of the machine.
    """

    host_name = socket.gethostname()
    ip = socket.gethostbyname(host_name)
    
    return str(host_name), str(ip)


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

    resp = jsonify(status = "UP")
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
    
@app.route("/details_host")
def details_dinamico():
    """
    Creando un endpoint simples para la API com html dinamico
    http://127.0.0.1:5000/details_host

    Returns:
        trmplate html: index.html
    """
    hostname, ip = fetchDetails()
    
    
    return render_template("index_host.html", hostname=hostname, ip=ip)
    

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000, debug=True)