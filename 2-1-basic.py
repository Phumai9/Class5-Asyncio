# Wed Jul 26 15:10:02 2023 hello 1 started
# Wed Jul 26 15:10:02 2023 hello 2 started
# Wed Jul 26 15:10:06 2023 hello 1 done
# Wed Jul 26 15:10:06 2023 hello 2 done
# Time: 4.01 sec

import asyncio
import time

# ก็เป็นการทำงานเเบบ Asynchronous โดยเเสดงวันเวลาการทำงาน

# ฟังก์ชัน hello(i) เป็นหารทำงานเเบบ asynchronous และแสดงข้อความ "hello" พร้อมกับหมายเลขงาน i
async def hello(i):
    print(f"{time.ctime()} hello {i} started")
    await asyncio.sleep(4)
    print(f"{time.ctime()} hello {i} done")

# ฟังก์ชัน main() เป็น asynchronous และใช้ในการสร้างและรัน tasks แบบ asynchronous โดยสร้าง task1 เเละ task 2
async def main():
        task1 =asyncio.create_task(hello(1)) #returns immediately, the  task is creasted
        #await astncio.sleep(3)
        task2 =asyncio.create_task(hello(2))
        await task1
        await task2

# รัน main เเละเเสดงเวลางาน
if __name__ == '__main__':
      start = time.time()
      asyncio.run(main())
      end = time.time()
      print(f'Time: {end-start:.2f} sec')