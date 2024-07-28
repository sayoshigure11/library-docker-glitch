# 2024/07/11/05:30
# 本コードのコピー
# ブクログのランキングデータ
# import requests
from bs4 import BeautifulSoup as bs
import urllib.parse as up
import datetime
import re
import aiohttp

# # python3 -m clear_up用　shuna@LAPTOP-VHG04PF2:~/next-jikken/library-docker-glitch/get_data_7_25
# import sys
# sys.path.append("..")
# from api.rakuten_api import fetch_rakuten


# python3 kari_flask.py用　shuna@LAPTOP-VHG04PF2:~/next-jikken/library-docker-glitch
from get_data_7_25.api.rakuten_api import fetch_rakuten


HOST="booklog.jp"
URL="https://"+HOST
BASE_URL=URL+"/ranking/weekly"


HEADERS={ "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}


# urlからisbnを抽出する関数
import re

def extract_number(input_string):
    pattern = r'/item/1/(\d+)'
    match = re.search(pattern, input_string)
    if match:
        return match.group(1)
    else:
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


# rakuten_apiからデータを取得する関数
async def get_book_info(get_isbn):
    # book_data = await run_async(fetch_rakuten(get_isbn))
    book_data = await fetch_rakuten(get_isbn)
    if book_data:
        # print("データを取得しました:", book_data)
        return book_data
    else:
        print("データの取得に失敗しました。")
        return None


class SearchType:
  book = "book"
  bunko = "bunko"
  shinsho = "shinsho"
  comic = "comic"
  honour = "honour"


today=datetime.date.today()

from datetime import datetime, timedelta
from calendar import Calendar

date=datetime.now() - timedelta(hours=12)

calendar = Calendar(firstweekday=0)
month_calendar = calendar.monthdays2calendar(date.year, date.month)


count=1
for week in month_calendar:
  for day in week:
    if day[0] == date.day:
      break
  else:
    count+=1
    continue
  break

year=str(today.year)
month=date.month
if month == 0:
  year -= 1
  month = 12
elif month == 1:
  month = "01"
elif month == 2:
  month = "02"
elif month == 3:
  month = "03"
elif month == 4:
  month = "04"
elif month == 5:
  month = "05"
elif month == 6:
  month = "06"
elif month == 7:
  month = "07"
elif month == 8:
  month = "08"
elif month == 9:
  month = "09"
week = count




# def _search(type_=SearchType.book,session=requests):
#     SEARCH_URL=BASE_URL + "/" + str(year) + str(month) + "/" + str(count) + "/" + type_
#     res=session.get(SEARCH_URL,headers=HEADERS)
#     res.encoding='utf-8'
#     return res.text

async def _search(type_=SearchType.book):
    async with aiohttp.ClientSession() as session:
        SEARCH_URL=BASE_URL + "/" + str(year) + str(month) + "/" + str(count) + "/" + type_
        print("SEARCH_URL", SEARCH_URL)
        async with session.get(SEARCH_URL, headers=HEADERS) as response:
            return await response.text()




async def toData(l):
  productRanking=l.select_one(".ranking").select_one(".rank-num").find("span").text

  productImage=l.select_one(".thumb").find("a").find("img").get("src")

  productUrl= URL + l.select_one(".thumb").find("a").get("href")



  productTitle= l.select_one(".desc").find("h3").find("a").text
  productAuthor= l.select_one(".descMini").select_one(".itemInfoElmBox").find("span").find("a").text



  # isbnを取得するための前段階
  get_isbn = str(extract_number(l.select_one(".thumb").find("a").get("href")))
  # print("get_isbn",get_isbn)
  # rakuten_apiからデータを取得
  book_info = await get_book_info(get_isbn)



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

  else:
    productIsbn = get_isbn
    productPrice = 0
    productCaption = ""
    productPublisher = ""
    productSalesDate = ""
    productPageCount = ""


  # print("productIsbn",productIsbn)
  # print("productPrice",productPrice)
  # print("productCaption",productCaption)
  # print("productPublisher",productPublisher)
  # print("productSalesDate",productSalesDate)
  # print("productPageCount",productPageCount)
  extracted_price = extract_numbers(str(productPrice))


  return {
    "ranking":int(productRanking),
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
  # print("soup",soup)
  kari1 = soup.select_one(".autopagerize_page_element.t20M")
  print("kari1",kari1)
  kari2 = kari1.select_one(".ranking-list")
  for l in kari2.select(".clearFix")[:3]:
    yield await toData(l)
async def search_booklog_ranking(type_=SearchType.book):
  text= await _search(type_)
  soup= bs(text,"html.parser")
  async for data in getData(soup):
    SEARCH_URL=BASE_URL + "/" + str(year) + str(month) + "/" + str(count) + "/" + type_
    yield data