from flask import Flask, send_from_directory
from werkzeug.contrib.fixers import ProxyFix

from api.api import blueprint as api

app = Flask(__name__)

@app.route('/<path:path>', methods=['GET'])
def static_proxy(path):
  return send_from_directory('./static', path)

@app.route('/')
def root():
  return send_from_directory('./static', 'index.html')

app.register_blueprint(api)

if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    app.debug = True
    app.run(host='0.0.0.0')