import asyncio
import time

# Task A: Computing 0+0
# Time: 0.00
# Task A: Computing 1+1
# Time: 1.00
# Task A: Sum = 3

# Task B: Computing 0+0
# Time: 2.01
# Task B: Computing 1+1
# Time: 3.01
# Task B: Computing 3+3
# Time: 4.01
# Task B: Sum = 6

# Time: 5.01 sec

# มีการสร้างงานสองชิ้น คือ (task A และ task B) และแสดงผลเวลาที่ใช้ในการทำงานของแต่ละงานและรวมเวลาทั้งหมดที่ใช้ในการทำงานของทั้งสองงานเป็นเเบบ Asynchronize 
# โดยจะทำงานในงานอื่นโดยไม่ต้องรอเวลา


# เเสดงเวลาเริ่มต้นของการทำงานจนเสร็จเเละดีเลย์ 1 วิ
async def sleep():
    print(f'Time: {time.time() - start:.2f}')
    time.sleep(1)

# ใช่ฟังก์ชัน sum() เป็นเเบบ asynchronous และคำนวณผลรวมของการทำงาน
async def sum(name, numbers):
    total = 0
    for number in numbers:
        print(f'Task {name}: Computing {total}+{total}')
        await sleep() # ใช้ await เพื่อรอฟังก์ชัน sleep() เสร็จสิ้นก่อนทำงานในรอบถัดไป เเต่จะไม่กระทบงานอื่นๆ
        total += number
    print(f'Task {name}: Sum = {total}\n')

start = time.time()

# สร้าง tasks เพื่อทำการเรียกใช้ฟังก์ชัน sum() แบบ asynchronous
loop = asyncio.get_event_loop()
tasks = [loop.create_task(sum("A", [1, 2])),
         loop.create_task(sum("B", [1, 2, 3]))
]

# รัน tasks แบบ asynchronous และรอให้ทำงานเสร็จ
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

end = time.time()
print(f'Time: {end-start:.2f} sec')