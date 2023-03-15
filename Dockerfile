FROM  python:3.10.0-alpine3.15
WORKDIR /app


COPY . /app
RUN pip install -r requirements.txt

COPY src .
EXPOSE 5000


CMD [ "flask", "run","--host","0.0.0.0","--port","5000"]
