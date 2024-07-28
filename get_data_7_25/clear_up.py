# 完成
import asyncio

# # python3 -m clear_up用　shuna@LAPTOP-VHG04PF2:~/next-jikken/library-docker-glitch/get_data_7_25
# from booklog.booklog_ranking import search_booklog_ranking
# from bookmeter.bookmeter_ranking import search_bookmeter_ranking
# from bookoff.bookoff_ranking import search_bookoff_ranking

# python3 kari_flask.py用　shuna@LAPTOP-VHG04PF2:~/next-jikken/library-docker-glitch
# 実行するファイルでは相対パスが使えないらしい・・・
from .booklog.booklog_ranking import search_booklog_ranking
from .bookmeter.bookmeter_ranking import search_bookmeter_ranking
from .bookoff.bookoff_ranking import search_bookoff_ranking

# データの整形
data1 = [{"ranking": 1, "title": "ノルウェイの森", "author": "村上春樹"},{"ranking": 2, "title": "海辺のカフカ", "author": "村上春樹"},{"ranking": 3, "title": "名探偵コナン", "author": "青山剛昌"}, {"ranking": 4, "title": "マジック快斗", "author": "青山剛昌"}]
data2 = [{"ranking": 1, "title": "名探偵コナン", "author": "青山剛昌"}, {"ranking": 2, "title": "マジック快斗", "author": "青山剛昌"},{"ranking": "id", "title": "", "author": ""},{"ranking": "id" , "title": "", "author": ""}]
data3 = [{"ranking": 1, "title": "海辺のカフカ", "author": "村上春樹"}, {"ranking": 2, "title": "ノルウェイの森", "author": "村上春樹"}, {"ranking": 3, "title": "名探偵コナン", "author": "青山剛昌"}]


async def get_data():
    # booklog_ranking_data = list(search_booklog_ranking())
    # bookmeter_ranking_data = list(search_bookmeter_ranking())
    # bookoff_ranking_data = list(search_bookoff_ranking())[:20]
    
    
    # booklog_ranking_data = search_booklog_ranking()
    # bookmeter_ranking_data = search_bookmeter_ranking()
    # bookoff_ranking_data = search_bookoff_ranking()

    async def collect_data(search_func, limit=None):
        data = []
        async for item in search_func:
            data.append(item)
            if limit and len(data) >= limit:
                break
        return data

    booklog_ranking_data = collect_data(search_booklog_ranking())
    bookmeter_ranking_data = collect_data(search_bookmeter_ranking())
    bookoff_ranking_data = collect_data(search_bookoff_ranking(), limit=20)

    
    results = await asyncio.gather(
        bookoff_ranking_data,
        bookmeter_ranking_data,
        booklog_ranking_data
    )

    bookoff_ranking, bookmeter_ranking, booklog_ranking = results

    bookoff_ranking = bookoff_ranking[:20]

    #print("booklog_ranking",booklog_ranking)
    #print("bookmeter_ranking", bookmeter_ranking)
    #print("bookoff_ranking", bookoff_ranking)

    return {"booklog_ranking": booklog_ranking, "bookmeter_ranking": bookmeter_ranking, "bookoff_ranking": bookoff_ranking}

def ranking_key(item):
    if item['ranking'] == 'id':
        return float('inf')
    return item['ranking']

def is_valid_item(item):
    return item["title"] != "" and item["author"] != "" and item["ranking"] != "id"


def rank_data(data, weight):
    for i, item in enumerate(data, 1):
        if is_valid_item(item):
            item['score'] = (len(data) - i + 1) * weight
        else:
            item['score'] = 0
    return data



async def merge_data():
    data = await get_data()
    data1 = data["booklog_ranking"]
    data2 = data["bookmeter_ranking"]
    data3 = data["bookoff_ranking"]
    
    sorted_data1 = sorted(data1, key=lambda x: x['ranking'])
    # sorted_data2 = sorted(data2, key=ranking_key)
    sorted_data2 = sorted(data2, key=lambda x: x['ranking'])
    sorted_data3 = sorted(data3, key=lambda x: x['ranking'])

    ranked_data1 = rank_data(sorted_data1, 3)
    ranked_data2 = rank_data(sorted_data2, 2)
    ranked_data3 = rank_data(sorted_data3, 1)

    merged = {}
    for dataset in [ranked_data1, ranked_data2, ranked_data3]:
        for item in dataset:
            if is_valid_item(item):
                key = (item['title'], item['author'])
                if key in merged:
                    merged[key]['score'] += item['score']
                else:
                    merged[key] = item.copy()
    #print("merged",merged)
    final_data_kari = list(merged.values())

    # 追加　ランキングを更新
    for index, item in enumerate(final_data_kari):
        item['ranking'] = index + 1

    return sorted(final_data_kari, key=lambda x: x['score'], reverse=True)



async def main():
    clear_data = await merge_data()
    for index, item in enumerate(clear_data):
        item['ranking'] = index + 1
    # print("clear_data",clear_data)


# VScode用の実行部分
if __name__ == "__main__":
    asyncio.run(main())