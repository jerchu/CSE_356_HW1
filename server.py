from flask import Flask
app = Flask(__name__, static_url_path='')

@app.route('/')
def hello_world():
    return 'Hello world'

app.run(host='0.0.0.0', port=80)
