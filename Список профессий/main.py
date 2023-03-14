from flask import Flask, render_template

app = Flask(__name__)


@app.route('list_prof/<list>')
def index(list):
    return render_template("index.html", list=list, prof=["инженер", "пилот", "строитель"])

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

# http://127.0.0.1:8080/list_prof/ul