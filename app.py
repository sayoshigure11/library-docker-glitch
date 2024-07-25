# # 2024/7/10/12:00
# from flask import Flask, request, abort
# import hmac
# import hashlib
# import base64
# import time
# import os
# from contextlib import contextmanager
# from ipaddress import ip_address, ip_network
# from flask_sqlalchemy import SQLAlchemy

# from dotenv import load_dotenv
# from flask_limiter import Limiter
# from flask_limiter.util import get_remote_address

# from flask_migrate import Migrate

# from get_data.clear_up import merge_data

# load_dotenv()

# app = Flask(__name__)



# # 仮のデータ
# kari_data = [{'ranking': 3, 'title': '名探偵コナン', 'author': '青山剛昌','image':'ima', 'score': 15}, {'ranking': 1, 'title': 'ノルウェイの森', 'author': '村上春樹', 'image':'ima', 'score': 14}, {'ranking': 2, 'title': '海辺のカフカ', 'author': '村上春樹', 'image':'ima', 'score': 12}, {'ranking': 4, 'title': 'マジック快斗', 'author': '青山剛昌', 'image':'ima', 'score': 9}]


# # データベース接続設定
# app.config['SQLALCHEMY_DATABASE_URI'] = (
#     f"postgresql://{os.getenv('PGUSER')}:{os.getenv('PGPASSWORD')}@"
#     f"{os.getenv('PGHOST')}:{os.getenv('PGPORT', 5432)}/{os.getenv('PGDATABASE')}?sslmode=require"
# )
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# migrate = Migrate(app, db)

# # 
# @contextmanager
# def session_scope():
#     """セッションのコンテキストマネージャ"""
#     session = db.session
#     try:
#         yield session
#         session.commit()
#     except:
#         session.rollback()
#         raise
#     finally:
#         session.close()

# # データモデルの定義
# class Data(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     ranking = db.Column(db.Integer, nullable=False)
#     title = db.Column(db.String(100), nullable=False)
#     author = db.Column(db.String(100), nullable=False)
#     image = db.Column(db.String(100), nullable=False)
#     score = db.Column(db.Integer, nullable=False)



# # # 定期的に実行したいタスク
# # def periodic_task():
# #     with session_scope() as session:
# #         # データの取得
# #         new_data = merge_data()
# #         # データの追加
# #         session.add_all(new_data)
# #     return "Periodic task completed"


# # 定期的に実行したいタスク
# def periodic_task():
#     with session_scope() as session:
#         # # データの取得
#         # new_data = merge_data()
        
#         new_data = kari_data
        
        
        
#         # 辞書をDataモデルのインスタンスに変換します
#         new_data_instances = [Data(**item) for item in new_data]
        
        
        
#     #     # dataテーブルの全レコードをクラスが入った配列で返す
#     #     existing_data = session.query(Data).all()
#     #     if existing_data:
#     #         # dataテーブルの全レコードをupdate
#     #         session.query(Data).update(new_data)
#     #     else:
#     #         # データの追加
#     #         session.add_all(new_data)
#     # return "Periodic task completed"



#         # dataテーブルの全レコードをクラスが入った配列で返す
#         existing_data = session.query(Data).all()
#         if existing_data:
#             # 既存のデータを更新
#             for existing, new in zip(existing_data, new_data_instances):
#                 for key, value in new.__dict__.items():
#                     if key != '_sa_instance_state':
#                         setattr(existing, key, value)
#         else:
#             # 新しいデータを追加
#             session.add_all(new_data_instances)

#     return "Periodic task completed"


# SECRET_KEY = "your_secret_key_here"
# MAX_TIME_DIFFERENCE = 300
# ALLOWED_IPS = ['64.18.0.0/20', '64.233.160.0/19', '66.102.0.0/20', '172.217.26.238:443']

# limiter = Limiter(
#     key_func=get_remote_address,
#     app=app,
#     default_limits=["50 per day", "20 per hour", "1 per minute"]
# )

# def generate_token(timestamp):
#     message = str(timestamp).encode()
#     signature = hmac.new(SECRET_KEY.encode(), message, hashlib.sha256).digest()
#     return base64.b64encode(signature).decode()

# def ip_in_network(ip, network):
#     return ip_address(ip) in ip_network(network)

# @app.before_request
# def limit_remote_addr():
#     # if request.remote_addr:
#     #     if not any(ip_in_network(request.remote_addr, network) for network in ALLOWED_IPS):
#     #         abort(403)
#     pass

# @app.route('/update', methods=['POST'])
# @limiter.limit("5 per minute")
# def update():
#     token = request.headers.get('Authorization')
#     timestamp = request.headers.get('X-Timestamp')
    
#     if not token or not timestamp:
#         abort(401)
    
#     expected_token = generate_token(timestamp)
    
#     if not hmac.compare_digest(token, expected_token):
#         abort(401)
    
#     if abs(int(timestamp) - int(time.time())) > MAX_TIME_DIFFERENCE:
#         abort(401)
    
#     # ここに更新処理を記述
#     periodic_task()

#     return "Update successful", 200

  
# @app.route("/hello")
# def hello2():
  
#   # お試し
#   periodic_task()
#   return "This is a test"
  
# if __name__ == '__main__':
#     app.run(debug=True)





# 2024/7/19/11:00 試す前の保存用
from flask import Flask, request, abort, jsonify
import hmac
import hashlib
import base64
import time
import os
from contextlib import contextmanager
from ipaddress import ip_address, ip_network
from flask_sqlalchemy import SQLAlchemy

from dotenv import load_dotenv
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from flask_migrate import Migrate

from get_data.clear_up import merge_data

load_dotenv()

app = Flask(__name__)
app.json.ensure_ascii = False


# 仮のデータ
kari_data = [{'ranking': 3, 'title': '名探偵コナン0巻', 'author': '青山剛昌','image':'ima', 'score': 15}, {'ranking': 1, 'title': 'ノルウェイの森(下)', 'author': '村上春樹', 'image':'ima', 'score': 14}, {'ranking': 2, 'title': '海辺のカフカ', 'author': '村上春樹', 'image':'ima', 'score': 12}, {'ranking': 4, 'title': 'マジック快斗100巻', 'author': '青山剛昌', 'image':'ima', 'score': 9},{'ranking': 5, 'title': 'YAIBA', 'author': '青山剛昌','image':'ima', 'score': 5}]


# データベース接続設定
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"postgresql://{os.getenv('PGUSER')}:{os.getenv('PGPASSWORD')}@"
    f"{os.getenv('PGHOST')}:{os.getenv('PGPORT', 5432)}/{os.getenv('PGDATABASE')}?sslmode=require"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

migrate = Migrate(app, db)

# 
@contextmanager
def session_scope():
    """セッションのコンテキストマネージャ"""
    session = db.session
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

# データモデルの定義
class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ranking = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    score = db.Column(db.Integer, nullable=False)



# # 定期的に実行したいタスク
# def periodic_task():
#     with session_scope() as session:
#         # データの取得
#         new_data = merge_data()
#         # データの追加
#         session.add_all(new_data)
#     return "Periodic task completed"


# 定期的に実行したいタスク
def periodic_task():
    with session_scope() as session:
        # # データの取得
        new_data = merge_data()
        
        kari_data_kari = kari_data
        for item in kari_data_kari:
          item['image'] = str(time.time())
        
        # new_data = kari_data
        # new_data = kari_data_kari
        
        
        
        # 辞書をDataモデルのインスタンスに変換します
        new_data_instances = [Data(**item) for item in new_data[:40]]
        
        
        
    #     # dataテーブルの全レコードをクラスが入った配列で返す
    #     existing_data = session.query(Data).all()
    #     if existing_data:
    #         # dataテーブルの全レコードをupdate
    #         session.query(Data).update(new_data)
    #     else:
    #         # データの追加
    #         session.add_all(new_data)
    # return "Periodic task completed"



        # dataテーブルの全レコードをクラスが入った配列で返す
        existing_data = session.query(Data).all()
        print("Data",existing_data)
        if existing_data:
            # 既存のデータを更新
            for existing, new in zip(existing_data, new_data_instances):
                for key, value in new.__dict__.items():
                    if key != '_sa_instance_state':
                        setattr(existing, key, value)
        else:
            # 新しいデータを追加
            session.add_all(new_data_instances)

    return "Periodic task completed"


SECRET_KEY = "your_secret_key_here"
MAX_TIME_DIFFERENCE = 300
ALLOWED_IPS = ['64.18.0.0/20', '64.233.160.0/19', '66.102.0.0/20', '172.217.26.238:443']

limiter = Limiter(
    key_func=get_remote_address,
    app=app,
    default_limits=["50 per day", "20 per hour", "1 per minute"]
)

def generate_token(timestamp):
    message = str(timestamp).encode()
    signature = hmac.new(SECRET_KEY.encode(), message, hashlib.sha256).digest()
    return base64.b64encode(signature).decode()

def ip_in_network(ip, network):
    return ip_address(ip) in ip_network(network)

@app.before_request
def limit_remote_addr():
    # if request.remote_addr:
    #     if not any(ip_in_network(request.remote_addr, network) for network in ALLOWED_IPS):
    #         abort(403)
    pass

@app.route('/update', methods=['POST'])
@limiter.limit("5 per minute")
def update():
    token = request.headers.get('Authorization')
    timestamp = request.headers.get('X-Timestamp')
    
    if not token or not timestamp:
        abort(401)
    
    expected_token = generate_token(timestamp)
    
    if not hmac.compare_digest(token, expected_token):
        abort(401)
    
    if abs(int(timestamp) - int(time.time())) > MAX_TIME_DIFFERENCE:
        abort(401)
    
    # ここに更新処理を記述
    periodic_task()

    return "Update successful", 200

  
@app.route("/hello")
@limiter.limit("5 per minute")
def hello2():
 
  # # お試し
  # periodic_task()
  # return "This is a test"
  
  new_data = merge_data()
  # new_data = kari_data
  return jsonify(new_data)
  
if __name__ == '__main__':
    app.run(debug=True)