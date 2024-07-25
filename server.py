# from flask import Flask, jsonify, request
# import datetime
# import atexit
# from apscheduler.schedulers.background import BackgroundScheduler

# app = Flask(__name__)

# last_run_time = None

# @app.route("/demo")
# def cron_status():
#     global last_run_time
#     client = request.args.get('client')
#     if client == 'gas':
#         return "Glitch woke up"
#     message = last_run_time
#     return jsonify({"mes": message},{"time": last_run_time})

# def my_cron_job():
#     global last_run_time
#     last_run_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# scheduler = BackgroundScheduler()
# scheduler.start()
# scheduler.add_job(
#     func=my_cron_job,
#     trigger="interval",
#     minutes=2,
#     id='my_cron_job_id',
#     name='Print every 2 minutes',
#     # replace_existing=True
# )

# atexit.register(lambda: scheduler.shutdown())

# @app.route("/")
# def hello():
#     client = request.args.get('client')
#     if client == 'gas':
#         return "Glitch woke up"
#     return jsonify({"msg":"hello deploy from flask glitch"})

# if __name__ == "__main__":
#     app.run()



# @app.route("/hello")
# def hello2():
#   return "This is a test"

# if __name__ == "__main__":
#   app.run()






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

# from get_data.clear_up import merge_data

# load_dotenv()

# app = Flask(__name__)


# # データベース接続設定
# app.config['SQLALCHEMY_DATABASE_URI'] = (
#     f"postgresql://{os.getenv('PGUSER')}:{os.getenv('PGPASSWORD')}@"
#     f"{os.getenv('PGHOST')}:{os.getenv('PGPORT', 5432)}/{os.getenv('PGDATABASE')}?sslmode=require"
# )
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)


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
#     ranking = db.Column(db.String(10), nullable=False)
#     title = db.Column(db.String(100), nullable=False)
#     author = db.Column(db.String(100), nullable=False)
#     image = db.Column(db.String(100), nullable=False)
#     score = db.Column(db.String(10), nullable=False)



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
#         # データの取得
#         new_data = merge_data()
#         # dataテーブルの全レコードをクラスが入った配列で返す
#         data = session.query(Data).all()
#         if data:
#             # dataテーブルの全レコードをupdate
#             session.query(Data).update(new_data)
#         else:
#             # データの追加
#             session.add_all(new_data)
#     return "Periodic task completed"


# SECRET_KEY = "your_secret_key_here"
# MAX_TIME_DIFFERENCE = 300
# ALLOWED_IPS = ['64.18.0.0/20', '64.233.160.0/19', '66.102.0.0/20', '172.217.26.238:443']

# limiter = Limiter(
#     app,
#     key_func=get_remote_address,
#     default_limits=["5 per minute", "1 per second"]
# )

# def generate_token(timestamp):
#     message = str(timestamp).encode()
#     signature = hmac.new(SECRET_KEY.encode(), message, hashlib.sha256).digest()
#     return base64.b64encode(signature).decode()

# def ip_in_network(ip, network):
#     return ip_address(ip) in ip_network(network)

# @app.before_request
# def limit_remote_addr():
#     if request.remote_addr:
#         if not any(ip_in_network(request.remote_addr, network) for network in ALLOWED_IPS):
#             abort(403)

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

# if __name__ == '__main__':
#     app.run(debug=True)










# 本コードのコピー
# from flask import Flask, jsonify, request
# import datetime
# import atexit
# from apscheduler.schedulers.background import BackgroundScheduler

# app = Flask(__name__)

# last_run_time = None

# @app.route("/demo")
# def cron_status():
#     global last_run_time
#     client = request.args.get('client')
#     if client == 'gas':
#         return "Glitch woke up"
#     message = last_run_time
#     return jsonify({"mes": message},{"time": last_run_time})

# def my_cron_job():
#     global last_run_time
#     last_run_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# scheduler = BackgroundScheduler()
# scheduler.start()
# scheduler.add_job(
#     func=my_cron_job,
#     trigger="interval",
#     minutes=2,
#     id='my_cron_job_id',
#     name='Print every 2 minutes',
#     # replace_existing=True
# )

# atexit.register(lambda: scheduler.shutdown())

# @app.route("/")
# def hello():
#     client = request.args.get('client')
#     if client == 'gas':
#         return "Glitch woke up"
#     return jsonify({"msg":"hello deploy from flask glitch"})

# if __name__ == "__main__":
#     app.run()



# @app.route("/hello")
# def hello2():
#   return "This is a test"

# if __name__ == "__main__":
#   app.run()






# 2024/7/10/12:00
from flask import Flask, request, abort
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

from get_data.clear_up import merge_data

load_dotenv()

app = Flask(__name__)



# 仮のデータ
kari_data = [{'ranking': 3, 'title': '名探偵コナン', 'author': '青山剛昌','image':'ima', 'score': 15}, {'ranking': 1, 'title': 'ノルウェイの森', 'author': '村上春樹', 'image':'ima', 'score': 14}, {'ranking': 2, 'title': '海辺のカフカ', 'author': '村上春樹', 'image':'ima', 'score': 12}, {'ranking': 4, 'title': 'マジック快斗', 'author': '青山剛昌', 'image':'ima', 'score': 9}]


# データベース接続設定
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"postgresql://{os.getenv('PGUSER')}:{os.getenv('PGPASSWORD')}@"
    f"{os.getenv('PGHOST')}:{os.getenv('PGPORT', 5432)}/{os.getenv('PGDATABASE')}?sslmode=require"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


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
    ranking = db.Column(db.String(10), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    score = db.Column(db.String(10), nullable=False)



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
        # new_data = merge_data()
        
        new_data = kari_data
        
        # dataテーブルの全レコードをクラスが入った配列で返す
        data = session.query(Data).all()
        if data:
            # dataテーブルの全レコードをupdate
            session.query(Data).update(new_data)
        else:
            # データの追加
            session.add_all(new_data)
    return "Periodic task completed"


SECRET_KEY = "your_secret_key_here"
MAX_TIME_DIFFERENCE = 300
ALLOWED_IPS = ['64.18.0.0/20', '64.233.160.0/19', '66.102.0.0/20', '172.217.26.238:443']

# limiter = Limiter(
#     key_func=get_remote_address,
#     app=app,
#     default_limits=["50 per day", "20 per hour", "1 per minute"]
# )

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
# @limiter.limit("5 per minute")
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
def hello2():
  return "This is a test"
  
if __name__ == '__main__':
    app.run(debug=True)