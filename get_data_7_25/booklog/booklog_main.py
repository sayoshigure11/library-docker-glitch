import asyncio

# from get_data_7_25.booklog.booklog_ranking import search_booklog_ranking
from .booklog_ranking import search_booklog_ranking

async def main():
    booklog_ranking = [data async for data in search_booklog_ranking()][:20]
    print("booklog_ranking",booklog_ranking)



# コラボラトリー用の実行部分
# await main()



# VScode用の実行部分
if __name__ == "__main__":
    asyncio.run(main())

