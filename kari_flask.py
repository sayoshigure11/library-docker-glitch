# # 2024/7/10/12:00
# from flask import Flask, request, abort, jsonify
# import hmac
# import hashlib
# import base64
# import time
# import os
# from contextlib import contextmanager
# from ipaddress import ip_address, ip_network
# # from flask_sqlalchemy import SQLAlchemy

# # from dotenv import load_dotenv
# from flask_limiter import Limiter
# from flask_limiter.util import get_remote_address

# # from flask_migrate import Migrate

# from get_data_7_25.clear_up import merge_data

# # load_dotenv()

# app = Flask(__name__)
# app.json.ensure_ascii = False


# # 仮のデータ
# kari_data = [{'ranking': 3, 'title': '名探偵コナン0巻', 'author': '青山剛昌','image':'ima', 'score': 15}, {'ranking': 1, 'title': 'ノルウェイの森(下)', 'author': '村上春樹', 'image':'ima', 'score': 14}, {'ranking': 2, 'title': '海辺のカフカ', 'author': '村上春樹', 'image':'ima', 'score': 12}, {'ranking': 4, 'title': 'マジック快斗100巻', 'author': '青山剛昌', 'image':'ima', 'score': 9},{'ranking': 5, 'title': 'YAIBA', 'author': '青山剛昌','image':'ima', 'score': 5}]


# # # データベース接続設定
# # app.config['SQLALCHEMY_DATABASE_URI'] = (
# #     f"postgresql://{os.getenv('PGUSER')}:{os.getenv('PGPASSWORD')}@"
# #     f"{os.getenv('PGHOST')}:{os.getenv('PGPORT', 5432)}/{os.getenv('PGDATABASE')}?sslmode=require"
# # )
# # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# # db = SQLAlchemy(app)

# # migrate = Migrate(app, db)

# # # 
# # @contextmanager
# # def session_scope():
# #     """セッションのコンテキストマネージャ"""
# #     session = db.session
# #     try:
# #         yield session
# #         session.commit()
# #     except:
# #         session.rollback()
# #         raise
# #     finally:
# #         session.close()

# # # データモデルの定義
# # class Data(db.Model):
# #     id = db.Column(db.Integer, primary_key=True)
# #     ranking = db.Column(db.Integer, nullable=False)
# #     title = db.Column(db.String(100), nullable=False)
# #     author = db.Column(db.String(100), nullable=False)
# #     image = db.Column(db.String(100), nullable=False)
# #     score = db.Column(db.Integer, nullable=False)


# # # データモデルの定義
# # class Data2(db.Model):
# #     id = db.Column(db.Integer, primary_key=True)
# #     ranking = db.Column(db.Integer, nullable=False)
# #     title = db.Column(db.String(100), nullable=False)
# #     author = db.Column(db.String(100), nullable=False)
# #     image = db.Column(db.String(100), nullable=False)
# #     isbn = db.Column(db.String(100), nullable=True)
# #     price = db.Column(db.Integer, nullable=True)
# #     caption = db.Column(db.String(100), nullable=True)
# #     publisher = db.Column(db.String(100), nullable=True)
# #     date = db.Column(db.String(100), nullable=True)
# #     # salesdate = db.Column(db.String(100), nullable=True)
# #     score = db.Column(db.Integer, nullable=False)



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
#     new_data = merge_data()
#     return new_data



#     # with session_scope() as session:
#     #     # # データの取得
#     #     new_data = merge_data()
        
#     #     kari_data_kari = kari_data
#     #     for item in kari_data_kari:
#     #       item['image'] = str(time.time())
        
#     #     # new_data = kari_data
#     #     # new_data = kari_data_kari
        
        
        
#     #     # 辞書をDataモデルのインスタンスに変換します
#     #     # new_data_instances = [Data2(**item) for item in new_data[:40]]
#     #     new_data_instances = [Data2(**item) for item in new_data]
        
        
        
#     # #     # dataテーブルの全レコードをクラスが入った配列で返す
#     # #     existing_data = session.query(Data).all()
#     # #     if existing_data:
#     # #         # dataテーブルの全レコードをupdate
#     # #         session.query(Data).update(new_data)
#     # #     else:
#     # #         # データの追加
#     # #         session.add_all(new_data)
#     # # return "Periodic task completed"



#     #     # dataテーブルの全レコードをクラスが入った配列で返す
#     #     existing_data = session.query(Data2).all()
#     #     print("Data2",existing_data)
#     #     if existing_data:
#     #         # 既存のデータを更新
#     #         for existing, new in zip(existing_data, new_data_instances):
#     #             for key, value in new.__dict__.items():
#     #                 if key != '_sa_instance_state':
#     #                     setattr(existing, key, value)
#     #     else:
#     #         # 新しいデータを追加
#     #         session.add_all(new_data_instances)

#     # return "Periodic task completed"


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
# @limiter.limit("5 per minute")
# def hello2():
 
#   # # お試し
#   # periodic_task()
#   # return "This is a test"
  
#   new_data = periodic_task()
#   # new_data = kari_data
#   return jsonify(new_data)
  
# if __name__ == '__main__':
#     app.run(debug=True)








# # 2024/7/10/12:00
# from flask import Flask, request, abort
# import hmac
# import hashlib
# import base64
# import time
# import os
# from contextlib import contextmanager
# from ipaddress import ip_address, ip_network

# from flask_limiter import Limiter
# from flask_limiter.util import get_remote_address

# from quart import Quart, jsonify

# from get_data_7_25.clear_up import merge_data


# # app = Flask(__name__)
# app = Quart(__name__)
# app.json.ensure_ascii = False


# # 仮のデータ
# kari_data = [{'ranking': 3, 'title': '名探偵コナン0巻', 'author': '青山剛昌','image':'ima', 'score': 15}, {'ranking': 1, 'title': 'ノルウェイの森(下)', 'author': '村上春樹', 'image':'ima', 'score': 14}, {'ranking': 2, 'title': '海辺のカフカ', 'author': '村上春樹', 'image':'ima', 'score': 12}, {'ranking': 4, 'title': 'マジック快斗100巻', 'author': '青山剛昌', 'image':'ima', 'score': 9},{'ranking': 5, 'title': 'YAIBA', 'author': '青山剛昌','image':'ima', 'score': 5}]


# # 定期的に実行したいタスク
# async def periodic_task():
#     # # データの取得
#     new_data = await merge_data()

#     # 仮
#     return new_data
    
#     # kari_data_kari = kari_data
#     # for item in kari_data_kari:
#     #     item['image'] = str(time.time())
    
#     # # new_data = kari_data
#     # # new_data = kari_data_kari
    
    
    
#     # # 辞書をDataモデルのインスタンスに変換します
#     # # new_data_instances = [Data2(**item) for item in new_data[:40]]
#     # new_data_instances = [Data2(**item) for item in new_data]
    
#     # # dataテーブルの全レコードをクラスが入った配列で返す
#     # existing_data = session.query(Data2).all()
#     # print("Data2",existing_data)
#     # if existing_data:
#     #     # 既存のデータを更新
#     #     for existing, new in zip(existing_data, new_data_instances):
#     #         for key, value in new.__dict__.items():
#     #             if key != '_sa_instance_state':
#     #                 setattr(existing, key, value)
#     # else:
#     #     # 新しいデータを追加
#     #     session.add_all(new_data_instances)

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
# @limiter.limit("5 per minute")
# async def hello2():
 
#   # # お試し
#   # periodic_task()
#   # return "This is a test"
  


# #   new_data = merge_data()
  
#   new_data = await periodic_task()
#   return jsonify(new_data)
  
# if __name__ == '__main__':
#     app.run(debug=True)



# from quart import Quart, request, abort, jsonify
# import hmac
# import hashlib
# import base64
# import time
# import os
# from contextlib import asynccontextmanager
# from ipaddress import ip_address, ip_network
# from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
# # from sqlalchemy.orm import sessionmaker
# # from sqlalchemy.ext.declarative import declarative_base
# # from flask_sqlalchemy import SQLAlchemy
# # from flask_migrate import Migrate
# from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
# from sqlalchemy.orm import declarative_base, sessionmaker
# from quart_db import Migrate


# # from dotenv import load_dotenv
# from quart_rate_limiter import RateLimiter, rate_limit
# from datetime import timedelta

# # from quart_migrate import Migrate

# from get_data_7_25.clear_up import merge_data


# # app = Flask(__name__)
# app = Quart(__name__)
# # limiter = RateLimiter(app)
# app.json.ensure_ascii = False


# # engine = create_async_engine(DATABASE_URL, echo=True)
# # async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# # Base = declarative_base()


# DATABASE_URL = "postgresql+asyncpg://user:password@host:port/dbname"
# engine = create_async_engine(DATABASE_URL)
# AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
# Base = declarative_base()

# # 仮のデータ
# kari_data = [{'ranking': 3, 'title': '名探偵コナン0巻', 'author': '青山剛昌','image':'ima', 'score': 15}, {'ranking': 1, 'title': 'ノルウェイの森(下)', 'author': '村上春樹', 'image':'ima', 'score': 14}, {'ranking': 2, 'title': '海辺のカフカ', 'author': '村上春樹', 'image':'ima', 'score': 12}, {'ranking': 4, 'title': 'マジック快斗100巻', 'author': '青山剛昌', 'image':'ima', 'score': 9},{'ranking': 5, 'title': 'YAIBA', 'author': '青山剛昌','image':'ima', 'score': 5}]

# # データベース接続設定
# app.config['SQLALCHEMY_DATABASE_URI'] = (
#     f"postgresql://{os.getenv('PGUSER')}:{os.getenv('PGPASSWORD')}@"
#     f"{os.getenv('PGHOST')}:{os.getenv('PGPORT', 5432)}/{os.getenv('PGDATABASE')}?sslmode=require"
# )
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# # migrate = Migrate(app, db)

# migrate = Migrate(app, Base)

# # # 定期的に実行したいタスク
# # async def periodic_task():
# #     # # データの取得
# #     new_data = await merge_data()

# #     # 仮
# #     return new_data

# @asynccontextmanager
# async def session_scope():
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


# # class Data2(db.Model):
# #     __tablename__ = 'data2'
    
# #     id = Column(Integer, primary_key=True)
# #     ranking = Column(Integer, nullable=False)
# #     title = Column(String(100), nullable=False)
# #     author = Column(String(100), nullable=False)
# #     image = Column(String(100), nullable=False)
# #     isbn = Column(String(100), nullable=True)
# #     price = Column(Integer, nullable=True)
# #     caption = Column(String(100), nullable=True)
# #     publisher = Column(String(100), nullable=True)
# #     date = Column(String(100), nullable=True)
# #     score = Column(Integer, nullable=False)

# # データモデルの定義
# class Data2(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     ranking = db.Column(db.Integer, nullable=False)
#     title = db.Column(db.String(100), nullable=False)
#     author = db.Column(db.String(100), nullable=False)
#     image = db.Column(db.String(100), nullable=False)
#     isbn = db.Column(db.String(100), nullable=True)
#     price = db.Column(db.Integer, nullable=True)
#     caption = db.Column(db.String(100), nullable=True)
#     publisher = db.Column(db.String(100), nullable=True)
#     date = db.Column(db.String(100), nullable=True)
#     # salesdate = db.Column(db.String(100), nullable=True)
#     score = db.Column(db.Integer, nullable=False)

# # 定期的に実行したいタスク
# async def periodic_task():
#     async with session_scope() as session:
#         # # データの取得
#         new_data = await merge_data()
        
#         kari_data_kari = kari_data
#         for item in kari_data_kari:
#           item['image'] = str(time.time())
        
#         # 辞書をDataモデルのインスタンスに変換します
#         new_data_instances = [Data2(**item) for item in new_data]
        

#         # # dataテーブルの全レコードをクラスが入った配列で返す
#         existing_data = await session.query(Data2).all()
#         # print("Data2",existing_data)

#         # existing_data = await session.execute(select(Data2))
#         # existing_data = existing_data.scalars().all()

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

# # limiter = Limiter(
# #     key_func=get_remote_address,
# #     app=app,
# #     default_limits=["50 per day", "20 per hour", "1 per minute"]
# # )

# def generate_token(timestamp):
#     message = str(timestamp).encode()
#     signature = hmac.new(SECRET_KEY.encode(), message, hashlib.sha256).digest()
#     return base64.b64encode(signature).decode()

# def ip_in_network(ip, network):
#     return ip_address(ip) in ip_network(network)

# @app.before_request
# def limit_remote_addr():
#     pass

# @app.route('/update', methods=['POST'])
# # @limiter.limit("5 per minute")
# @rate_limit(5, timedelta(minutes=1))
# async def update():
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
# @rate_limit(5, timedelta(minutes=1))
# # @limiter.limit("5 per minute")
# async def hello2():
 
#   # # お試し
#   # periodic_task()
#   # return "This is a test"
  


# #   new_data = merge_data()
  
#   new_data = await periodic_task()
#   return jsonify(new_data)
  
# if __name__ == '__main__':
#     app.run(debug=True)















# from quart import Quart, request, abort, jsonify
# import hmac
# import hashlib
# import base64
# import time
# import os
# from contextlib import asynccontextmanager
# from ipaddress import ip_address, ip_network
# from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
# from sqlalchemy.orm import declarative_base, sessionmaker
# from flask_migrate import Migrate
# from quart_rate_limiter import RateLimiter, rate_limit
# from datetime import timedelta
# from get_data_7_25.clear_up import merge_data
# from quart_sqlalchemy import SQLAlchemy

# from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
# from sqlalchemy.orm import sessionmaker, declarative_base
# from sqlalchemy import Column, Integer, String
# import asyncio
# from contextlib import asynccontextmanager



# app = Quart(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = (
#     f"postgresql+asyncpg://{os.getenv('PGUSER')}:{os.getenv('PGPASSWORD')}@"
#     f"{os.getenv('PGHOST')}:{os.getenv('PGPORT', 5432)}/{os.getenv('PGDATABASE')}?ssl=true"
# )

# DATABASE_URL = "postgresql+asyncpg://library_owner:OEdQk5qLv9JT@ep-black-hall-a1jcje8o.ap-southeast-1.aws.neon.tech/library?ssl=true"
# engine = create_async_engine(DATABASE_URL, echo=True)
# AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
# Base = declarative_base()


# db = SQLAlchemy(app)

# class Data2(Base):
#     __tablename__ = 'data2'
#     id = Column(Integer, primary_key=True)
#     ranking = Column(Integer, nullable=False)
#     title = Column(String(100), nullable=False)
#     author = Column(String(100), nullable=False)
#     image = Column(String(100), nullable=False)
#     isbn = Column(String(100), nullable=True)
#     price = Column(Integer, nullable=True)
#     caption = Column(String(100), nullable=True)
#     publisher = Column(String(100), nullable=True)
#     date = Column(String(100), nullable=True)
#     score = Column(Integer, nullable=False)


# @asynccontextmanager
# async def session_scope():
#     # async with db.session() as session:
#     async with AsyncSessionLocal() as session:
#         try:
#             yield session
#             await session.commit()
#         except:
#             await session.rollback()
#             raise

# async def periodic_task():
#     async with session_scope() as session:
#         new_data = await merge_data()

#         for item in new_data:
#             item['image'] = str(time.time())

#         existing_data = await session.execute(db.select(Data2))
#         existing_data = existing_data.scalars().all()

#         if existing_data:
#             for existing, new in zip(existing_data, new_data):
#                 for key, value in new.items():
#                     setattr(existing, key, value)
#         else:
#             session.add_all([Data2(**item) for item in new_data])

#     return "Periodic task completed"


# SECRET_KEY = "your_secret_key_here"
# MAX_TIME_DIFFERENCE = 300
# ALLOWED_IPS = ['64.18.0.0/20', '64.233.160.0/19', '66.102.0.0/20', '172.217.26.238:443']

# def generate_token(timestamp):
#     message = str(timestamp).encode()
#     signature = hmac.new(SECRET_KEY.encode(), message, hashlib.sha256).digest()
#     return base64.b64encode(signature).decode()

# def ip_in_network(ip, network):
#     return ip_address(ip) in ip_network(network)

# # @app.before_serving
# # async def startup():
# #     await engine.connect()

# # @app.after_serving
# # async def cleanup():
# #     await engine.dispose()

# @app.before_request
# async def limit_remote_addr():
#     pass

# @app.route('/update', methods=['POST'])
# @rate_limit(5, timedelta(minutes=1))
# async def update():
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
#     await periodic_task()

#     return "Update successful", 200

# @app.route("/hello")
# @rate_limit(5, timedelta(minutes=1))
# async def hello2():
#     new_data = await periodic_task()
#     return jsonify(new_data)

# if __name__ == '__main__':
#     app.run(debug=True)







# from quart import Quart, request, abort, jsonify
# import hmac
# import hashlib
# import base64
# import time
# import os
# from contextlib import asynccontextmanager
# from ipaddress import ip_address, ip_network
# from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
# from sqlalchemy.orm import declarative_base, sessionmaker
# from sqlalchemy import Column, Integer, String
# from datetime import timedelta
# from quart_rate_limiter import RateLimiter, rate_limit
# from get_data_7_25.clear_up import merge_data


# from quart import Quart, request, abort, jsonify
# import hmac
# import hashlib
# import base64
# import time
# import os
# from contextlib import asynccontextmanager
# from ipaddress import ip_address, ip_network
# from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
# from sqlalchemy.orm import declarative_base, sessionmaker
# from sqlalchemy import Column, Integer, String, select
# from datetime import timedelta
# from quart_rate_limiter import RateLimiter, rate_limit
# from get_data_7_25.clear_up import merge_data


# app = Quart(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = (
#     f"postgresql+asyncpg://{os.getenv('PGUSER')}:{os.getenv('PGPASSWORD')}@"
#     f"{os.getenv('PGHOST')}:{os.getenv('PGPORT', 5432)}/{os.getenv('PGDATABASE')}?ssl=true"
# )

# DATABASE_URL = "postgresql+asyncpg://library_owner:OEdQk5qLv9JT@ep-black-hall-a1jcje8o.ap-southeast-1.aws.neon.tech/library?ssl=require"
# engine = create_async_engine(DATABASE_URL, echo=True)
# AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
# Base = declarative_base()

# # 修正: Flask-SQLAlchemyの代わりにSQLAlchemyを直接使用
# # db = SQLAlchemy(app)

# class Data2(Base):
#     __tablename__ = 'data2'
#     id = Column(Integer, primary_key=True)
#     ranking = Column(Integer, nullable=False)
#     title = Column(String(100), nullable=False)
#     author = Column(String(100), nullable=False)
#     image = Column(String(100), nullable=False)
#     isbn = Column(String(100), nullable=True)
#     price = Column(Integer, nullable=True)
#     caption = Column(String(100), nullable=True)
#     publisher = Column(String(100), nullable=True)
#     date = Column(String(100), nullable=True)
#     score = Column(Integer, nullable=False)


# @asynccontextmanager
# async def session_scope():
#     async with AsyncSessionLocal() as session:
#         try:
#             yield session
#             await session.commit()
#         except:
#             await session.rollback()
#             raise

# async def periodic_task():
#     async with session_scope() as session:
#         new_data = await merge_data()

#         for item in new_data:
#             item['image'] = str(time.time())

        
#         stmt = select(Data2)
#         existing_data = await session.execute(stmt)
#         existing_data = existing_data.scalars().all()

#         # existing_data = await session.execute(db.select(Data2))
#         # existing_data = existing_data.scalars().all()

#         if existing_data:
#             for existing, new in zip(existing_data, new_data):
#                 for key, value in new.items():
#                     setattr(existing, key, value)
#         else:
#             session.add_all([Data2(**item) for item in new_data])

#     return "Periodic task completed"


# SECRET_KEY = "your_secret_key_here"
# MAX_TIME_DIFFERENCE = 300
# ALLOWED_IPS = ['64.18.0.0/20', '64.233.160.0/19', '66.102.0.0/20', '172.217.26.238:443']

# def generate_token(timestamp):
#     message = str(timestamp).encode()
#     signature = hmac.new(SECRET_KEY.encode(), message, hashlib.sha256).digest()
#     return base64.b64encode(signature).decode()

# def ip_in_network(ip, network):
#     return ip_address(ip) in ip_network(network)

# @app.before_request
# async def limit_remote_addr():
#     pass

# @app.route('/update', methods=['POST'])
# @rate_limit(5, timedelta(minutes=1))
# async def update():
#     token = request.headers.get('Authorization')
#     timestamp = request.headers.get('X-Timestamp')

#     if not token or not timestamp:
#         abort(401)

#     expected_token = generate_token(timestamp)

#     if not hmac.compare_digest(token, expected_token):
#         abort(401)

#     if abs(int(timestamp) - int(time.time())) > MAX_TIME_DIFFERENCE:
#         abort(401)

#     await periodic_task()

#     return "Update successful", 200

# @app.route("/hello")
# @rate_limit(5, timedelta(minutes=1))
# async def hello2():
#     new_data = await periodic_task()
#     return jsonify(new_data)

# if __name__ == '__main__':
#     app.run(debug=True)












































from quart import Quart, request, abort, jsonify
import hmac
import hashlib
import base64
import time
import os
from contextlib import asynccontextmanager
from ipaddress import ip_address, ip_network
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, select
from datetime import timedelta
from quart_rate_limiter import RateLimiter, rate_limit
from get_data_7_25.clear_up import merge_data

app = Quart(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"postgresql+asyncpg://{os.getenv('PGUSER')}:{os.getenv('PGPASSWORD')}@"
    f"{os.getenv('PGHOST')}:{os.getenv('PGPORT', 5432)}/{os.getenv('PGDATABASE')}?sslmode=require"
)

# DATABASE_URL = "postgresql+asyncpg://library_owner:OEdQk5qLv9JT@ep-black-hall-a1jcje8o.ap-southeast-1.aws.neon.tech/library?sslmode=require"
DATABASE_URL =  "postgresql+asyncpg://library_owner:OEdQk5qLv9JT@ep-black-hall-a1jcje8o.ap-southeast-1.aws.neon.tech/library?ssl=require"

engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()

class Data2(Base):
    __tablename__ = 'data2'
    # id = Column(Integer, primary_key=True)
    # ranking = Column(Integer, nullable=False)
    # title = Column(String(100), nullable=False)
    # author = Column(String(100), nullable=False)
    # image = Column(String(100), nullable=False)
    # isbn = Column(String(100), nullable=True)
    # price = Column(Integer, nullable=True)
    # caption = Column(String(100), nullable=True)
    # publisher = Column(String(100), nullable=True)
    # date = Column(String(100), nullable=True)
    # score = Column(Integer, nullable=False)

    id = Column(Integer, primary_key=True)
    ranking = Column(Integer, nullable=False)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    image = Column(String, nullable=False)
    isbn = Column(String, nullable=True)
    price = Column(Integer, nullable=True)
    caption = Column(String, nullable=True)
    publisher = Column(String, nullable=True)
    # date = Column(String, nullable=True)
    salesDate = Column(String, nullable=True)
    score = Column(Integer, nullable=False)


# # データモデルの定義
# class Data2(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     ranking = db.Column(db.Integer, nullable=False)
#     title = db.Column(db.String(255), nullable=False)
#     author = db.Column(db.String(255), nullable=False)
#     image = db.Column(db.String(255), nullable=False)
#     isbn = db.Column(db.String(100), nullable=True)
#     price = db.Column(db.Integer, nullable=True)
#     caption = db.Column(db.String(511), nullable=True)
#     publisher = db.Column(db.String(100), nullable=True)
#     date = db.Column(db.String(100), nullable=True)
#     # salesdate = db.Column(db.String(100), nullable=True)
#     score = db.Column(db.Integer, nullable=False)

@asynccontextmanager
async def session_scope():
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except:
            await session.rollback()
            raise

# async def periodic_task():
#     async with session_scope() as session:
#         new_data = await merge_data()

#         for item in new_data:
#             item['image'] = str(time.time())

#         stmt = select(Data2)
#         existing_data = await session.execute(stmt)
#         existing_data = existing_data.scalars().all()

#         if existing_data:
#             for existing, new in zip(existing_data, new_data):
#                 for key, value in new.items():
#                     setattr(existing, key, value)
#         else:
#             session.add_all([Data2(**item) for item in new_data])

#     return "Periodic task completed"

def truncate_string(value, max_length=100):
    if value and len(value) > max_length:
        return value[:max_length]
    return value

async def periodic_task():
    async with session_scope() as session:
        new_data = await merge_data()

        # for item in new_data:
        #     item['title'] = truncate_string(item['title'], 95)
        #     item['caption'] = truncate_string(item['caption'], 95)

        # for item in new_data:
        #     item['image'] = str(time.time())

        stmt = select(Data2)
        existing_data = await session.execute(stmt)
        existing_data = existing_data.scalars().all()

        if existing_data:
            for existing, new in zip(existing_data, new_data):
                for key, value in new.items():
                    if hasattr(existing, key):
                        setattr(existing, key, value)
        else:
            filtered_new_data = [{key: value for key, value in item.items() if hasattr(Data2, key)} for item in new_data]
            session.add_all([Data2(**item) for item in filtered_new_data])

    return "Periodic task completed"



SECRET_KEY = "your_secret_key_here"
MAX_TIME_DIFFERENCE = 300
ALLOWED_IPS = ['64.18.0.0/20', '64.233.160.0/19', '66.102.0.0/20', '172.217.26.238:443']

def generate_token(timestamp):
    message = str(timestamp).encode()
    signature = hmac.new(SECRET_KEY.encode(), message, hashlib.sha256).digest()
    return base64.b64encode(signature).decode()

def ip_in_network(ip, network):
    return ip_address(ip) in ip_network(network)

@app.before_request
async def limit_remote_addr():
    pass

@app.route('/update', methods=['POST'])
@rate_limit(5, timedelta(minutes=1))
async def update():
    token = request.headers.get('Authorization')
    timestamp = request.headers.get('X-Timestamp')

    if not token or not timestamp:
        abort(401)

    expected_token = generate_token(timestamp)

    if not hmac.compare_digest(token, expected_token):
        abort(401)

    if abs(int(timestamp) - int(time.time())) > MAX_TIME_DIFFERENCE:
        abort(401)

    await periodic_task()

    return "Update successful", 200

@app.route("/hello")
@rate_limit(5, timedelta(minutes=1))
async def hello2():
    # new_data = await periodic_task()
    new_data = await merge_data()
    return jsonify(new_data)


# replitの部分を試す
from get_data_7_25.api.google_api import get_book_data_google
from get_data_7_25.api.opendb_api import get_book_data_opendb
from get_data_7_25.api.opensearch_api import get_book_data_opensearch
from get_data_7_25.api.sru_api import get_book_data_sru
from get_data_7_25.api.rakuten_api import fetch_rakuten
from get_data_7_25.matome_jikkou import jikkou
# 確認用17:30 問題無し
@app.route("/google")
# @rate_limit(5, timedelta(minutes=1))
async def google():
    new_data = await get_book_data_google("9784022650597")
    # new_data = await merge_data()
    return jsonify(new_data)

@app.route("/opendb")
async def opendb():
    new_data = await get_book_data_opendb("9784022650597")
    return jsonify(new_data)

@app.route("/opensearch")
async def opensearch():
    new_data = await get_book_data_opensearch("9784022650597")
    return jsonify(new_data)

@app.route("/sru")
async def sru():
    new_data = await get_book_data_sru("9784022650597")
    return jsonify(new_data)

@app.route("/jikkou")
async def matome():
    new_data = await jikkou("9784022650597")
    return jsonify(new_data)

@app.route("/rakuten")
async def rakuten():
    new_data = await fetch_rakuten("9784022650597")
    return jsonify(new_data)


if __name__ == '__main__':
    app.run(debug=True)
