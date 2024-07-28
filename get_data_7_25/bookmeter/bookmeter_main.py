import asyncio
from .bookmeter_ranking import search_bookmeter_ranking
# from get_data_7_25.bookmeter.bookmeter_ranking import search_bookmeter_ranking


async def main():
    booklog_ranking = [data async for data in search_bookmeter_ranking()][:20]
    print("booklog_ranking",booklog_ranking)




# コラボラトリー用の実行部分
# await main()




# VScode用の実行部分
if __name__ == "__main__":
    asyncio.run(main())
