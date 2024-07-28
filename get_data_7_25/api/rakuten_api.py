# 楽天api
import asyncio
import aiohttp
import urllib.parse

# # python3 -m clear_up用　shuna@LAPTOP-VHG04PF2:~/next-jikken/library-docker-glitch/get_data_7_25
# import sys
# sys.path.append("..")
# from matome_jikkou import jikkou


# python3 kari_flask.py用　shuna@LAPTOP-VHG04PF2:~/next-jikken/library-docker-glitch
from get_data_7_25.matome_jikkou import jikkou

async def delay(ms: int):
    await asyncio.sleep(ms / 1000)  # milliseconds to seconds

async def fetch_with_timeout(url, timeout=10):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url, timeout=timeout) as response:
                return await response.json()
        except asyncio.TimeoutError:
            print(f"リクエストがタイムアウトしました。(タイムアウト: {timeout}秒)")
            return None
        except aiohttp.ClientError as e:
            print(f"リクエスト中にエラーが発生しました: {e}")
            return None

async def fetch_rakuten(isbn):
    # 楽天ブックスAPIのURL
    url = f"https://app.rakuten.co.jp/services/api/BooksBook/Search/20170404?format=json&isbn={isbn}&applicationId=1057691251432321112"
    print("2秒間待機します...")
    await delay(2000)
    print("待機終了、データ取得を開始します。")

    # タイムアウトを10秒に設定してfetchを実行
    result = await fetch_with_timeout(url, timeout=30)

    if result:
        hits = result.get('hits')
        if hits == 0:
            print("データが見つかりませんでした。 rakuten")
            # return None

            # 図書館apiなどと合体させてから
            product_data = await jikkou(isbn)
            # print("product_data",product_data)
            product_data['rakuten_api_library'] = False
            return product_data
        else:
          data = result.get('Items')[0]['Item']
          # print("データを取得しました rakuten:", data)
          data['rakuten_api_library'] = True
          return data

    else:
        print("データの取得に失敗しました。 rakuten")
        return None
    



# VScode用の実行部分
async def main():
    get_data = await fetch_rakuten("9784103549512")
    print("get_data",get_data)

if __name__ == "__main__":
    asyncio.run(main())