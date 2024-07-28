# # ブックオフランキング
# import requests
# from bs4 import BeautifulSoup as bs
# import urllib.parse as up
# import re


# HOST="shopping.bookoff.co.jp"
# URL="https://"+HOST
# SEARCH_URL=URL+"/list/ranking.html"


# HEADERS={ "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}


# #取ってくるページ
# #https://shopping.bookoff.co.jp/list/ranking.html?genre=12


# class SearchType:
#   BOOK=12
#   NOVEL=1201



# # 取得したデータから価格のみを抽出
# def clean_price(price_str):
#     match = re.search(r'(\d+)円', price_str)
#     if match:
#         return int(match.group(1))
#     return None



# def _search(type_=SearchType.BOOK,session=requests):
#     params={
#         "genre" : type_
#     }
#     res=session.get(SEARCH_URL,headers=HEADERS, params=params)
#     res.encoding='utf-8'
#     return res.text


# def toData(l):
#   productItem=l

#   productUrl=URL + productItem.find("a").get("href")
#   print(productUrl)


#   productImage=productItem.find("a").find("img").get("src")
#   print(productImage)


#   productDetail1=productItem.select_one(".productItem__detail")
#   productDetail=productDetail1.find("a")


#   productRanking=productDetail.find("span").find("strong").text + "位"
#   print(productRanking)


#   productTitle=productDetail.select_one(".productItem__title").text
#   print(productTitle)
#   productAuthor=productDetail.select_one(".productItem__author").text
#   print(productAuthor)
#   productPrice=clean_price(productItem.select_one(".productItem__price").text)
#   print(productPrice)


#   stocked=productDetail1.select_one(".productItem__btns").find("a").text


#   if stocked=="入荷お知らせ":
#     productStocked=False
#   else:
#     productStocked=True
#   print(productStocked)


#   # return {
#   #   "ranking":productRanking,
# 	# 	"title":productTitle,
# 	# 	"url":productUrl,
# 	# 	"author":productAuthor,
# 	# 	"price":productPrice,
# 	# 	"stocked":productStocked,
#   #   "image":productImage
# 	# }

#   return {
#     "ranking":productRanking,
# 		"title":productTitle,
# 		# "url":productUrl,
# 		"author":productAuthor,
# 		# "price":productPrice,
# 		# "stocked":productStocked,
#     "image":productImage
# 	}



# def getData(soup):
#   for l in soup.select(".productItem__inner"):
#     yield toData(l)
# def search(type_=SearchType.BOOK,session=requests):
#   text=_search(type_,session)
#   soup=bs(text,"html.parser")
#   for data in getData(soup):
#     data["url"]=up.urljoin(SEARCH_URL,data["url"])
#     print(data)
#     yield data



# # results = [data for data in search()]


# # # Notebookのセルに出力
# # results









# # ブックオフの個別商品ページのスクレイピング
# # import requests
# # from bs4 import BeautifulSoup as bs
# # import urllib.parse as up
# # import time
# # from functools import wraps
# # from flask import Blueprint, request, jsonify
# # import json
# # import re



# # last_request_time = 0
# # MIN_REQUEST_INTERVAL = 2

# # HOST="shopping.bookoff.co.jp"
# # URL="https://"+HOST
# # SEARCH_URL=URL+"/search/genre/"

# # def rate_limit(f):
# #     @wraps(f)
# #     def wrapper(*args, **kwargs):
# #         global last_request_time
# #         elapsed = time.time() - last_request_time
# #         left_to_wait = MIN_REQUEST_INTERVAL - elapsed


# #         if left_to_wait > 0:
# #             time.sleep(left_to_wait)
        
# #         ret = f(*args, **kwargs)
# #         last_request_time = time.time()
# #         return ret
# #     return wrapper


# # HEADERS={ "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}
# # ENCODING="sjis"

# # class SearchType:
# #     ALL=""
# #     BOOK="12/"
# #     PRATICAL_BOOK=1201
# #     MAGAZINE="13"
# #     CD=31
# #     DVD=71
# #     GAME=51
# #     ELSE=81
# #     SET="set"


# # # 取得したデータから価格のみを抽出
# # def clean_price(price_str):
# #     match = re.search(r'(\d+)円', price_str)
# #     if match:
# #         return int(match.group(1))
# #     return None


# # # 新しいVersion
# # @rate_limit
# # def _search(query,page=1,type_=SearchType.BOOK,session=requests):
# #     query="keyword/" + query
# #     params={
# #         "p" :page
# #     }
# #     res=session.get(SEARCH_URL + type_ + query,headers=HEADERS, params=params)
# #     res.encoding='utf-8'
# #     return res.text



# # def toData(l):
# #     #productItem=l.select_one(".productItem__inner")
# #     productItem=l

# #     productUrl=URL + productItem.find("a").get("href")
# #     print(productUrl)

# #     productImage=productItem.find("a").find("img").get("src")
# #     print(productImage)

# #     productDetail1=productItem.select_one(".productItem__detail")
# #     productDetail=productDetail1.find("a")

# #     productTitle=productDetail.select_one(".productItem__title").text
# #     print(productTitle)
# #     productAuthor=productDetail.select_one(".productItem__author").text
# #     print(productAuthor)
# #     # productPrice=productItem.select_one(".productItem__price").text
# #     # print(productPrice)
# #     productPrice=clean_price(productItem.select_one(".productItem__price").text)
# #     print(productPrice)

# #     productStocked=productItem.select_one(".productItem__stock").select_one("span").text
# #     print(productStocked)

# #     return {
# #         "title":productTitle,
# #         "url":productUrl,
# #         "author":productAuthor,
# #         "price":productPrice,
# #         "stocked":productStocked,
# #         "image":productImage
# #     }


# # @rate_limit
# # def getData(soup):
# #     for l in soup.select(".productItem__inner"):
# #         yield toData(l)


# # @rate_limit
# # def search(query,page,type_=SearchType.BOOK,session=requests):
# #     text=_search(query,str(page),type_,session)
# #     soup=bs(text,"html.parser")
# #     for data in getData(soup):
# #         data["url"]=up.urljoin(SEARCH_URL,data["url"])
# #         print(data)
# #         yield data




# # # query = "ノルウェイの森"
# # # results = [data for data in search(query)]


# # bookoff_detail_bp = Blueprint('bookoff_detail', __name__)


# # @bookoff_detail_bp.route("/bookdetail/<isbn>", methods=['GET'])
# # def bookoff_detail(isbn):
# #     print(f"Request method: {request.method}")
# #     print(f"Request headers: {request.headers}")
# #     print(f"Request args: {request.args}")
# #     try:
# #         page = request.args.get("page", 1, type=int)
# #         data = list(search(isbn, page))
# #         return json.dumps(data, ensure_ascii=False, indent=4), 200, {'Content-Type': 'application/json'}
# #     except Exception as e:
# #         print(f"Error occurred: {str(e)}")
# #         return jsonify({"error": str(e)}), 500






# # 本コードのコピー
# # ブックオフランキング
# import requests
# from bs4 import BeautifulSoup
# import urllib.parse as up
# import re


# HOST="shopping.bookoff.co.jp"
# URL="https://"+HOST
# SEARCH_URL=URL+"/list/ranking.html"


# HEADERS={ "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}


# #取ってくるページ
# #https://shopping.bookoff.co.jp/list/ranking.html?genre=12


# class SearchType:
#   BOOK=12
#   NOVEL=1201



# # 取得したデータから価格のみを抽出
# def clean_price(price_str):
#     match = re.search(r'(\d+)円', price_str)
#     if match:
#         return int(match.group(1))
#     return None



# def _search(type_=SearchType.BOOK,session=requests):
#     params={
#         "genre" : type_
#     }
#     res=session.get(SEARCH_URL,headers=HEADERS, params=params)
#     res.encoding='utf-8'
#     return res.text


# def toData(l):
#   productItem=l

#   productUrl=URL + productItem.find("a").get("href")


#   productImage=productItem.find("a").find("img").get("src")


#   productDetail1=productItem.select_one(".productItem__detail")
#   productDetail=productDetail1.find("a")


#   productRanking=productDetail.find("span").find("strong").text


#   productTitle=productDetail.select_one(".productItem__title").text
#   productAuthor=productDetail.select_one(".productItem__author").text
#   productPrice=clean_price(productItem.select_one(".productItem__price").text)


#   stocked=productDetail1.select_one(".productItem__btns").find("a").text


#   if stocked=="入荷お知らせ":
#     productStocked=False
#   else:
#     productStocked=True


# 	# return {
# 	# "ranking":productRanking,
# 	# 	"title":productTitle,
# 	# 	"url":productUrl,
# 	# 	"author":productAuthor,
# 	# 	"price":productPrice,
# 	# 	"stocked":productStocked,
# 	# "image":productImage
# 	# }
  
#   return {
#     "ranking":int(productRanking),
# 		"title":productTitle,
# 		# "url":productUrl,
# 		"author":productAuthor,
# 		# "price":productPrice,
# 		# "stocked":productStocked,
#     "image":productImage
# 	}



# def getData(soup):
#   for l in soup.select(".productItem__inner"):
#     yield toData(l)
# def search_bookoff_ranking(type_=SearchType.BOOK,session=requests):
#   text=_search(type_,session)
#   soup=bs(text,"html.parser")
#   for data in getData(soup):
#     # data["url"]=up.urljoin(SEARCH_URL,data["url"])
#     yield data










# # 本コードのコピー
# # ブックオフランキング
# import requests
# from bs4 import BeautifulSoup as bs
# import urllib.parse as up
# import re


# HOST="shopping.bookoff.co.jp"
# URL="https://"+HOST
# SEARCH_URL=URL+"/list/ranking.html"


# HEADERS={ "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}


# #取ってくるページ
# #https://shopping.bookoff.co.jp/list/ranking.html?genre=12


# class SearchType:
#   BOOK=12
#   NOVEL=1201



# # 取得したデータから価格のみを抽出
# def clean_price(price_str):
#     match = re.search(r'(\d+)円', price_str)
#     if match:
#         return int(match.group(1))
#     return None



# def _search(type_=SearchType.BOOK,session=requests):
#     params={
#         "genre" : type_
#     }
#     res=session.get(SEARCH_URL,headers=HEADERS, params=params)
#     res.encoding='utf-8'
#     return res.text


# def toData(l):
#   productItem=l

#   productUrl=URL + productItem.find("a").get("href")


#   productImage=productItem.find("a").find("img").get("src")


#   productDetail1=productItem.select_one(".productItem__detail")
#   productDetail=productDetail1.find("a")


#   productRanking=productDetail.find("span").find("strong").text


#   productTitle=productDetail.select_one(".productItem__title").text
#   productAuthor=productDetail.select_one(".productItem__author").text
#   productPrice=clean_price(productItem.select_one(".productItem__price").text)


#   stocked=productDetail1.select_one(".productItem__btns").find("a").text


#   if stocked=="入荷お知らせ":
#     productStocked=False
#   else:
#     productStocked=True

#   return {
#     "ranking":int(productRanking),
# 		"title":productTitle,
# 		# "url":productUrl,
# 		"author":productAuthor,
# 		# "price":productPrice,
# 		# "stocked":productStocked,
#     "image":productImage
# 	}



# def getData(soup):
#   for l in soup.select(".productItem__inner"):
#     yield toData(l)
# def search_bookoff_ranking(type_=SearchType.BOOK,session=requests):
#   text=_search(type_,session)
#   soup=bs(text,"html.parser")
#   for data in getData(soup):
#     # data["url"]=up.urljoin(SEARCH_URL,data["url"])
#     yield data











# 2024/07/19/試す前用保存
# 本コードのコピー
# ブックオフランキング
import requests
from bs4 import BeautifulSoup as bs
import urllib.parse as up
import re

from .rakuten_api import fetch_rakuten, run_async

HOST="shopping.bookoff.co.jp"
URL="https://"+HOST
SEARCH_URL=URL+"/list/ranking.html"


HEADERS={ "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}


#取ってくるページ
#https://shopping.bookoff.co.jp/list/ranking.html?genre=12


class SearchType:
  BOOK=12
  NOVEL=1201


# rakuten_apiからデータを取得する関数
def get_book_info(title, author):
    book_data = run_async(fetch_rakuten(title, author))
    if book_data:
        # print("データを取得しました:", book_data)
        return book_data
    else:
        print("データの取得に失敗しました。")
        return None


# 取得したデータから価格のみを抽出
def clean_price(price_str):
    match = re.search(r'(\d+)円', price_str)
    if match:
        return int(match.group(1))
    return None



def _search(type_=SearchType.BOOK,session=requests):
    params={
        "genre" : type_
    }
    res=session.get(SEARCH_URL,headers=HEADERS, params=params)
    res.encoding='utf-8'
    return res.text


def toData(l):
  productItem=l

  productUrl=URL + productItem.find("a").get("href")


  productImage=productItem.find("a").find("img").get("src")


  productDetail1=productItem.select_one(".productItem__detail")
  productDetail=productDetail1.find("a")


  productRanking=productDetail.find("span").find("strong").text


  productTitle=productDetail.select_one(".productItem__title").text
  productAuthor=productDetail.select_one(".productItem__author").text
  productPrice=clean_price(productItem.select_one(".productItem__price").text)


  stocked=productDetail1.select_one(".productItem__btns").find("a").text

  # rakuten_apiからデータを取得
  title=productTitle
  author=productAuthor
  book_info = get_book_info(title, author)
  
  productIsbn = book_info['isbn']
  productPrice = book_info['itemPrice']
  productCaption = book_info['itemCaption']
  productPublisher = book_info['publisherName']
  productSalesDate = book_info['salesDate']


  if stocked=="入荷お知らせ":
    productStocked=False
  else:
    productStocked=True

  return {
    "ranking":int(productRanking),
		"title":productTitle,
		# "url":productUrl,
		"author":productAuthor,
		# "price":productPrice,
		# "stocked":productStocked,
    "image":productImage
	}



def getData(soup):
  for l in soup.select(".productItem__inner"):
    yield toData(l)
def search_bookoff_ranking(type_=SearchType.BOOK,session=requests):
  text=_search(type_,session)
  soup=bs(text,"html.parser")
  for data in getData(soup):
    # data["url"]=up.urljoin(SEARCH_URL,data["url"])
    yield data