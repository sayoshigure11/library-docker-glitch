# # # 完成

# # from booklog_ranking import search_booklog_ranking
# # from bookmeter_ranking import search_bookmeter_ranking
# # from bookoff_ranking import search_bookoff_ranking

# # # データの整形
# # data1 = [{"ranking": 1, "title": "ノルウェイの森", "author": "村上春樹"},{"ranking": 2, "title": "海辺のカフカ", "author": "村上春樹"},{"ranking": 3, "title": "名探偵コナン", "author": "青山剛昌"}, {"ranking": 4, "title": "マジック快斗", "author": "青山剛昌"}]
# # data2 = [{"ranking": 1, "title": "名探偵コナン", "author": "青山剛昌"}, {"ranking": 2, "title": "マジック快斗", "author": "青山剛昌"},{"ranking": "id", "title": "", "author": ""},{"ranking": "id" , "title": "", "author": ""}]
# # data3 = [{"ranking": 1, "title": "海辺のカフカ", "author": "村上春樹"}, {"ranking": 2, "title": "ノルウェイの森", "author": "村上春樹"}, {"ranking": 3, "title": "名探偵コナン", "author": "青山剛昌"}]

# # def ranking_key(item):
# #     if item['ranking'] == 'id':
# #         return float('inf')
# #     return item['ranking']

# # def is_valid_item(item):
# #     return item["title"] != "" and item["author"] != "" and item["ranking"] != "id"

# # sorted_data1 = sorted(data1, key=lambda x: x['ranking'])
# # sorted_data2 = sorted(data2, key=ranking_key)
# # sorted_data3 = sorted(data3, key=lambda x: x['ranking'])

# # def rank_data(data, weight):
# #     for i, item in enumerate(data, 1):
# #         if is_valid_item(item):
# #             item['score'] = (len(data) - i + 1) * weight
# #         else:
# #             item['score'] = 0
# #     return data

# # ranked_data1 = rank_data(sorted_data1, 3)
# # ranked_data2 = rank_data(sorted_data2, 2)
# # ranked_data3 = rank_data(sorted_data3, 1)

# # def merge_data(data1, data2, data3):
# #     merged = {}
# #     for dataset in [data1, data2, data3]:
# #         for item in dataset:
# #             if is_valid_item(item):
# #                 key = (item['title'], item['author'])
# #                 if key in merged:
# #                     merged[key]['score'] += item['score']
# #                 else:
# #                     merged[key] = item.copy()
# #     print(merged)
# #     return list(merged.values())

# # final = merge_data(ranked_data1, ranked_data2, ranked_data3)
# # sorted_final = sorted(final, key=lambda x: x['score'], reverse=True)

# # # 結果の表示
# # print("Final sorted data:")
# # for item in sorted_final:
# #     print(item)




# # 完成

# from booklog_ranking import search_booklog_ranking
# from bookmeter_ranking import search_bookmeter_ranking
# from bookoff_ranking import search_bookoff_ranking

# # データの整形
# data1 = [{"ranking": 1, "title": "ノルウェイの森", "author": "村上春樹"},{"ranking": 2, "title": "海辺のカフカ", "author": "村上春樹"},{"ranking": 3, "title": "名探偵コナン", "author": "青山剛昌"}, {"ranking": 4, "title": "マジック快斗", "author": "青山剛昌"}]
# data2 = [{"ranking": 1, "title": "名探偵コナン", "author": "青山剛昌"}, {"ranking": 2, "title": "マジック快斗", "author": "青山剛昌"},{"ranking": "id", "title": "", "author": ""},{"ranking": "id" , "title": "", "author": ""}]
# data3 = [{"ranking": 1, "title": "海辺のカフカ", "author": "村上春樹"}, {"ranking": 2, "title": "ノルウェイの森", "author": "村上春樹"}, {"ranking": 3, "title": "名探偵コナン", "author": "青山剛昌"}]


# def get_data():
#     booklog_ranking = list(search_booklog_ranking())
#     bookmeter_ranking = list(search_bookmeter_ranking())
#     # bookoff_ranking = list(search_bookoff_ranking())
#     bookoff_ranking = list(search_bookoff_ranking())[:20]

#     return {"booklog_ranking": booklog_ranking, "bookmeter_ranking": bookmeter_ranking, "bookoff_ranking": bookoff_ranking}

# def ranking_key(item):
#     if item['ranking'] == 'id':
#         return float('inf')
#     return item['ranking']

# def is_valid_item(item):
#     return item["title"] != "" and item["author"] != "" and item["ranking"] != "id"


# def rank_data(data, weight):
#     for i, item in enumerate(data, 1):
#         if is_valid_item(item):
#             item['score'] = (len(data) - i + 1) * weight
#         else:
#             item['score'] = 0
#     return data



# def merge_data():
#     data = get_data()
#     data1 = data["booklog_ranking"]
#     data2 = data["bookmeter_ranking"]
#     data3 = data["bookoff_ranking"]

#     sorted_data1 = sorted(data1, key=lambda x: x['ranking'])
#     sorted_data2 = sorted(data2, key=ranking_key)
#     sorted_data3 = sorted(data3, key=lambda x: x['ranking'])

#     ranked_data1 = rank_data(sorted_data1, 3)
#     ranked_data2 = rank_data(sorted_data2, 2)
#     ranked_data3 = rank_data(sorted_data3, 1)

#     merged = {}
#     for dataset in [ranked_data1, ranked_data2, ranked_data3]:
#         for item in dataset:
#             if is_valid_item(item):
#                 key = (item['title'], item['author'])
#                 if key in merged:
#                     merged[key]['score'] += item['score']
#                 else:
#                     merged[key] = item.copy()
#     print(merged)
#     final_data_kari = list(merged.values())
#     return sorted(final_data_kari, key=lambda x: x['score'], reverse=True)

# final = merge_data()
# # sorted_final = sorted(final, key=lambda x: x['score'], reverse=True)

# # 結果の表示
# print("Final sorted data:")
# for item in final:
#     print(item)




# # 自分で考えたやつ＋claude3　これはうまく機能しない・・・
# # # データの整形
# # data1 = [{"ranking": 1, "title": "ノルウェイの森", "author": "村上春樹"},{"ranking": 2, "title": "海辺のカフカ", "author": "村上春樹"},{"ranking": 3, "title": "名探偵コナン", "author": "青山剛昌"}, {"ranking": 4, "title": "マジック快斗", "author": "青山剛昌"}]
# # data2 = [{"ranking": 1, "title": "名探偵コナン", "author": "青山剛昌"}, {"ranking": 2, "title": "マジック快斗", "author": "青山剛昌"},{"ranking": "id", "title": "", "author": ""},{"ranking": "id" , "title": "", "author": ""}]
# # data3 = [{"ranking": 1, "title": "海辺のカフカ", "author": "村上春樹"}, {"ranking": 2, "title": "ノルウェイの森", "author": "村上春樹"}, {"ranking": 3, "title": "名探偵コナン", "author": "青山剛昌"}]

# # # data1 = list(search_booklog_ranking())
# # # data2 = list(search_bookmeter_ranking())
# # # data3 = list(search_third_source_ranking())  # 新しいデータソースの関数を追加

# # # データの並び替え
# # def ranking_key(item):
# #     if item['ranking'] == 'id':
# #         return float('inf')
# #     return item['ranking']

# # def is_valid_item(item):
# #     return item["title"] != "" and item["author"] != "" and item["ranking"] != "id"

# # sorted_data1 = sorted(data1, key=lambda x: x['ranking'], reverse=True)
# # sorted_data2 = sorted(data2, key=ranking_key, reverse=True)
# # sorted_data3 = sorted(data3, key=lambda x: x['ranking'], reverse=True)

# # # スコアの計算
# # def rank_data(data, weight):
# #     i = 1
# #     for item in data:
# #         if is_valid_item(item):
# #             item['score'] = i * weight
# #             i += 1
# #         else:
# #             item['score'] = 0
# #         yield item

# # ranked_data1 = list(rank_data(sorted_data1, 3))
# # ranked_data2 = list(rank_data(sorted_data2, 2))
# # ranked_data3 = list(rank_data(sorted_data3, 1))



# # def common_items():
# #     for item1 in ranked_data1:
# #         for item2 in ranked_data2:
# #             for item3 in ranked_data3:
# #                 if (is_valid_item(item1) and is_valid_item(item2) and is_valid_item(item3) and
# #                     item1["title"] == item2["title"] == item3["title"] and
# #                     item1["author"] == item2["author"] == item3["author"]):
# #                     item1["score"] = item1["score"] + item2["score"] + item3["score"]
# #                     yield item1
# #                 # elif (is_valid_item(item1) and is_valid_item(item2) and
# #                 #       item1["title"] == item2["title"] and item1["author"] == item2["author"]):
# #                 #     item1["score"] = item1["score"] + item2["score"]
# #                 #     yield item1
# #                 # elif (is_valid_item(item1) and is_valid_item(item3) and
# #                 #       item1["title"] == item3["title"] and item1["author"] == item3["author"]):
# #                 #     item1["score"] = item1["score"] + item3["score"]
# #                 #     yield item1

# # common_items = list(common_items())

# # #print(common_items)

# # def not_in_common(item, other_data1, other_data2):
# #     return not any(item["title"] == other_item["title"] and 
# #                    item["author"] == other_item["author"] 
# #                    for other_item in other_data1 + other_data2 if is_valid_item(other_item))

# # unique_data1 = [item for item in data1 if is_valid_item(item) and not_in_common(item, data2, data3)]
# # unique_data2 = [item for item in data2 if is_valid_item(item) and not_in_common(item, data1, data3)]
# # unique_data3 = [item for item in data3 if is_valid_item(item) and not_in_common(item, data1, data2)]


# # print(unique_data1)
# # print(unique_data2)
# # print(unique_data3)

# # final = common_items + unique_data1 + unique_data2 + unique_data3
# # sorted_final = sorted(final, key=lambda x: x['score'], reverse=True)

# # # 結果の表示
# # # print("Final sorted data:")
# # # print(sorted_final)
# # # for item in sorted_final:
# # #     print(item)









# 本コードのコピー
# from booklog_ranking import search_booklog_ranking
# from bookmeter_ranking import search_bookmeter_ranking
# from bookoff_ranking import search_bookoff_ranking

# # データの整形
# data1 = [{"ranking": 1, "title": "ノルウェイの森", "author": "村上春樹"},{"ranking": 2, "title": "海辺のカフカ", "author": "村上春樹"},{"ranking": 3, "title": "名探偵コナン", "author": "青山剛昌"}, {"ranking": 4, "title": "マジック快斗", "author": "青山剛昌"}]
# data2 = [{"ranking": 1, "title": "名探偵コナン", "author": "青山剛昌"}, {"ranking": 2, "title": "マジック快斗", "author": "青山剛昌"},{"ranking": "id", "title": "", "author": ""},{"ranking": "id" , "title": "", "author": ""}]
# data3 = [{"ranking": 1, "title": "海辺のカフカ", "author": "村上春樹"}, {"ranking": 2, "title": "ノルウェイの森", "author": "村上春樹"}, {"ranking": 3, "title": "名探偵コナン", "author": "青山剛昌"}]

# def ranking_key(item):
#     if item['ranking'] == 'id':
#         return float('inf')
#     return item['ranking']

# def is_valid_item(item):
#     return item["title"] != "" and item["author"] != "" and item["ranking"] != "id"

# sorted_data1 = sorted(data1, key=lambda x: x['ranking'])
# sorted_data2 = sorted(data2, key=ranking_key)
# sorted_data3 = sorted(data3, key=lambda x: x['ranking'])

# def rank_data(data, weight):
#     for i, item in enumerate(data, 1):
#         if is_valid_item(item):
#             item['score'] = (len(data) - i + 1) * weight
#         else:
#             item['score'] = 0
#     return data

# ranked_data1 = rank_data(sorted_data1, 3)
# ranked_data2 = rank_data(sorted_data2, 2)
# ranked_data3 = rank_data(sorted_data3, 1)

# def merge_data(data1, data2, data3):
#     merged = {}
#     for dataset in [data1, data2, data3]:
#         for item in dataset:
#             if is_valid_item(item):
#                 key = (item['title'], item['author'])
#                 if key in merged:
#                     merged[key]['score'] += item['score']
#                 else:
#                     merged[key] = item.copy()
#     print(merged)
#     return list(merged.values())

# final = merge_data(ranked_data1, ranked_data2, ranked_data3)
# sorted_final = sorted(final, key=lambda x: x['score'], reverse=True)

# # 結果の表示
# print("Final sorted data:")
# for item in sorted_final:
#     print(item)




# 完成
from .booklog_ranking import search_booklog_ranking
from .bookmeter_ranking import search_bookmeter_ranking
from .bookoff_ranking import search_bookoff_ranking

# データの整形
data1 = [{"ranking": 1, "title": "ノルウェイの森", "author": "村上春樹"},{"ranking": 2, "title": "海辺のカフカ", "author": "村上春樹"},{"ranking": 3, "title": "名探偵コナン", "author": "青山剛昌"}, {"ranking": 4, "title": "マジック快斗", "author": "青山剛昌"}]
data2 = [{"ranking": 1, "title": "名探偵コナン", "author": "青山剛昌"}, {"ranking": 2, "title": "マジック快斗", "author": "青山剛昌"},{"ranking": "id", "title": "", "author": ""},{"ranking": "id" , "title": "", "author": ""}]
data3 = [{"ranking": 1, "title": "海辺のカフカ", "author": "村上春樹"}, {"ranking": 2, "title": "ノルウェイの森", "author": "村上春樹"}, {"ranking": 3, "title": "名探偵コナン", "author": "青山剛昌"}]


def get_data():
    booklog_ranking = list(search_booklog_ranking())
    bookmeter_ranking = list(search_bookmeter_ranking())
    bookoff_ranking = list(search_bookoff_ranking())[:20]

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



def merge_data():
    data = get_data()
    data1 = data["booklog_ranking"]
    data2 = data["bookmeter_ranking"]
    data3 = data["bookoff_ranking"]
    
    sorted_data1 = sorted(data1, key=lambda x: x['ranking'])
    sorted_data2 = sorted(data2, key=ranking_key)
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
    print(merged)
    final_data_kari = list(merged.values())
    return sorted(final_data_kari, key=lambda x: x['score'], reverse=True)