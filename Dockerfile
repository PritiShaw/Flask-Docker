FROM python:3.7-stretch

RUN  apt-get update \
    && apt-get install -y wget

COPY ./src/ /src/

WORKDIR /src
RUN pip install -r requirements.txt
CMD bash setup.sh