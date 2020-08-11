"""
Controller for the data upload server
"""
from flask import Flask, flash, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
#from werkzeug.utils import secure_filename

import pandas as pd
from celery import Celery
from celery.task.control import revoke

from app.utils import allowed_file, dataUpload
import app.errors as errors

app = Flask(__name__)

#register a error handler
app.register_blueprint(errors.blueprint)

#declare database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/csvs.db'
db = SQLAlchemy(app)
app.config['CELERY_BROKER_URL']='redis://localhost:6379',
app.config['CELERY_RESULT_BACKEND']='redis://localhost:6379'

#configure/initialize extensions
db.init_app(app)

def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery

celery = make_celery(app)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():

    if request.method == 'POST':

        #get file
        csv_file = request.form['file_path']

        #if user does not select file, browser also
        #submit an empty part without filename
        if csv_file == '':
            flash('No selected file')
            return redirect(request.url)

        task_id = csv_file
        if request.form.getlist('Cancel') != []:
            #end the thread
            revoke(task_id, terminate=True)
            return render_template("upload.html")

        if csv_file and allowed_file(csv_file):
            dataUpload.apply_async((csv_file,app.config['SQLALCHEMY_DATABASE_URI']),task_id=task_id)

        else:
            flash(u'File can be in csv or txt format only, please check')
            return redirect(request.url)
    return render_template("upload.html")

@app.route('/list', methods=['GET','POST'])
def list_tables():
    engine = db.get_engine()
    if request.form.getlist('Clear-all') != []:
        db.reflect()
        db.drop_all()

    return  render_template("tables.html",data=engine.table_names())

@app.route('/list/<string:table>/',methods=['GET'])
def get(table):
    table = db.session.query(db.metadata.tables[table])
    print(table)
    return render_template('upload.html',data=table)
