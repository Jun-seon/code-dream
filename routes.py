from flask import Flask, render_template

app = Flask(__name__)


@app.route('/theme')
def theme():
    return render_template('theme.html')


@app.route('/')
def document():
    return render_template('document.html')


if __name__ == '__main__':
    app.run(debug=True)