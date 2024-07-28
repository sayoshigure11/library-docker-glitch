# Google_booksからデータを取得
import requests
import json
import asyncio

async def get_book_data_google(isbn):
    # isbn = "9784022650591"
    url_google = f'https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}' #GooglBooksAPI
    # response = requests.get(url)
    response_google = requests.get(url_google).json() #情報の取得,json変換

    if response_google:
      try:
        description = response_google['items'][0]['volumeInfo']['description']
        publishedDate = response_google['items'][0]['volumeInfo']['publishedDate']
        page_count = response_google['items'][0]['volumeInfo']['pageCount']

        google_fetch = True

      except KeyError:
        # print("指定されたパスでdescriptionが見つかりません。")

        google_fetch = False

        # return None

    else:
        print("Book not found in Google Books.")
        # 次のフェッチを行う

        google_fetch = False

        # return None


    if google_fetch == False:
      return {
          "google_data": False,
          # "title": "",
          # "authors": "",
          "description": "",
          "publishedDate": "",
          "page_count": "",
      }
    return {
        "google_data": google_fetch,
        # "title": title,
        # "authors": authors,
        "description": description,
        "publishedDate": publishedDate,
        "page_count": page_count,
    }


# コラボラトリー用の実行部分
# isbn = "9784479782995"
# response_google = await get_book_data_google(isbn)
# print(response_google)



# VScode用の実行部分
# VScode用の実行部分
async def main():
    get_data = await get_book_data_google("9784103549512")
    print("get_data",get_data)

if __name__ == "__main__":
    asyncio.run(main())