from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def theme():
    return render_template('theme.html')


@app.route('/document')
def document():
    return render_template('document.html')


if __name__ == '__main__':
    app.run(debug=True)