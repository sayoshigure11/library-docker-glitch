import asyncio
from .bookoff_ranking import search_bookoff_ranking


async def main():
    bookoff_ranking = [data async for data in search_bookoff_ranking()][:20]
    print(bookoff_ranking)


# コラボラトリー用の実行部分
# await main()


# VScode用の実行部分
if __name__ == "__main__":
    asyncio.run(main())