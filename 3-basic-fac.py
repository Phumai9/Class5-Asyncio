# Computing factorial(2), currently i=2...
# Computing factorial(3), currently i=2...
# Computing factorial(4), currently i=2...
# Computing factorial(3), currently i=3...
# Computing factorial(4), currently i=3...
# Computing factorial(4), currently i=4...
# [2, 6, 24]
# Time: 3.03 sec

import asyncio
import time

# เป็นการทำงานของ factorial ที่ใช้การทำงานเเบบ Asynchronize

# ฟังก์ชัน factorial(n) เป็น asynchronous และคำนวณค่าตัวประกอบของตัวเลข n
async def factorial(n):
    f = 1
    for i in range(2, n + 1):
        print(f"Computing factorial({n}), currently i={i}...")
        await asyncio.sleep(1)
        f *= i
    return f

# ฟังก์ชัน main() เป็น asynchronous และใช้ในการรัน coroutines แบบ asynchronous
async def main():
    # ใช้ asyncio.gather() เพื่อรัน coroutines และรอให้ทุกตัวเสร็จสิ้นแล้วคืนค่ากลับเป็นลิสต์
    L = await asyncio.gather(factorial(2),  factorial(3), factorial(4))
    print(L)    # [2, 6, 24]

# รัน
if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'Time: {end-start:.2f} sec')