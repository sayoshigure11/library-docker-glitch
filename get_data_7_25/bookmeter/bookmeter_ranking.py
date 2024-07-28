# 2024/07/24
# 本コードのコピー
# ブックメーターのランキング
from typing import Pattern
import requests
from bs4 import BeautifulSoup as bs
import urllib.parse as up
import datetime
import re
import aiohttp


# # python3 -m clear_up用　shuna@LAPTOP-VHG04PF2:~/next-jikken/library-docker-glitch/get_data_7_25
# from .bookmeter_individual import get_individual_bookmeter_data
# import sys
# sys.path.append("..")
# from api.rakuten_api import fetch_rakuten


# python3 kari_flask.py用　shuna@LAPTOP-VHG04PF2:~/next-jikken/library-docker-glitch
from get_data_7_25.bookmeter.bookmeter_individual import get_individual_bookmeter_data
from get_data_7_25.api.rakuten_api import fetch_rakuten

HOST="bookmeter.com"
URL="https://"+HOST
# BASE_URL=URL+"/rankings/monthly"

BASE_URL2= URL+"/rankings/latest/wish_book"


HEADERS={ "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}

# priceから数字を抽出する関数
def extract_numbers(text):
  """
  文字列から数字だけを抽出します。

  Args:
    text: 数字を含む文字列

  Returns:
    数字のみを含む文字列
  """
  return re.findall(r"\d+", text)

# rakuten_apiからデータを取得する関数
async def get_book_info(isbn):
    book_data = await fetch_rakuten(isbn)
    if book_data:
        # print("データを取得しました:", book_data)
        return book_data
    else:
        print("データの取得に失敗しました。")
        return None


class SearchType:
  bunko=2
  tankoubon=1
  comic=9
  all=0

class SearchType_bookmeter:
  bunko="bunko"
  tankoubon="tankoubon"
  comic="comic"

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


async def _search(type_=SearchType_bookmeter.tankoubon):
    async with aiohttp.ClientSession() as session:
        book_size = type_
        SEARCH_URL2= BASE_URL2 + "/" + type_ + "/" + "week"
        async with session.get(SEARCH_URL2, headers=HEADERS) as response:
            return await response.text()



async def toData(l):
  # print("l",l)
  productRanking=l.select_one(".book__ranking").find("span").text


  productImage=l.select_one(".book__cover").find("a").find("img").get("src")


  productUrl=URL + l.select_one(".book__cover").find("a").get("href")


  productDetail=l.select_one(".book__detail")


  productTitle=productDetail.select_one(".detail__title").find("a").text
  productAuthor=productDetail.select_one(".detail__authors").find("li").find("a").text


  productEvaluation=productDetail.select_one(".detail__options").find("dd").text

  # isbnをamazonのurlから取得する
  isbn = await get_individual_bookmeter_data(productUrl)
  # print("isbn",isbn)
  book_info = await get_book_info(isbn['isbn'])


  if book_info and book_info['rakuten_api_library'] == True:
    productIsbn = book_info['isbn']
    productPrice = book_info['itemPrice']
    productCaption = book_info['itemCaption']
    productPublisher = book_info['publisherName']
    productSalesDate = book_info['salesDate']
    productPageCount = ""

  elif book_info and book_info['rakuten_api_library'] == False:
    if book_info['price'] == "":
      book_info['price'] = 0
    if book_info['page_count'] == "":
      book_info['page_count'] = 0

    productIsbn = book_info['isbn']
    productPrice = book_info['price']
    productCaption = book_info['caption']
    productPublisher = book_info['publisher']
    productSalesDate = book_info['publishedDate']
    productPageCount = book_info['page_count']

  extracted_price = extract_numbers(str(productPrice))


  return {
    "ranking":int(extract_rank(productRanking)),
		"title":productTitle,
		"isbn":productIsbn,
		"author":productAuthor,
		# "price":int(productPrice),
    "price":int(extracted_price[0]),
		"caption":productCaption,
    "publisher":productPublisher,
    "salesDate":productSalesDate,
    "image":productImage
	}



async def getData(soup):
  for l in soup.select(".list__book")[:3]:
    yield await toData(l)
async def search_bookmeter_ranking(type_=SearchType_bookmeter.bunko ,session=requests):
  text= await _search(type_)
  soup=bs(text,"html.parser")
  async for data in getData(soup):
    # SEARCH_URL=BASE_URL + "/" + type_ + "/" + str(year) + "/" + str(month)
    SEARCH_URL2= BASE_URL2 + "/" + type_ + "/" + "week"
    yield data