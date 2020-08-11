
# Data Collect

## Usage

This repository contains a small webapp that can be used to upload csv data to a
sql server, you can stop your upload at anytime and download the contents of your upload
or view them too.

A list of your uploaded files will also be present thought the session :)

### To build this repository from source

Clone or download the repository from github

```bash
cd path/to/folder/data_collect
```

Use a python3 virtual environement:

```bash
python3 -m venv /venv
source venv/bin/activate activate

# Install dependencies
pip install -r requirements.txt

# Install app
python setup.py develop
```

The flask-app in deployed on `127.0.0.1:5000\` and the upload file endpoint is:
`\upload`
To see a list of your uploads :
`\list`

### Docker deployment

ensure docker daemon is running & `cd path\to\data-collect`

build using:

```bash
docker build
OR
docker-compose build
```

docker build -t data_collect

Start

```bash
docker-compose up -d
```

### Deploy using minikube

install minikube & kubectl

```bash

```

```bash
sudo minikube start --driver=docker
```

---*---

### Other approaces & issues:

- **MAJOR LIMITATION** background tasks for one file only work one at a time,
ex you can only upload one file with a certain filepath at a time because the
backround jobs use the full file path as task id!!

- I could not find the full path for the file using a 'file' upload type and
hence the app asks user for the full filepath
- Not tested for multiple windows but should work fine

### TODO

- add a clear database button
- add users to the database with username & passwords
- catch pandas related errors

please do open issues & I will try and update this repository :)