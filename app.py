import device as device
from flask import Flask, render_template, request
from scripts.puttysessions import putty

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('clisessions.html')


@app.route('/puttysessions', methods=["GET", "POST"])
def putty1():
    if request.method == 'POST':
        result = request.form.to_dict()
        ip = putty(result['ip'])
        return render_template('clisessions.html', result=putty(ip))
    else:
        return render_template('clisessions.html')


if __name__ == "__main__":
    app.run(port=3000, debug=True)
