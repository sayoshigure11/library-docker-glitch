# # ブックメーターのランキング
# import requests
# from bs4 import BeautifulSoup as bs
# import urllib.parse as up
# import re
# import time


# import json
# import sys
# import datetime






# HOST="bookmeter.com"
# URL="https://"+HOST
# BASE_URL=URL+"/rankings/monthly"

# BASE_URL2=URL+"/rankings/latest/wish_book"


# HEADERS={ "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}




# class SearchType:
#   bunko="bunko"
#   tankoubon="tankoubon"
#   comic="comic"
#   light_novel= "light_novel"
#   others="others"


# today=datetime.date.today()




# year=today.year
# month=today.month - 1
# if month == 0:
#   year -= 1
#   month = 12




# def _search(type_=SearchType.tankoubon,session=requests):
#     SEARCH_URL=BASE_URL + "/" + type_ + "/" + str(year) + "/" + str(month)
#     SEARCH_URL2=BASE_URL + "/" + type_ + "/" + "week"
#     res=session.get(SEARCH_URL,headers=HEADERS)
#     res=session.get(SEARCH_URL2,headers=HEADERS)
#     res.encoding='utf-8'
#     return res.text




# def toData(l):
#   productRanking=l.select_one(".book__ranking").find("span").text
#   print(productRanking)


#   productImage=l.select_one(".book__cover").find("a").find("img").get("src")
#   print(productImage)




#   productUrl=URL + l.select_one(".book__cover").find("a").get("href")
#   print(productUrl)


 
#   productDetail=l.select_one(".book__detail")




#   productTitle=productDetail.select_one(".detail__title").find("a").text
#   print(productTitle)
#   productAuthor=productDetail.select_one(".detail__authors").find("li").find("a").text
#   print(productAuthor)


#   productEvaluation=productDetail.select_one(".detail__options").find("dd").text




#   # return {
#   #   "ranking":productRanking,
# 	# 	"title":productTitle,
# 	# 	"url":productUrl,
# 	# 	"author":productAuthor,
# 	# 	"evaluation":productEvaluation,
#   #   "image":productImage
# 	# }

#   return {
#     "ranking":productRanking,
# 		"title":productTitle,
# 		# "url":productUrl,
# 		"author":productAuthor,
# 		# "evaluation":productEvaluation,
#     "image":productImage
# 	}








# def getData(soup):
#   for l in soup.select(".list__book"):
#     yield toData(l)
# def search(type_=SearchType.tankoubon,session=requests):
#   text=_search(type_,session)
#   soup=bs(text,"html.parser")
#   for data in getData(soup):
#     SEARCH_URL=BASE_URL + "/" + type_ + "/" + str(year) + "/" + str(month)
#     SEARCH_URL2=BASE_URL + "/" + type_ + "/" + "week"
#     data["url"]=up.urljoin(SEARCH_URL,data["url"])
#     data["url"]=up.urljoin(SEARCH_URL2,data["url"])
#     print(data)
#     yield data




# # results = [data for data in search()]


# # # Notebookのセルに出力
# # results








# # 本コードのコピー
# # ブックメーターのランキング
# import requests
# from bs4 import BeautifulSoup
# import urllib.parse as up
# import datetime



# HOST="bookmeter.com"
# URL="https://"+HOST
# # BASE_URL=URL+"/rankings/monthly"

# BASE_URL2=URL+"/rankings/latest/wish_book"


# HEADERS={ "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}



# class SearchType:
#   bunko="bunko"
#   tankoubon="tankoubon"
#   comic="comic"
#   light_novel= "light_novel"
#   others="others"


# today=datetime.date.today()



# year=today.year
# month=today.month - 1
# if month == 0:
#   year -= 1
#   month = 12




# def _search(type_=SearchType.tankoubon,session=requests):
#     # SEARCH_URL=BASE_URL + "/" + type_ + "/" + str(year) + "/" + str(month)
#     SEARCH_URL2=BASE_URL + "/" + type_ + "/" + "week"
#     # res=session.get(SEARCH_URL,headers=HEADERS)
#     res=session.get(SEARCH_URL2,headers=HEADERS)
#     res.encoding='utf-8'
#     return res.text



# def toData(l):
#   productRanking=l.select_one(".book__ranking").find("span").text


#   productImage=l.select_one(".book__cover").find("a").find("img").get("src")


#   productUrl=URL + l.select_one(".book__cover").find("a").get("href")


#   productDetail=l.select_one(".book__detail")


#   productTitle=productDetail.select_one(".detail__title").find("a").text
#   productAuthor=productDetail.select_one(".detail__authors").find("li").find("a").text


#   productEvaluation=productDetail.select_one(".detail__options").find("dd").text


# 	# return {
# 	# "ranking":productRanking,
# 	# 	"title":productTitle,
# 	# 	"url":productUrl,
# 	# 	"author":productAuthor,
# 	# 	"evaluation":productEvaluation,
# 	# "image":productImage
# 	# }
  
#   return {
#     "ranking":productRanking,
# 		"title":productTitle,
# 		# "url":productUrl,
# 		"author":productAuthor,
# 		# "evaluation":productEvaluation,
#     "image":productImage
# 	}

  

# def getData(soup):
#   for l in soup.select(".list__book"):
#     yield toData(l)
# def search_bookmeter_ranking(type_=SearchType.tankoubon,session=requests):
#   text=_search(type_,session)
#   soup=bs(text,"html.parser")
#   for data in getData(soup):
#     # SEARCH_URL=BASE_URL + "/" + type_ + "/" + str(year) + "/" + str(month)
#     SEARCH_URL2=BASE_URL + "/" + type_ + "/" + "week"
#     # data["url"]=up.urljoin(SEARCH_URL,data["url"])
#     # data["url"]=up.urljoin(SEARCH_URL2,data["url"])
#     yield data







# from typing import Pattern
# # 本コードのコピー
# # ブックメーターのランキング
# import requests
# from bs4 import BeautifulSoup
# import urllib.parse as up
# import datetime



# HOST="bookmeter.com"
# URL="https://"+HOST
# # BASE_URL=URL+"/rankings/monthly"

# BASE_URL2=URL+"/rankings/latest/wish_book"


# HEADERS={ "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}



# class SearchType:
#   bunko="bunko"
#   tankoubon="tankoubon"
#   comic="comic"
#   light_novel= "light_novel"
#   others="others"


# today=datetime.date.today()



# year=today.year
# month=today.month - 1
# if month == 0:
#   year -= 1
#   month = 12


# def extract_rank(text):
#     pattern = r"(\d+)位"
#     match = re.search(pattern, text)
#     if match:
#         return match.group(1)
#     else:
#         return None



# def extract_author(text):
#     pattern1 = r"\u3000"
#     pattern2 = r" "
#     match1 = re.search(pattern1, text)
#     match2 = re.search(pattern2, text)
#     if match1:
#         return re.sub(r"[\u3000]", "", text)
#     elif match2:
#         return re.sub(r"[ ]", "", text)
#     else:
#         return text


# def _search(type_=SearchType.tankoubon,session=requests):
#     # SEARCH_URL=BASE_URL + "/" + type_ + "/" + str(year) + "/" + str(month)
#     SEARCH_URL2=BASE_URL2 + "/" + type_ + "/" + "week"
#     # res=session.get(SEARCH_URL,headers=HEADERS)
#     res=session.get(SEARCH_URL2,headers=HEADERS)
#     res.encoding='utf-8'
#     return res.text



# def toData(l):
#   productRanking=l.select_one(".book__ranking").find("span").text


#   productImage=l.select_one(".book__cover").find("a").find("img").get("src")


#   productUrl=URL + l.select_one(".book__cover").find("a").get("href")


#   productDetail=l.select_one(".book__detail")


#   productTitle=productDetail.select_one(".detail__title").find("a").text
#   productAuthor=productDetail.select_one(".detail__authors").find("li").find("a").text


#   productEvaluation=productDetail.select_one(".detail__options").find("dd").text


# 	# return {
# 	# "ranking":productRanking,
# 	# 	"title":productTitle,
# 	# 	"url":productUrl,
# 	# 	"author":productAuthor,
# 	# 	"evaluation":productEvaluation,
# 	# "image":productImage
# 	# }
  
#   return {
#     "ranking":int(extract_rank(productRanking)),
# 		"title":productTitle,
# 		# "url":productUrl,
# 		"author":extract_author(productAuthor),
# 		# "evaluation":productEvaluation,
#     "image":productImage
# 	}

  

# def getData(soup):
#   for l in soup.select(".list__book"):
#     yield toData(l)
# def search_bookmeter_ranking(type_=SearchType.tankoubon,session=requests):
#   text=_search(type_,session)
#   soup=bs(text,"html.parser")
#   for data in getData(soup):
#     # SEARCH_URL=BASE_URL + "/" + type_ + "/" + str(year) + "/" + str(month)
#     SEARCH_URL2=BASE_URL2 + "/" + type_ + "/" + "week"
#     # data["url"]=up.urljoin(SEARCH_URL,data["url"])
#     # data["url"]=up.urljoin(SEARCH_URL2,data["url"])
#     yield data










# from typing import Pattern
# # 本コードのコピー
# # ブックメーターのランキング
# import requests
# from bs4 import BeautifulSoup as bs
# import urllib.parse as up
# import datetime



# HOST="bookmeter.com"
# URL="https://"+HOST
# # BASE_URL=URL+"/rankings/monthly"

# BASE_URL2=URL+"/rankings/latest/wish_book"


# HEADERS={ "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}



# class SearchType:
#   bunko="bunko"
#   tankoubon="tankoubon"
#   comic="comic"
#   light_novel= "light_novel"
#   others="others"


# today=datetime.date.today()



# year=today.year
# month=today.month - 1
# if month == 0:
#   year -= 1
#   month = 12


# def extract_rank(text):
#     pattern = r"(\d+)位"
#     match = re.search(pattern, text)
#     if match:
#         return match.group(1)
#     else:
#         return None



# def extract_author(text):
#     pattern1 = r"\u3000"
#     pattern2 = r" "
#     match1 = re.search(pattern1, text)
#     match2 = re.search(pattern2, text)
#     if match1:
#         return re.sub(r"[\u3000]", "", text)
#     elif match2:
#         return re.sub(r"[ ]", "", text)
#     else:
#         return text


# def _search(type_=SearchType.tankoubon,session=requests):
#     # SEARCH_URL=BASE_URL + "/" + type_ + "/" + str(year) + "/" + str(month)
#     SEARCH_URL2=BASE_URL2 + "/" + type_ + "/" + "week"
#     # res=session.get(SEARCH_URL,headers=HEADERS)
#     res=session.get(SEARCH_URL2,headers=HEADERS)
#     res.encoding='utf-8'
#     return res.text



# def toData(l):
#   productRanking=l.select_one(".book__ranking").find("span").text


#   productImage=l.select_one(".book__cover").find("a").find("img").get("src")


#   productUrl=URL + l.select_one(".book__cover").find("a").get("href")


#   productDetail=l.select_one(".book__detail")


#   productTitle=productDetail.select_one(".detail__title").find("a").text
#   productAuthor=productDetail.select_one(".detail__authors").find("li").find("a").text


#   productEvaluation=productDetail.select_one(".detail__options").find("dd").text


# 	# return {
# 	# "ranking":productRanking,
# 	# 	"title":productTitle,
# 	# 	"url":productUrl,
# 	# 	"author":productAuthor,
# 	# 	"evaluation":productEvaluation,
# 	# "image":productImage
# 	# }
  
#   return {
#     "ranking":int(extract_rank(productRanking)),
# 		"title":productTitle,
# 		# "url":productUrl,
# 		"author":extract_author(productAuthor),
# 		# "evaluation":productEvaluation,
#     "image":productImage
# 	}

  

# def getData(soup):
#   for l in soup.select(".list__book"):
#     yield toData(l)
# def search_bookmeter_ranking(type_=SearchType.tankoubon,session=requests):
#   text=_search(type_,session)
#   soup=bs(text,"html.parser")
#   for data in getData(soup):
#     # SEARCH_URL=BASE_URL + "/" + type_ + "/" + str(year) + "/" + str(month)
#     SEARCH_URL2=BASE_URL2 + "/" + type_ + "/" + "week"
#     # data["url"]=up.urljoin(SEARCH_URL,data["url"])
#     # data["url"]=up.urljoin(SEARCH_URL2,data["url"])
#     yield data










# 2024/07/19　試す前用保存
# 本コードのコピー
# ブックメーターのランキング
from typing import Pattern
import requests
from bs4 import BeautifulSoup as bs
import urllib.parse as up
import datetime
import re

from .rakuten_api import fetch_rakuten, run_async


HOST="bookmeter.com"
URL="https://"+HOST
# BASE_URL=URL+"/rankings/monthly"

BASE_URL2=URL+"/rankings/latest/wish_book"


HEADERS={ "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}



# rakuten_apiからデータを取得する関数
def get_book_info(title, author):
    book_data = run_async(fetch_rakuten(title, author))
    if book_data:
        print("データを取得しました:", book_data)
        return book_data
    else:
        print("データの取得に失敗しました。")
        return None


class SearchType:
  bunko="bunko"
  tankoubon="tankoubon"
  comic="comic"
  light_novel= "light_novel"
  others="others"


today=datetime.date.today()



year=today.year
month=today.month - 1
if month == 0:
  year -= 1
  month = 12


def extract_rank(text):
    pattern = r"(\d+)位"
    match = re.search(pattern, text)
    if match:
        return match.group(1)
    else:
        return None



def extract_author(text):
    pattern1 = r"\u3000"
    pattern2 = r" "
    match1 = re.search(pattern1, text)
    match2 = re.search(pattern2, text)
    if match1:
        return re.sub(r"[\u3000]", "", text)
    elif match2:
        return re.sub(r"[ ]", "", text)
    else:
        return text


def _search(type_=SearchType.tankoubon,session=requests):
    # SEARCH_URL=BASE_URL + "/" + type_ + "/" + str(year) + "/" + str(month)
    SEARCH_URL2=BASE_URL2 + "/" + type_ + "/" + "week"
    # res=session.get(SEARCH_URL,headers=HEADERS)
    res=session.get(SEARCH_URL2,headers=HEADERS)
    res.encoding='utf-8'
    return res.text



def toData(l):
  productRanking=l.select_one(".book__ranking").find("span").text


  productImage=l.select_one(".book__cover").find("a").find("img").get("src")


  productUrl=URL + l.select_one(".book__cover").find("a").get("href")


  productDetail=l.select_one(".book__detail")


  productTitle=productDetail.select_one(".detail__title").find("a").text
  productAuthor=productDetail.select_one(".detail__authors").find("li").find("a").text


  productEvaluation=productDetail.select_one(".detail__options").find("dd").text

  
  # rakuten_apiからデータを取得
  title=productTitle
  author=productAuthor
  book_info = get_book_info(title, author)
  
  productIsbn = book_info['isbn']
  productPrice = book_info['itemPrice']
  productCaption = book_info['itemCaption']
  productPublisher = book_info['publisherName']
  productSalesDate = book_info['salesDate']


	# return {
	# "ranking":productRanking,
	# 	"title":productTitle,
	# 	"url":productUrl,
	# 	"author":productAuthor,
	# 	"evaluation":productEvaluation,
	# "image":productImage
	# }
  
  return {
    "ranking":int(extract_rank(productRanking)),
		"title":productTitle,
		# "url":productUrl,
		"author":extract_author(productAuthor),
		# "evaluation":productEvaluation,
    "image":productImage
	}

  

def getData(soup):
  for l in soup.select(".list__book"):
    yield toData(l)
def search_bookmeter_ranking(type_=SearchType.tankoubon,session=requests):
  text=_search(type_,session)
  soup=bs(text,"html.parser")
  for data in getData(soup):
    # SEARCH_URL=BASE_URL + "/" + type_ + "/" + str(year) + "/" + str(month)
    SEARCH_URL2=BASE_URL2 + "/" + type_ + "/" + "week"
    # data["url"]=up.urljoin(SEARCH_URL,data["url"])
    # data["url"]=up.urljoin(SEARCH_URL2,data["url"])
    yield data