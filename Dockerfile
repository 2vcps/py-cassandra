FROM python:latest

RUN apt update  && apt -y install vim

COPY py-cass.py /
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /
CMD ["sleep", "84600"]