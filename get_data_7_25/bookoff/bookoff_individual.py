# とりあえず単体はおｋな奴 untitled23
#取ってくるページ
#https://shopping.bookoff.co.jp/list/ranking.html?genre=12
import asyncio
import aiohttp
import urllib.parse

from bs4 import BeautifulSoup as bs
import requests
import re

class SearchType:
  BOOK=12
  NOVEL=1201
  TANKOUBON=1221

HEADERS={ "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}


# 取得したデータから価格のみを抽出
def clean_price(price_str):
    match = re.search(r'(\d+)円', price_str)
    if match:
        return int(match.group(1))
    return 0


def extract_date(text):
    # 正規表現パターンを使用して日付を抽出
    pattern = r'\d{4}/\d{2}/\d{2}'
    match = re.search(pattern, text)

    if match:
        return match.group()
    else:
        return text  # 日付が見つからない場合


async def _search_indi(productUrl, type_=SearchType.TANKOUBON):
    async with aiohttp.ClientSession() as session:
        async with session.get(productUrl, headers=HEADERS) as response:
            return await response.text()


async def toData_indi(l):
  productItem = l
  # print("productItem",productItem)

  productDetail__tableWrap = productItem.select_one(".productDetail__tableWrap")
  productDetail__table = productDetail__tableWrap.select_one(".productDetail__table")

  tbody = productDetail__table.select_one("tbody")

  rows = tbody.find_all('tr')
  # print("rows",rows)

  key_list = ['itemCaption', 'publisherName', 'salesDate', 'isbn']
  data = {}

  for index, row in enumerate(rows):
    cells = row.find('td')
    # print("cells",cells)
    if cells:
      key = key_list[index]
      value = extract_date(cells.text.strip())
      data[key] = value

      data['itemPrice'] = 0

  # print(data)

  return data


async def getData_indi(soup):
  # 試すように数を制限
  for l in soup.select(".productDetail")[:5]:
    yield await toData_indi(l)
async def search_bookoff_indi(productUrl, type_=SearchType.TANKOUBON,session=requests):
  text = await _search_indi(productUrl, type_)
  soup= bs(text,"html.parser")
  async for data in getData_indi(soup):
    yield data

async def get_data_individual(productUrl):
  async for data in search_bookoff_indi(productUrl):
    # print("get_data",data)
    return data



# コラボラトリー用の実行部分
# kari = await get_data_individual("https://shopping.bookoff.co.jp/used/0017245050")
# print("kari",kari)


# VScode用の実行部分
async def main():
  kari = await get_data_individual("https://shopping.bookoff.co.jp/used/0017245050")
  # print("kari",kari)
if __name__ == "__main__":
    asyncio.run(main())