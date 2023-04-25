# 비동기 프로그래밍을 위한 라이브러리 : 코루틴 이용
# 코루틴을 시작하는 run()

import asyncio
import random

async def fetch_data():
    print("데이터를 가져오는 중...")
    await asyncio.sleep(1) # 데이터를 가져오는데 1초가 걸린다고 가정
    return random.randint(1, 100)

async def main():
    data = await fetch_data()
    print(f"가져온 데이터: {data}")

asyncio.run(main())