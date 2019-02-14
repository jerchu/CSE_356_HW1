# from gevent.pywsgi import WSGIServer
from flask import Flask
app = Flask(__name__, static_url_path='')

@app.route('/')
def hello_world():
    return 'Hello world'

# if __name__ == '__main__':
# 	http_server = WSGIServer(('', 80), app)
# 	http_server.serve_forever()
