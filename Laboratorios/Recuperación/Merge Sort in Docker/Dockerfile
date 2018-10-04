FROM python:3.6-alpine

ENV APP_HOME=/app

LABEL MAINTAINER="IOHANNES IACOBUS 20170480" EMAIL="jotade100@gmail.com"
#directorio de trabajo
WORKDIR ${APP_HOME}


#Copiar todo al contenedor
COPY . ${APP_HOME}/

RUN pip install -r app/requirements.txt


CMD ["python","app/proceso.py"]
#se expone un puerto
EXPOSE 5000
