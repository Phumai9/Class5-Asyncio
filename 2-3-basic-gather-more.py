# Wed Jul 26 15:10:22 2023hello0started
# Wed Jul 26 15:10:22 2023hello1started
# Wed Jul 26 15:10:22 2023hello2started
# Wed Jul 26 15:10:22 2023hello3started
# Wed Jul 26 15:10:22 2023hello4started
# Wed Jul 26 15:10:22 2023hello5started
# Wed Jul 26 15:10:22 2023hello6started
# Wed Jul 26 15:10:22 2023hello7started
# Wed Jul 26 15:10:22 2023hello8started
# Wed Jul 26 15:10:22 2023hello9started
# Wed Jul 26 15:10:26 2023hello0done
# Wed Jul 26 15:10:26 2023hello2done
# Wed Jul 26 15:10:26 2023hello6done
# Wed Jul 26 15:10:26 2023hello9done
# Wed Jul 26 15:10:26 2023hello8done
# Wed Jul 26 15:10:26 2023hello5done
# Wed Jul 26 15:10:26 2023hello7done
# Wed Jul 26 15:10:26 2023hello4done
# Wed Jul 26 15:10:26 2023hello1done
# Wed Jul 26 15:10:26 2023hello3done
# Time:4.02sec

import asyncio
import time

# ฟังก์ชัน hello(i) เป็นหารทำงานเเบบ asynchronous และแสดงข้อความ "hello" พร้อมกับหมายเลขงาน i
async def hello(i):
    print(f"{time.ctime()}hello{i}started")
    await asyncio.sleep(4)
    print(f"{time.ctime()}hello{i}done")

# ฟังก์ชัน main() เป็น asynchronous และใช้ในการสร้างและรัน coroutines แบบ asynchronous
async def main():
    # รัน coroutines แบบ asynchronous พร้อมกันและรอให้ทุกตัวเสร็จ
    coros = [hello(i)for i in range(10)]
    await asyncio.gather(*coros)

# รัน main เเละเเสดงเวลางาน
if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())   
    end = time.time()
    print(f'Time:{end-start:.2f}sec')