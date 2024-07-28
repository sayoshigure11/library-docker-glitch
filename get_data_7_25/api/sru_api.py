# SRUからデータを取得
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



async def get_book_data_sru(isbn):
    # isbn = "9784479782995"
    url = f"https://ndlsearch.ndl.go.jp/api/sru?operation=searchRetrieve&maximumRecords=10&recordSchema=dcndl&recordPacking=xml&query=dpid=iss-ndl-opac-national%20AND%20isbn%3d{isbn}%20AND%20mediatype%3D%22books%22&onlyBib=true"
    response = requests.get(url)
    response.encoding = 'utf-8'
    parsed_data = await convert_xml_to_json(response.text)

    # print("parsed_data",parsed_data)

    if parsed_data:
        try:
            # # titleへのパスを辿る
            publisher = parsed_data['searchRetrieveResponse']['records']['record']['recordData']['rdf:RDF']['dcndl:BibResource'][0]['dcterms:publisher']['foaf:Agent']['foaf:name']
            # print("Publisher:", publisher)
            sales_date = parsed_data['searchRetrieveResponse']['records']['record']['recordData']['rdf:RDF']['dcndl:BibResource'][0]['dcterms:date']
            # print("Sales Date:", sales_date)
            price = parsed_data['searchRetrieveResponse']['records']['record']['recordData']['rdf:RDF']['dcndl:BibResource'][0]['dcndl:price']
            # print("Price:", price)
            page_count = parsed_data['searchRetrieveResponse']['records']['record']['recordData']['rdf:RDF']['dcndl:BibResource'][0]['dcterms:extent']
            # print("Page Count:", page_count)

            return {
                "sru_data": True,
                "publisher": publisher,
                "sales_date": sales_date,
                "price": price,
                "page_count": page_count,
            }

        except KeyError:
            print("指定されたパスで見つかりません。")
            return {
                "sru_data": False
            }
    else:
        print("データの解析に失敗しました。")
        return {
            "sru_data": False
        }

    # return parsed_data


# コラボラトリー用の実行部分
# data = await get_book_data_sru(True, "9784022650591")
# print(data)


# VScode用の実行部分
async def main():
    get_data = await get_book_data_sru("9784103549512")
    print("get_data",get_data)

if __name__ == "__main__":
    asyncio.run(main())
