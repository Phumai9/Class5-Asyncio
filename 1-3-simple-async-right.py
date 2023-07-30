# Task A: Computing 0+1
# Time: 0.00
# Task B: Computing 0+1
# Time: 0.00
# Task A: Computing 1+2
# Time: 1.01
# Task B: Computing 1+2
# Time: 1.01
# Task A: Sum = 3

# Task B: Computing 3+2
# Time: 2.03
# Task B: Sum = 5

# Time:3.04 sec

# มีการสร้างงานสองชิ้น คือ (task A และ task B) และแสดงผลเวลาที่ใช้ในการทำงานของแต่ละงานและรวมเวลาทั้งหมดที่ใช้ในการทำงานของทั้งสองงานเป็นเเบบ Asynchronize 
# โดยจะทำงานในงานอื่นโดยไม่ต้องรอเวลาเเต่เปลี่ยนจำนวนงานต่างจากข้อที่เเล้ว โดยงานสุดท้ายจะเสร้จหลังจาก A เสร็จไปเเล้ว

# เเสดงเวลาเริ่มต้นของการทำงานจนเสร็จเเละดีเลย์ 1 วิ
import asyncio
import time
async def sleep():
    print(f'Time: {time.time() - start:.2f}')
    await asyncio.sleep(1)

# ใช่ฟังก์ชัน sum() เป็นเเบบ asynchronous และคำนวณผลรวมของการทำงาน
async def sum(name, numbers):
    total = 0
    for number in numbers:
        print(f'Task {name}: Computing {total}+{number}')
        await sleep()
        total += number
    print(f'Task {name}: Sum = {total}\n')

start = time.time()

# สร้าง tasks เพื่อทำการเรียกใช้ฟังก์ชัน sum() แบบ asynchronous
loop = asyncio.get_event_loop()
tasks = [loop.create_task(sum("A", [1, 2])),
        loop.create_task(sum("B", [1, 2, 2])),
]

# รัน tasks แบบ asynchronous และรอให้ทำงานเสร็จ
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

end = time.time()
print(f'Time:{end-start:.2f} sec')