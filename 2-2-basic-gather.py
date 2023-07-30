# Wed Jul 26 14:43:47 2023 hello 1 started
# Wed Jul 26 14:43:47 2023 hello 2 started
# Wed Jul 26 14:43:51 2023 hello 1 done
# Wed Jul 26 14:43:51 2023 hello 2 done
# Time: 4.01 sec

# Wed Jul 26 15:10:11 2023 hello 1 started
# Wed Jul 26 15:10:11 2023 hello 2 started
# Wed Jul 26 15:10:15 2023 hello 1 done
# Wed Jul 26 15:10:15 2023 hello 2 done
# Time: 4.01 sec

# เป็นการทำงานเเบบ Asyc เเบบ gather โดยจะทำงาน 2 งาน 

import asyncio
import time

# ฟังก์ชัน hello(i) เป็นหารทำงานเเบบ asynchronous และแสดงข้อความ "hello" พร้อมกับหมายเลขงาน i
async def hello(i):
    print(f"{time.ctime()} hello {i} started")
    await asyncio.sleep(4)
    print(f"{time.ctime()} hello {i} done")

# ฟังก์ชัน main() เป็น asynchronous และใช้ในการสร้างและรัน tasks แบบ asynchronous โดยสร้าง task1 เเละ task 2
async def main():
    task1 = asyncio.create_task(hello(1)) # return immediately, the task is created
    #await asyncio.sleep(3)
    task2 = asyncio.create_task(hello(2))
     # รอให้ทั้ง task1 และ task2 เสร็จสิ้น
    await asyncio.gather(task1, task2)

# รัน main เเละเเสดงเวลางาน
if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'Time: {end-start:.2f} sec')
