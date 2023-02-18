from flask import Flask, render_template

app = Flask(__name__, template_folder='../templates')


# /helloにディスパッチ
@app.route("/hello")
def hello_world():
    return "Hello, World!"


@app.route("/hello/<name>")
def hello_name(name):
    # URLの一部分(<name>)を変数として受け取る
    return f"Hello, {name}!"


@app.route("/hello/template/<name>")
def hello_template_name(name):
    # htmlテンプレートにrender
    return render_template('hello.html', name=name)


if __name__ == "__main__":
    app.run(debug=True, port=8888, threaded=True)
