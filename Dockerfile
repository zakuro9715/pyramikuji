FROM python:3.4.2
MAINTAINER YuZakuro <zakuro@yuzakuro.me>

ENV APPROOT /usr/src/pyramikuji
RUN mkdir -p $APPROOT
WORKDIR /usr/src/pyramikuji

COPY setup.py /usr/src/pyramikuji/
COPY README.txt /usr/src/pyramikuji/

RUN python setup.py develop

COPY . /usr/src/pyramikuji

CMD ["pserve", "development.ini", "--reload"]
