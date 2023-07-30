# Task A: Computer 0+1
# Time: 0.00
# Task B: Computer 0+1
# Time: 0.00
# Task A: Computer 1+2
# Time: 1.00
# Task B: Computer 1+2
# Time: 1.00
# Task A:Sum = 3

# Task B: Computer 3+3
# Time: 2.00
# Task B:Sum = 6

# Time: 3.00 sec

import asyncio
import time 
from concurrent.futures.thread import ThreadPoolExecutor

# เเสดงเวลาเริ่มต้นของการทำงานจนเสร็จเเละดีเลย์ 1 วิ

def sleep():
    print(f'Time: {time.time() - start:.2f}')
    time.sleep(1)

async def sum(name, numbers):
    _executor = ThreadPoolExecutor(2)
    total = 0 
    for number in numbers:
        # สร้าง ThreadPoolExecutor ในการจัดการเส้นทางสองเส้นที่ใช้ในการดีเลย์
        print(f'Task {name}: Computer {total}+{number}')
        # ใช้ loop.run_in_executor() เพื่อรันฟังก์ชัน sleep() ใน thread ที่แยกกัน
        # ทำให้เกิดการดีเลย์ 1 วินาทีในแต่ละการทำงาน
        await loop.run_in_executor(_executor, sleep)
        total += number
    print(f'Task {name}:Sum = {total}\n')

start =time.time()


# สร้าง tasks เพื่อทำการเรียกใช้ฟังก์ชัน sum() แบบ asynchronous
loop = asyncio.get_event_loop()
task = [
        loop.create_task(sum("A", [1,2])),
        loop.create_task(sum("B", [1,2,3])),
]

# รัน tasks แบบ asynchronous และรอให้ทำงานเสร็จสิ้น
loop.run_until_complete(asyncio.wait(task))
loop.close

end= time.time()
print(f'Time: {end-start:.2f} sec')