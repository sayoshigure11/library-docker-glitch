# OpenSearchからデータを取得
import xmltodict
import json
import requests
import asyncio

async def convert_xml_to_json(xml_str):
    try:
        dict = xmltodict.parse(xml_str)
        return dict  # 直接ディクショナリを返す
    except Exception as e:
        print("XMLの解析エラー", e)
        return None


async def get_book_data_opensearch(isbn):
    # isbn = "4575247537"
    url_opensearch = f"https://ndlsearch.ndl.go.jp/api/opensearch?isbn={isbn}"
    response_opensearch = requests.get(url_opensearch)
    response_opensearch.encoding = 'utf-8'
    parsed_data_opensearch = await convert_xml_to_json(response_opensearch.text)


    if parsed_data_opensearch:
        try:
            rss = parsed_data_opensearch['rss']
            channel = rss['channel']
            item = channel['item']
            item_length = len(item)
            # print("item_length:", item_length)
            # print(parsed_data_opensearch['rss']['channel']['item'])

            if item_length == 2:
              publisher = parsed_data_opensearch['rss']['channel']['item'][item_length - 1]['dc:publisher']
              # print("Publisher:", publisher)
              price = parsed_data_opensearch['rss']['channel']['item'][item_length - 1]['dcndl:price']
              # print("Price:", price)
              page_count = parsed_data_opensearch['rss']['channel']['item'][item_length - 1]['dc:extent']
              # print("Page Count:", page_count)
              if 'dcterms:issued' in parsed_data_opensearch['rss']['channel']['item'][item_length - 1]:
                date = parsed_data_opensearch['rss']['channel']['item'][item_length - 1]['dcterms:issued']
                # print("Date:dcterms:issued:", date)
              else:
                date = parsed_data_opensearch['rss']['channel']['item'][item_length - 1]['dc:description']
              # print("Date:description:", date)

            elif item_length > 10:
              if 'dcterms:issued' in parsed_data_opensearch['rss']['channel']['item']:
                date = parsed_data_opensearch['rss']['channel']['item']['dcterms:issued']
                # print("Date:dcterms:issued:", date)
              else:
                date = parsed_data_opensearch['rss']['channel']['item']['dc:description']
                if date == None:
                   date = None
                if date != None:
                  if len(date) >1:
                    date = date[len(date) - 1]
                  # print("Date:description:", date)

              if 'dc:publisher' in parsed_data_opensearch['rss']['channel']['item']:
                publisher = parsed_data_opensearch['rss']['channel']['item']['dc:publisher']
                if len(publisher) >1:
                  publisher = publisher[len(publisher) - 1]
                # print("Publisher:", publisher)
              else:
                publisher = ""
                # print("Publisher:", publisher)

              if 'dcndl:price' in parsed_data_opensearch['rss']['channel']['item']:
                price = parsed_data_opensearch['rss']['channel']['item']['dcndl:price']
                # print("Price:", price)
              else:
                price = 0
                # print("Price:", price)

              if 'dc:extent' in parsed_data_opensearch['rss']['channel']['item']:
                page_count = parsed_data_opensearch['rss']['channel']['item']['dc:extent']
                # print("Page Count:", page_count)
              else:
                page_count = ""
                # print("Page Count:", page_count)

            else:
              publisher = parsed_data_opensearch['rss']['channel']['item']['dc:publisher']
              # print("Publisher:", publisher)
              price = ""
              page_count = ""
              date = parsed_data_opensearch['rss']['channel']['item']['dcterms:issued']
              # print("Date:", date)

            return {
                "opensearch_data": True,
                "publisher": publisher,
                "price": price,
                "page_count": page_count,
                "sales_date": date,
            }
        except KeyError:
            print("指定されたパスが見つかりません[open_search]")
            return {
                "opensearch_data": False
            }
    else:
        print("データの解析に失敗しました。[open_search]")
        return {
            "opensearch_data": False
        }

    # return parsed_data_opensearch



# コラボラトリー用の実行部分
# get_data_opensearch = await get_book_data_opensearch("404114728")
# print(get_data_opensearch)



# VScode用の実行部分
async def main():
    get_data = await get_book_data_opensearch("9784103549512")
    print("get_data",get_data)

if __name__ == "__main__":
    asyncio.run(main())