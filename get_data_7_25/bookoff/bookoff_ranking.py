# 2024/07/11/05:30
# 本コードのコピー
# ブックオフランキング
import requests
from bs4 import BeautifulSoup as bs
import urllib.parse as up
import re
import aiohttp

# # python3 -m clear_up用　shuna@LAPTOP-VHG04PF2:~/next-jikken/library-docker-glitch/get_data_7_25
# from .bookoff_individual import get_data_individual

# import sys
# sys.path.append("..")
# from api.rakuten_api import fetch_rakuten


# python3 kari_flask.py用　shuna@LAPTOP-VHG04PF2:~/next-jikken/library-docker-glitch
from get_data_7_25.bookoff.bookoff_individual import get_data_individual
from get_data_7_25.api.rakuten_api import fetch_rakuten


HOST="shopping.bookoff.co.jp"
URL="https://"+HOST
SEARCH_URL=URL+"/list/ranking.html"


HEADERS={ "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}


#取ってくるページ
#https://shopping.bookoff.co.jp/list/ranking.html?genre=12


class SearchType:
  BOOK=12
  NOVEL=1201
  TANKOUBON=1221


# rakuten_apiからデータを取得する関数
async def get_book_info(isbn):
    book_data = await fetch_rakuten(isbn)
    if book_data:
        # print("データを取得しました:", book_data)
        return book_data
    else:
        print("データの取得に失敗しました。")
        return None


# 取得したデータから価格のみを抽出
async def clean_price(price_str):
    match = await re.search(r'(\d+)円', price_str)
    if match:
        return int(match.group(1))
    return None

def extract_rank(product_rank):
    match = re.search(r'(\d+)位', product_rank)
    if match:
        return int(match.group(1))
    return None

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


async def _search(type_=SearchType.BOOK):
    async with aiohttp.ClientSession() as session:
        params = {"genre": type_}
        async with session.get(SEARCH_URL, headers=HEADERS, params=params) as response:
            return await response.text()


async def toData(l):
  productItem= l

  productUrl= URL + productItem.find("a").get("href")


  productImage= productItem.find("a").find("img").get("src")


  productDetail1= productItem.select_one(".productItem__detail")
  productDetail= productDetail1.find("a")


  productRanking= productDetail.find("span").find("strong").text
  # print("productRanking",productRanking)


  productTitle= productDetail.select_one(".productItem__title").text
  productAuthor= productDetail.select_one(".productItem__author").text
  productPrice= clean_price(productItem.select_one(".productItem__price").text)


  stocked= productDetail1.select_one(".productItem__btns").find("a").text


  # 商品の個別ページからデータを取得
  product_data = await get_data_individual(productUrl)
  productIsbn = product_data['isbn']
  productPrice = product_data['itemPrice']
  productCaption = product_data['itemCaption']
  productPublisher = product_data['publisherName']
  productSalesDate = product_data['salesDate']

  # rakuten_apiからデータを取得
  # title= productTitle
  # author= productAuthor
  book_info = await get_book_info(productIsbn)





  # if book_info != "null":
  #   print("rakuten_apiからデータを取得しました:",book_info)
  #   productIsbn = book_info['isbn']
  #   productPrice = book_info['itemPrice']
  #   productCaption = book_info['itemCaption']
  #   productPublisher = book_info['publisherName']
  #   productSalesDate = book_info['salesDate']


  # if stocked=="入荷お知らせ":
  #   productStocked=False
  # else:
  #   productStocked=True

  # return {
  #   "ranking":int(productRanking),
	# 	"title":productTitle,
	# 	"isbn":productIsbn,
	# 	"author":productAuthor,
	# 	"price":int(productPrice),
	# 	"caption":productCaption,
  #   "publisher":productPublisher,
  #   "salesDate":productSalesDate,
  #   "image":productImage
	# }



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
    # "ranking":extract_rank(productRanking),
    "ranking":int(productRanking),
		"title":productTitle,
		"isbn":productIsbn,
		"author":productAuthor,
		# "price":int(clean_price(productPrice)),
    "price":int(extracted_price[0]),
		"caption":productCaption,
    "publisher":productPublisher,
    "salesDate":productSalesDate,
    "image":productImage
	}




async def getData(soup):
  # 試すように数を制限
  for l in soup.select(".productItem__inner")[:3]:
    yield await toData(l)
async def search_bookoff_ranking(type_=SearchType.BOOK,session=requests):
  text = await _search(type_)
  soup= bs(text,"html.parser")
  async for data in getData(soup):
    yield data