import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return 'Index page.'

@app.route('/hello/<name>')
def hello(name=None):
    #return name
    q = flask.request.args.get('q')
    return flask.render_template('hello.html', title='flask test', name=name, q=q) 
