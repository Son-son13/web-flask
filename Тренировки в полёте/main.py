from flask import Flask, render_template

app = Flask(__name__)


@app.route('/index/<prov>')
def index(prov):
    if 'инженер' in prov or 'строитель' in prov:
        return render_template("ing.html", title="Инженерный симулятор")
    else:
        return render_template("science.html", title="Научный симулятор")


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

# http://127.0.0.1:8080/index/Первый