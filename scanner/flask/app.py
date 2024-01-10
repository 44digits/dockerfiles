import flask
import subprocess

app = flask.Flask(__name__)

@app.route("/")
def index():
    return flask.render_template('index.html')

@app.route("/scan", methods=["GET"])
def scan():
    print(flask.request.args)

    first = flask.request.args.get('fname', 'xx')
    print(first)
    last = flask.request.args.get('lname')
    print(last)

    _cc = subprocess.run(["ls", "-l"], capture_output=True)

    return _cc.stdout.decode('ascii')
