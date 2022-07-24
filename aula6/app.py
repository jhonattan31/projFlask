
from flask import Flask, request

app = Flask(__name__)

@app.route('/add', methods=['GET','POST'])
def add():
    if request.method == 'POST':
        return 'Post detectado'
    else:
        return "Deu certo"


if __name__ == '__main__':
    app.run(debug=True)