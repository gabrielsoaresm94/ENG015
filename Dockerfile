FROM ubuntu:18.10

RUN apt-get update
RUN apt-get install -y python3 python3-dev python3-pip python-pip nginx
RUN apt-get install -y gdal-bin libgdal-dev

RUN gdalinfo --version
RUN pip install --global-option=build_ext --global-option="-I/usr/include/gdal" GDAL==2.3.2
RUN pip3 install pygdal==2.3.2.4

COPY requirements.txt /
RUN pip3 install -r /requirements.txt

COPY . /app
RUN mkdir /app/report
RUN mkdir /app/data
WORKDIR /app

COPY . /app
WORKDIR /app

EXPOSE 8888

CMD jupyter notebook --ip=0.0.0.0 --port=8888 --allow-root