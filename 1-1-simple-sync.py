# 1-1-simple-sync.py

# Task A: Computing 0+1
# Time: 0.00
# Task A: Computing 1+2
# Time: 0.00
# Task A: Sum = 3

# Task B: Computing 0+1
# Time: 0.00
# Task B: Computing 1+2
# Time: 0.00
# Task B: Computing 3+3
# Time: 0.00
# Task B: Sum = 6

# Time: 0.00 sec

# มีการสร้างงานสองชิ้น คือ (task A และ task B) และแสดงผลเวลาที่ใช้ในการทำงานของแต่ละงานและรวมเวลาทั้งหมดที่ใช้ในการทำงานของทั้งสองงานเป็นเเบบ Synchronize

import time

# เเสดงเวลาเริ่มต้นของการทำงานจนเสร็จ
def sleep():
    print(f'Time: {time.time() - start:.2f}')

# เป็นฟังชัน sum ที่คำนวณผลรวมของตัวเลขของ numbers ตามชื่องาน (name) เเละคำนวณผลรวมในแต่ละครั้ง โดยใช้ sleep()ไว้ดูการทำงานของฟังชัน
def sum(name, numbers):
    total = 0
    for number in numbers:
        print(f'Task {name}: Computing {total}+{number}')
        sleep()
        total += number
    # แสดงผลรวมที่ได้
    print(f'Task {name}: Sum = {total}\n')

# บันทึกเวลาเริ่มต้นการทำงาน
start = time.time()

# เรียกใช้ฟังก์ชัน sum() สองครั้งเเละจะทำการคำนวณผลรวมของตัวเลข

task = [
    sum("A", [1, 2]),
    sum("B", [1, 2, 3],)
]

# บันทึกเวลาสิ้นสุดการทำงานเเละเเสดงค่าการทำงานทั้งหมด
end = time.time()
print(f'Time: {end-start:.2f} sec')
