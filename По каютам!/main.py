from flask import Flask, render_template

app = Flask(__name__)


@app.route('/distibution')
def index(*l):
    return render_template("base-1.html", titile="Имена", user_list=l)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

# http://127.0.0.1:8080/index/Первый