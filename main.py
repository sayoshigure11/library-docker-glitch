# from flask import Flask, jsonify, request

# app = Flask(__name__)



# # https://youtu.be/8dOUauu0Og4?si=BTch5OgCffnYSTR7&t=446
# import datetime
# import atexit
# from apscheduler.schedulers.background import BackgroundScheduler
# from apscheduler.trigger.interval import IntervalTrigger


# last_run_time = None

# @app.route("/demo")
# def cron_status():
#     global last_run_time
#     client = request.args.get('client')
#     if client == 'gas':
#         return "Glitch woke up"
#     return f"Last run time of the job: {last_run_time}"

# def my_cron_job():
#     global last_run_time
#     last_run_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#     app.logger.info(f"job run at: {last_run_time}")

# scheduler = BackgroundScheduler()
# scheduler.start()

# scheduler.add_job(
#     func=my_cron_job,
#     trigger=IntervalTrigger(minutes=2),
#     id='my_cron_job_id',
#     name='Print every 2 minutes',
#     replace_existing=True
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







# おｋ
from flask import Flask, jsonify, request
import datetime
import atexit
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

last_run_time = None

@app.route("/demo")
def cron_status():
    global last_run_time
    client = request.args.get('client')
    if client == 'gas':
        return "Glitch woke up"
    message = last_run_time
    return jsonify({"mes": message},{"time": last_run_time})

def my_cron_job():
    global last_run_time
    last_run_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

scheduler = BackgroundScheduler()
scheduler.start()
scheduler.add_job(
    func=my_cron_job,
    trigger="interval",
    minutes=2,
    id='my_cron_job_id',
    name='Print every 2 minutes',
    # replace_existing=True
)

atexit.register(lambda: scheduler.shutdown())

@app.route("/")
def hello():
    client = request.args.get('client')
    if client == 'gas':
        return "Glitch woke up"
    return jsonify({"msg":"hello deploy from flask glitch"})


@app.route("/hello")
def hello2():
  return "This is a test"

if __name__ == "__main__":
    app.run()





# # データの整形
# data1 = [{"ranking": 1, "title": "ノルウェイの森", "author": "村上春樹"},{"ranking": 2, "title": "海辺のカフカ", "author": "村上春樹"},{"ranking": 3, "title": "名探偵コナン", "author": "青山剛昌"}, {"ranking": 4, "title": "マジック快斗", "author": "青山剛昌"}]
# data2 = [{"ranking": 1, "title": "名探偵コナン", "author": "青山剛昌"}, {"ranking": 2, "title": "マジック快斗", "author": "青山剛昌"},{"ranking": "id", "title": "", "author": ""},{"ranking": "id" , "title": "", "author": ""}]


# # data1の並び替え
# sorted_data1 = sorted(data1, key=lambda x: x['ranking'], reverse=True)

# # data2の並び替え
# # "id"のrankingを持つ項目を最後に配置
# def ranking_key(item):
#     if item['ranking'] == 'id':
#         return float('inf')  # 無限大を返すことで、"id"を最後に配置
#     return item['ranking']

# sorted_data2 = sorted(data2, key=ranking_key, reverse=True)

# # 結果の表示
# print("Sorted data1:")
# for item in sorted_data1:
#     print(item)

# print("\nSorted data2:")
# for item in sorted_data2:
#     print(item)


# def rank1():
#   global i
#   i = 1
#   for data in sorted_data1:
#     data['score'] = i * 3
#     i += 1
#     yield data

# def rank2():
#   global i
#   i = 1
#   for data in sorted_data2:
#     data['score'] =  i
#     i += 1
#     yield data

# ranked_data1 = list(rank1())
# ranked_data2 = list(rank2())

# def is_valid_item(item):
#     return item["title"] != "" and item["author"] != "" and item["ranking"] != "id"

# def common_items():
#   for item1 in ranked_data1:
#     for item2 in ranked_data2:
#       if is_valid_item(item1) and is_valid_item(item2) and item1["title"] == item2["title"] and item1["author"] == item2["author"]:
#         item1["score"] = item1["score"] * 1 + item2["score"] * 1
#         yield item1

# common_items = list(common_items())


# print("共通の要素:")
# print(common_items)


# def not_in_common(item, other_data):
#     return not any(item["title"] == other_item["title"] and 
#                    item["author"] == other_item["author"] 
#                    for other_item in other_data if is_valid_item(other_item))

# unique_data1 = [item for item in data1 if is_valid_item(item) and not_in_common(item, data2)]
# unique_data2 = [item for item in data2 if is_valid_item(item) and not_in_common(item, data1)]

# print("\ndata1の固有の要素:")
# print(unique_data1)
# print("\ndata2の固有の要素:")
# print(unique_data2)

# final = common_items + unique_data1 + unique_data2
# sorted_final = sorted(final, key=lambda x: x['score'], reverse=True)
# print(sorted_final)










# sqlite3に保存
# data2 = []

# while len(data2) <= 100:
#     data2.append(("日本語で遊ぼう","日本昔話"))

# import sqlite3

# dbname = 'TEST.db'
# conn = sqlite3.connect(dbname)
# # sqliteを操作するカーソルオブジェクトを作成
# cur = conn.cursor()

# # personsというtableを作成してみる
# # 大文字部はSQL文。小文字でも問題ない。
# cur.execute(
#     '''CREATE TABLE IF NOT EXISTS persons10(id INTEGER PRIMARY KEY AUTOINCREMENT,
#      firstname STRING, secondname STRING)''')
# # # "name"に"Taro"を入れる
# data = [("田中", "稔"), ("山田", "祐介"), ("佐藤", "健"), ("高橋", "渉")]

# cur.executemany("INSERT INTO persons10 (firstname, secondname) VALUES (?,?)", data2)
# # cur.execute('INSERT INTO persons(name) values("Taro")')
# # # 同様に
# # cur.execute('INSERT INTO persons(name) values("Hanako")')
# # cur.execute('INSERT INTO persons(name) values("Hiroki")')

# # terminalで実行したSQL文と同じようにexecute()に書く
# cur.execute('SELECT * FROM persons10')

# # 中身を全て取得するfetchall()を使って、printする。
# #print(cur.fetchall())
# data_list = cur.fetchall()

# # データベースへコミット。これで変更が反映される。
# conn.commit()

# cur.close()

# conn.close()

# import os

# # 既存のコードの最後に以下を追加

# # データベースファイルのパス
# db_path = 'TEST.db'

# # ファイルサイズを取得（バイト単位）
# size_bytes = os.path.getsize(db_path)

# # バイトをキロバイトに変換
# size_kb = size_bytes / 1024

# print(f"データベースファイルのサイズ: {size_kb:.2f} KB", f"データベースの中身: {data_list}")

