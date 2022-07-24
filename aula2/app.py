from flask import Flask

app = Flask(__name__)

def index():
    return "<h1>Indexando 1</h1>"

def teste():
    return "<h3>Testando 2</h3>"

app.add_url_rule("/teste", "teste1", index)

app.add_url_rule("/teste-2", "teste2", teste)

if __name__ == '__main__':
    app.run(debug=True, port="3000")