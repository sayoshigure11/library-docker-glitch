# OpenDBからデータを取得
import requests
import json
import asyncio

async def get_book_data_opendb(isbn):
    # isbn = "9784022650591"
    url_opendb = f"https://api.openbd.jp/v1/get?isbn={isbn}&pretty" #OpenDBAPI
    response_opendb = requests.get(url_opendb).json() #情報の取得,json変換

    total_items = response_opendb[0]
    if total_items == None:
        print("Book not found in OpenDB.")
        opendb_fetch = False
        return {
            "opendb_data": False
        }

    # print(total_items)

    publisher = response_opendb[0]['summary']['publisher']
    date = response_opendb[0]['summary']['pubdate']
    if 'ProductSupply' in response_opendb[0]['onix']:
      price = response_opendb[0]['onix']['ProductSupply']['SupplyDetail']['Price'][0]['PriceAmount']
    else:
      price = ""
    opendb_fetch = True

    return {
        "opendb_data": True,
        "publisher": publisher,
        "sales_date": date,
        "price": price,
        "page_count": "",
    }

    # return response_opendb

# isbn = "9784479782995"


# コラボラトリー用の実行部分
# response_opendb = await get_book_data_opendb("404111165")

# print(response_opendb)



# VScode用の実行部分
async def main():
    get_data = await get_book_data_opendb("9784022650591")
    print("get_data",get_data)

if __name__ == "__main__":
    asyncio.run(main())