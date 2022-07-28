
from flask import Flask, request
#from json import dumps

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    print(request.method, request.args)
    return 'ok'


if __name__ == '__main__':
    app.run(debug=True)