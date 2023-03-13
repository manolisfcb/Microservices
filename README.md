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

Para crear un ambiente virtual en python 3 necesitamos estar la carpeta donde va a estar nuestro proyecto y luego usar el siguiente comando:

python3 -m -venv <my-env>