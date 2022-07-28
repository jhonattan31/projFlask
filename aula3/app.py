from flask import Flask

app = Flask(__name__)

@app.route('/web/')
@app.route('/web/<nome>')
def webName(nome=''):
    return 'Meu nome é {}'.format(nome)


@app.route('/site/')
@app.route('/site/<int:postId>')
def siteId(postId=-1):
        if(postId>1):
            return 'Numero escolhido foi {}'.format(postId)
        else:
            return 'Numero nulo identificado'

if __name__ == '__main__':
    app.run(debug=True, port="3000")