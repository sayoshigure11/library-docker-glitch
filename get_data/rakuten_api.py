# def get_rakuten_api(title, author):
  
#   return

# 7/19 試す前用保存
import asyncio
import aiohttp
import urllib.parse


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

async def fetch_rakuten(title, author):
    # キーワードをURLエンコード
    encode_data_title = urllib.parse.quote(title)
    print("encodeData title:", encode_data_title)
    encode_data_author = urllib.parse.quote(author)
    print("encodeData author:", encode_data_author)

    # 楽天ブックスAPIのURL
    url = f"https://app.rakuten.co.jp/services/api/BooksBook/Search/20170404?format=json&title={encode_data_title}&author={encode_data_author}&applicationId={os.getenv('RAKUTEN_API')}"
    print("2秒間待機します...")
    await delay(2000)
    print("待機終了、データ取得を開始します。")

    # タイムアウトを10秒に設定してfetchを実行
    result = await fetch_with_timeout(url, timeout=10)

    if result:
        data = result.get('Items')[0]['Item']
        print("データを取得しました:", data)

        return data
    else:
        print("データの取得に失敗しました。")
        return None



def run_async(coroutine):
  return asyncio.get_event_loop().run_until_complete(coroutine)