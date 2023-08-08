""" Main (page definitions) """

import flask
import controls.sample

app = flask.Flask(__name__)                 

@app.route('/')
def index():
    return 'Index page.'

@app.route('/hello/<name>')
def hello(name=None):
    #return name
    return flask.render_template('hello.html', title='flask test', greet=controls.sample.greet(name)) 
