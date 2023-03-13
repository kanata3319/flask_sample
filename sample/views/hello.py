from flask import render_template, request, Blueprint


# Blueprintのオブジェクトを生成する
# Blueprint: アプリケーションの機能を分割できる
app = Blueprint('func', __name__)

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


@app.route("/hello/form", methods=["GET", "POST"])
def hello_form():
    # 入力フォームのサンプル
    if(request.method == 'POST'):# リクエストがPOSTの場合
        last_name = request.form.get('last_name')  # last_nameを取得
        first_name = request.form.get('first_name')  # first_nameを取得
        return render_template('hello_form.html', last_name=last_name, first_name=first_name)  # last_name, first_nameをhome.htmlに送る
    return render_template('hello_form.html')
