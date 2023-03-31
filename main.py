from flask import Flask, url_for
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('base.html', title='Сайт-помщник')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
