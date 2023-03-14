# Microservices

Micro-services in python using flask 

Este es un tutorial simple de como crear um microservicio en python usando flask. 
Tecnologias que serán usadas:

- Python
- Flask
- VSCode
- Docker
- Kubernetes

Orden lógico para seguir este Tutorial:

1- Instalar python caso no lo tengas instalado
2- Instalar VSCode o cualquier otro editor de texto con el que estes familiarizado para programar
3- Crear un ambiente virtual para nuestro proyecto (No es recomendable instalar bibliotecas directo sobre el core de python)
4- Crear Una Api en Flask para mostrar el concepto 
5- Crear a docker image usando Dockerfile
6- Escribir el Docker Compose file
7- Escribir el Manifiesto Kubernetes para nuestra aplicacion
8- Crear el Helm Chart para nuestra aplicacion

Pasos 1 y 2 están fuera del objetivo del tutorial 

## Paso 3 Crear el ambiente Virtual

3.1 Para crear un ambiente virtual en python 3 necesitamos estar la carpeta donde va a estar nuestro proyecto y luego usar el siguiente comando:

code: python3 -m -venv <my-env>

3.2 Para instalar las dependencias necesarias usar el archivo requirements.txt

code: pip install -r requirements.txt

## Paso 5 Crear el docker image:
"""https://tecadmin.net/how-to-create-and-run-a-flask-application-using-docker/"""

1 Crear un archivo llamado Dockerfile el el directorio del proyecto.
2 Añade el siguiente codigo al archivo creado:
    
    #Cargar una imagen de python para tu docker image
    FROM python:3-alpine

    # Crar un directorio para la aplicacion
    WORKDIR /app

    # istalar las dependencias del proyecto en tu imagen
    COPY requirements.txt ./

    RUN pip install -r requirements.txt

    # Bundle app source
    COPY . .

    #Selecciona el puerto por el cual vas a rodar la aplicacion 
    EXPOSE 5000

    # Ejecuta el comando en el terminal para rodar la aplicacion
    CMD [ "flask", "run","--host","0.0.0.0","--port","5000"]