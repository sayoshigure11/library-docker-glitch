import asyncio
import aiohttp
import urllib.parse

from bs4 import BeautifulSoup as bs
import requests
import re

HEADERS={ "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}



def extract_asin(url):
    pattern = r'/dp/product/([0-9X]{10})/'
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    else:
        return None


async def _search_indi(productUrl):
    async with aiohttp.ClientSession() as session:
        async with session.get(productUrl, headers=HEADERS) as response:
            return await response.text()


async def toData_indi(l):
  productItem = l
  # print("productItem",productItem)
  productImageUrl = productItem.select_one(".image__cover").get("href")
  # print("productImage",productImageUrl)
  isbn = extract_asin(productImageUrl)
  # print("isbn",isbn)

  return {
      "isbn":isbn
  }


async def getData_indi(soup):
  # 試すように数を制限
  # print("soup",soup)
  for l in soup.select(".sidebar__group")[0]:
    # print("l",l)
    yield await toData_indi(l)
async def search_bookmeter_indi(product_url):
  text = await _search_indi(product_url)
  soup= bs(text,"html.parser")
  async for data in getData_indi(soup):
    yield data

async def get_individual_bookmeter_data(product_url):
  async for data in search_bookmeter_indi(product_url):
    # print("get_data",data)
    return data


# コラボラトリー用の実行部分
# getted_data = await get_individual_bookmeter_data("https://bookmeter.com/books/22035474")
# print(getted_data)



# VScode用の実行部分
async def main():
  kari = await get_individual_bookmeter_data("https://bookmeter.com/books/22035474")
  print("kari",kari)
if __name__ == "__main__":
    asyncio.run(main())