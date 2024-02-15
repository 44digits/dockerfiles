import flask
import subprocess

app = flask.Flask(__name__)

@app.route("/")
def index():
    return flask.render_template(
            'index.html', 
            filepath = '/data/bingo',
            filelist=['a', 'b', 'c'])

@app.route("/scan", methods=["POST"])
def scan():
    print(flask.request.form.get('scanner'))
    print(flask.request.form.get('paper'))
    dpi = flask.request.form.get('dpi')
    print(dpi)

    _cc = subprocess.run(["ls", "-l"], capture_output=True)

    #return _cc.stdout.decode('ascii')
    return index()