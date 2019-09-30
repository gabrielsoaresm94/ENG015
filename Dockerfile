FROM ubuntu:18.10
# FROM ubuntu:16.04

# RUN add-apt-repository ppa:ubuntugis/ppa
# RUN deb http://ppa.launchpad.net/ubuntugis/ubuntugis-unstable/ubuntu xenial main 

RUN apt-get update
RUN apt-get install -y python3 python3-dev python3-pip nginx
RUN apt-get install -y gdal-bin libgdal-dev

COPY requirements.txt /
RUN pip3 install -r /requirements.txt

COPY . /app
RUN mkdir /app/report
RUN mkdir /app/data
WORKDIR /app

COPY . /app
WORKDIR /app

EXPOSE 5000

CMD [ "python3", "./index.py" ]