FROM python:slim

RUN    pip3 install --upgrade pip setuptools

WORKDIR /home/data_collect

COPY app app
COPY app.py app.py

COPY requirements.txt requirements.txt

ENV FLASK_APP app.py

## Install dependencies
RUN pip3 install -r requirements.txt

EXPOSE 5001

ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]