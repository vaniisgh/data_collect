import os
from app.server import app

if __name__ == "__main__":
    app.secret_key =SECRET_KEY = os.environ.get('SECRET_KEY') or \
    b'_5#y2L"F4Q8z\n\xec]/'
    app.run(port=5001, threaded=True, host=('0.0.0.0'))
