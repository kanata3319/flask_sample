"""flask appの初期化を行い、flask appオブジェクトの実体を持つ"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from views import hello

app = Flask(__name__, template_folder='templates')
# Blueprintの登録
app.register_blueprint(hello.app)
# configの読み込み
app.config.from_object('app.config.Config')
# DB接続のためのインスタンス作成
db = SQLAlchemy(app)
migrate = Migrate(app, db)
