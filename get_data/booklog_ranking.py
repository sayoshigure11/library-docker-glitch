# # ブクログのランキングデータ
# import requests
# from bs4 import BeautifulSoup as bs
# import urllib.parse as up
# import datetime


# HOST="booklog.jp"
# URL="https://"+HOST
# BASE_URL=URL+"/ranking/weekly"


# HEADERS={ "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}


# class SearchType:
#   book = "book"
#   bunko = "bunko"
#   shinsho = "shinsho"
#   comic = "comic"
#   honour = "honour"


# today=datetime.date.today()

# from datetime import datetime
# from calendar import Calendar

# date=datetime.now()

# calendar = Calendar(firstweekday=0)
# month_calendar = calendar.monthdays2calendar(date.year, date.month)

# #print(month_calendar)

# print(date.day)

# count=1
# for week in month_calendar:
#   for day in week:
#     if day[0] == date.day:
#       break
#   else:
#     count+=1
#     continue
#   break

# print(str(date.month)+'月' + str(date.day) + '日は第' + str(count)+ '週目です')


# year=str(today.year)
# month=today.month - 1
# if month == 0:
#   year -= 1
#   month = 12
# elif month == 1:
#   month = "01"
# elif month == 2:
#   month = "02"
# elif month == 3:
#   month = "03"
# elif month == 4:
#   month = "04"
# elif month == 5:
#   month = "05"
# elif month == 6:
#   month = "06"
# elif month == 7:
#   month = "07"
# elif month == 8:
#   month = "08"
# elif month == 9:
#   month = "09"
# week = count




# def _search(type_=SearchType.book,session=requests):
#     SEARCH_URL=BASE_URL + "/" + str(year) + str(month) + "/" + str(week) + "/" + type_
#     res=session.get(SEARCH_URL,headers=HEADERS)
#     res.encoding='utf-8'
#     return res.text




# def toData(l):
#   productRanking=l.select_one(".ranking").select_one(".rank-num").find("span").text
#   print(productRanking)

#   productImage=l.select_one(".thumb").find("a").find("img").get("src")
#   print(productImage)

#   productUrl=URL + l.select_one(".thumb").find("a").get("href")
#   print(productUrl)

#   productTitle= l.select_one(".desc").find("h3").find("a").text
#   print(productTitle)
#   productAuthor= l.select_one(".descMini").select_one(".itemInfoElmBox").find("span").find("a").text
#   print(productAuthor)

#   #なぜか取得出来ない .select_one("info-rating")の段階でNoneになる　理由は不明
#   # productEvaluation=l.select_one(".desc").select_one(".aggregate.b15M").select_one("info-rating").find("span").text
#   # print(productEvaluation)


#   return {
#     "ranking":productRanking,
# 		"title":productTitle,
# 		# "url": productUrl,
# 		"author":productAuthor,
# 		# "evaluation":productEvaluation,
#     "image":productImage
# 	}


# def getData(soup):
#   kari1 = soup.select_one(".autopagerize_page_element.t20M")
#   kari2 = kari1.select_one(".ranking-list")
#   #for l in soup.select_one(".autopagerize_page_element t20M").select_one(".ranking-list").select(".clearFix"):
#   for l in kari2.select(".clearFix"):
#     yield toData(l)
# def search(type_=SearchType.book,session=requests):
#   text=_search(type_,session)
#   soup=bs(text,"html.parser")
#   for data in getData(soup):
#     SEARCH_URL=BASE_URL + "/" + str(year) + str(month) + "/" + str(week) + "/" + type_
#     data["url"]=up.urljoin(SEARCH_URL,data["url"])
#     print(data)
#     yield data



# # reslusts = list(search())
# # # Notebookのセルに出力
# # reslusts

# # なんかisocalendar()のweekとweekdayが逆になってない？バグ？？？
# # print(today.isocalendar()[2])

# # print(BASE_URL + "/" + str(year) + str(month) + "/" + str(week) + "/" + "book")







# # 本コードのコピー
# # ブクログのランキングデータ
# import requests
# from bs4 import BeautifulSoup
# import urllib.parse as up
# import datetime


# HOST="booklog.jp"
# URL="https://"+HOST
# BASE_URL=URL+"/ranking/weekly"


# HEADERS={ "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}


# class SearchType:
#   book = "book"
#   bunko = "bunko"
#   shinsho = "shinsho"
#   comic = "comic"
#   honour = "honour"


# today=datetime.date.today()

# from datetime import datetime
# from calendar import Calendar

# date=datetime.now()

# calendar = Calendar(firstweekday=0)
# month_calendar = calendar.monthdays2calendar(date.year, date.month)


# count=1
# for week in month_calendar:
#   for day in week:
#     if day[0] == date.day:
#       break
#   else:
#     count+=1
#     continue
#   break

# # print(str(date.month)+'月' + str(date.day) + '日は第' + str(count)+ '週目です')


# year=str(today.year)
# month=today.month - 1
# if month == 0:
#   year -= 1
#   month = 12
# elif month == 1:
#   month = "01"
# elif month == 2:
#   month = "02"
# elif month == 3:
#   month = "03"
# elif month == 4:
#   month = "04"
# elif month == 5:
#   month = "05"
# elif month == 6:
#   month = "06"
# elif month == 7:
#   month = "07"
# elif month == 8:
#   month = "08"
# elif month == 9:
#   month = "09"
# week = count




# def _search(type_=SearchType.book,session=requests):
#     SEARCH_URL=BASE_URL + "/" + str(year) + str(month) + "/" + str(week) + "/" + type_
#     res=session.get(SEARCH_URL,headers=HEADERS)
#     res.encoding='utf-8'
#     return res.text




# def toData(l):
#   productRanking=l.select_one(".ranking").select_one(".rank-num").find("span").text

#   productImage=l.select_one(".thumb").find("a").find("img").get("src")

#   productUrl=URL + l.select_one(".thumb").find("a").get("href")

#   productTitle= l.select_one(".desc").find("h3").find("a").text
#   productAuthor= l.select_one(".descMini").select_one(".itemInfoElmBox").find("span").find("a").text

# 	# return {
# 	# "ranking":productRanking,
# 	# 	"title":productTitle,
# 	# 	"url": productUrl,
# 	# 	"author":productAuthor,
# 	# 	# "evaluation":productEvaluation,
# 	# "image":productImage
# 	# }
  
#   return {
#     "ranking":int(productRanking),
# 		"title":productTitle,
# 		# "url": productUrl,
# 		"author":productAuthor,
# 		# "evaluation":productEvaluation,
#     "image":productImage
# 	}


# def getData(soup):
#   kari1 = soup.select_one(".autopagerize_page_element.t20M")
#   kari2 = kari1.select_one(".ranking-list")
#   for l in kari2.select(".clearFix"):
#     yield toData(l)
# def search_booklog_ranking(type_=SearchType.book,session=requests):
#   text=_search(type_,session)
#   soup=bs(text,"html.parser")
#   for data in getData(soup):
#     SEARCH_URL=BASE_URL + "/" + str(year) + str(month) + "/" + str(week) + "/" + type_
#     data["url"]=up.urljoin(SEARCH_URL,data["url"])
#     print(data)
#     yield data













# # 本コードのコピー
# # ブクログのランキングデータ
# import requests
# from bs4 import BeautifulSoup as bs
# import urllib.parse as up
# import datetime


# HOST="booklog.jp"
# URL="https://"+HOST
# BASE_URL=URL+"/ranking/weekly"


# HEADERS={ "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}


# class SearchType:
#   book = "book"
#   bunko = "bunko"
#   shinsho = "shinsho"
#   comic = "comic"
#   honour = "honour"


# today=datetime.date.today()

# from datetime import datetime
# from calendar import Calendar

# date=datetime.now()

# calendar = Calendar(firstweekday=0)
# month_calendar = calendar.monthdays2calendar(date.year, date.month)


# count=1
# for week in month_calendar:
#   for day in week:
#     if day[0] == date.day:
#       break
#   else:
#     count+=1
#     continue
#   break

# # print(str(date.month)+'月' + str(date.day) + '日は第' + str(count)+ '週目です')


# year=str(today.year)
# month=today.month - 1
# if month == 0:
#   year -= 1
#   month = 12
# elif month == 1:
#   month = "01"
# elif month == 2:
#   month = "02"
# elif month == 3:
#   month = "03"
# elif month == 4:
#   month = "04"
# elif month == 5:
#   month = "05"
# elif month == 6:
#   month = "06"
# elif month == 7:
#   month = "07"
# elif month == 8:
#   month = "08"
# elif month == 9:
#   month = "09"
# week = count




# def _search(type_=SearchType.book,session=requests):
#     SEARCH_URL=BASE_URL + "/" + str(year) + str(month) + "/" + str(week) + "/" + type_
#     res=session.get(SEARCH_URL,headers=HEADERS)
#     res.encoding='utf-8'
#     return res.text




# def toData(l):
#   productRanking=l.select_one(".ranking").select_one(".rank-num").find("span").text

#   productImage=l.select_one(".thumb").find("a").find("img").get("src")

#   productUrl=URL + l.select_one(".thumb").find("a").get("href")

#   productTitle= l.select_one(".desc").find("h3").find("a").text
#   productAuthor= l.select_one(".descMini").select_one(".itemInfoElmBox").find("span").find("a").text

# 	# return {
# 	# "ranking":productRanking,
# 	# 	"title":productTitle,
# 	# 	"url": productUrl,
# 	# 	"author":productAuthor,
# 	# 	# "evaluation":productEvaluation,
# 	# "image":productImage
# 	# }
  
#   return {
#     "ranking":int(productRanking),
# 		"title":productTitle,
# 		# "url": productUrl,
# 		"author":productAuthor,
# 		# "evaluation":productEvaluation,
#     "image":productImage
# 	}


# def getData(soup):
#   kari1 = soup.select_one(".autopagerize_page_element.t20M")
#   kari2 = kari1.select_one(".ranking-list")
#   for l in kari2.select(".clearFix"):
#     yield toData(l)
# def search_booklog_ranking(type_=SearchType.book,session=requests):
#   text=_search(type_,session)
#   soup=bs(text,"html.parser")
#   for data in getData(soup):
#     SEARCH_URL=BASE_URL + "/" + str(year) + str(month) + "/" + str(week) + "/" + type_
#     # data["url"]=up.urljoin(SEARCH_URL,data["url"])
#     print(data)
#     yield data



# # results = [data for data in search_booklog_ranking()]
# results = list(search_booklog_ranking())

# # Notebookのセルに出力
# results





# 2024/07/19　試す前用保存
# 本コードのコピー
# ブクログのランキングデータ
import requests
from bs4 import BeautifulSoup as bs
import urllib.parse as up
import datetime


from .rakuten_api import fetch_rakuten, run_async


HOST="booklog.jp"
URL="https://"+HOST
BASE_URL=URL+"/ranking/weekly"


HEADERS={ "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}



# rakuten_apiからデータを取得する関数
def get_book_info(title, author):
    book_data = run_async(fetch_rakuten(title, author))
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

from datetime import datetime
from calendar import Calendar

date=datetime.now()

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

# print(str(date.year)+'年' + str(date.month)+'月' + str(date.day) + '日は第' + str(count)+ '週目です')


year=str(today.year)
# month=today.month - 1
# if month == 0:
#   year -= 1
#   month = 12
# elif month == 1:
#   month = "01"
# elif month == 2:
#   month = "02"
# elif month == 3:
#   month = "03"
# elif month == 4:
#   month = "04"
# elif month == 5:
#   month = "05"
# elif month == 6:
#   month = "06"
# elif month == 7:
#   month = "07"
# elif month == 8:
#   month = "08"
# elif month == 9:
#   month = "09"
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




def _search(type_=SearchType.book,session=requests):
    # SEARCH_URL=BASE_URL + "/" + str(year) + str(month) + "/" + str(week) + "/" + type_
    SEARCH_URL=BASE_URL + "/" + str(year) + str(month) + "/" + str(count) + "/" + type_
    res=session.get(SEARCH_URL,headers=HEADERS)
    res.encoding='utf-8'
    return res.text




def toData(l):
  productRanking=l.select_one(".ranking").select_one(".rank-num").find("span").text

  productImage=l.select_one(".thumb").find("a").find("img").get("src")

  productUrl=URL + l.select_one(".thumb").find("a").get("href")

  productTitle= l.select_one(".desc").find("h3").find("a").text
  productAuthor= l.select_one(".descMini").select_one(".itemInfoElmBox").find("span").find("a").text

  

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
	# 	"url": productUrl,
	# 	"author":productAuthor,
	# 	# "evaluation":productEvaluation,
	# "image":productImage
	# }
  
  return {
    "ranking":int(productRanking),
		"title":productTitle,
		# "url": productUrl,
		"author":productAuthor,
		# "evaluation":productEvaluation,
    "image":productImage
	}


def getData(soup):
  kari1 = soup.select_one(".autopagerize_page_element.t20M")
  kari2 = kari1.select_one(".ranking-list")
  for l in kari2.select(".clearFix"):
    yield toData(l)
def search_booklog_ranking(type_=SearchType.book,session=requests):
  text=_search(type_,session)
  soup=bs(text,"html.parser")
  for data in getData(soup):
    # SEARCH_URL=BASE_URL + "/" + str(year) + str(month) + "/" + str(week) + "/" + type_
    SEARCH_URL=BASE_URL + "/" + str(year) + str(month) + "/" + str(count) + "/" + type_
    # data["url"]=up.urljoin(SEARCH_URL,data["url"])
    # print(data)
    yield data