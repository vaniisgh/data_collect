from os.path import split

from flask import config
from typing_extensions import runtime
from flask_sqlalchemy import SQLAlchemy

import celery
import pandas as pd


#utility to check for extensions that will be accepted during upload
ALLOWED_EXTENSIONS = {'csv', 'txt'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def upload_chunk(chunk=pd.DataFrame, file_name=str,db=SQLAlchemy):
        chunk.to_sql(file_name, con=db.get_engine(), if_exists='append')
        print(chunk)

#to run background task
@celery.task
def dataUpload(file,db):
    location, file_name = split(file)
    rows_done=0
    lines_number = sum(1 for line in open(file))
    csv_reader = pd.read_csv(file, chunksize=1000)
    for chunk in csv_reader:
        upload_chunk(chunk,file_name,db)
        rows_done+=1000
        status = int(round(float(rows_done)/lines_number * 100))


#to download data from the /list endpoint
class processClassDownload:

    def __init__(self,table,db):
        self.status = 0
        self.file = table
        self.db = db
        self.thread = threading.Thread(target = self.dataDownload())

    def dataDownload(self):
        location, file_name = split(self.file)
        rows_done=0
        lines_number = sum(1 for line in open(self.file))
        #read from SQLAlchemy database
        #csv_reader = pd.read_csv(self.file, chunksize=1000)
        #for chunk in csv_reader:
        #    upload_chunk(chunk,file_name,self.db)
        #    rows_done+=1000
        #    self.status = int(round(float(rows_done)/lines_number * 100))

    def run(self):
            self._running = True

    def stop(self):
            self._running = False


