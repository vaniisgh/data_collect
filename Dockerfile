FROM python:3.6-alpine

RUN pip3 install --upgrade pip setuptools

WORKDIR /home/data_collect

RUN python -m venv venv

COPY app app
COPY app.py app.py
COPY setup.py setup.py


ENV FLASK_APP app.py

RUN source venv/bin/activate
RUN python setup.py develop

EXPOSE 127
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]