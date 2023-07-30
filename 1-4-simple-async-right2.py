# Task A: Computing 0+1
# Time: 0.00
# Task B: Computing 0+1
# Time: 0.00
# Task A: Computing 1+2
# Time: 1.01
# Task B: Computing 1+2
# Time: 1.01
# Task A: Sum = 3

# Task B: Computing 3+3
# Time: 2.03
# Task B: Sum = 6

# Time: 3.04 sec

# มีการสร้างงานสองชิ้น คือ (task A และ task B) และแสดงผลเวลาที่ใช้ในการทำงานของแต่ละงานและรวมเวลาทั้งหมดที่ใช้
# Aysnchronous เเบบ gather ในโค้ดนี้ก็เเสดงผลลัพธ์การทำงานที่เเสดงผลออกมาเป็นลำดับจะเห็นผลลัพทธ์จะเเสดออกมาเเค่ว่างานไหนเสร็จก่อน

import asyncio
import time

# เเสดงเวลาเริ่มต้นของการทำงานจนเสร็จเเละดีเลย์ 1 วิ

async def sleep():
    print(f'Time: {time.time() - start:.2f}')
    await asyncio.sleep(1)

async def sum(name, numbers):
    total = 0
    for number in numbers:
        print(f'Task {name}: Computing {total}+{number}')
        await sleep()
        total += number
    print(f'Task {name}: Sum = {total}\n')

# ฟังก์ชัน main() เป็น asynchronous และใช้ในการรวมและรันฟังก์ชัน sum() พร้อมกัน
async def main():
    await asyncio.gather(sum("A", [1, 2]), sum("B", [1, 2, 3]))

if __name__=='__main__':
    start = time.time()
    # ใช้ asyncio.run() เพื่อรันฟังก์ชัน main() และจัดการเริ่มต้นและสิ้นสุดการทำงานโดยอัตโนมัติ
    asyncio.run(main())
end = time.time()
print(f'Time: {end-start:.2f} sec')