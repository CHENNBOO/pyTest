# 基本算术运算
x = 10
y = 3

# 加法
print("x + y =", x + y)  # 输出: 13

# 减法
print("x - y =", x - y)  # 输出: 7

# 乘法
print("x * y =", x * y)  # 输出: 30

# 除法（浮点除）
print("x / y =", x / y)  # 输出: 3.333...

# 地板除（整除），如果不是整数，就向下取整。即：取比目标结果小的最大整数
print("x // y =", x // y)  # 输出: 3

print("x // y =", -3 // 2)  # 输出: -2


# 取余
print("x % y =", x % y)  # 输出: 1

# 相反数
print("-x =", -x)  # 输出: -10

# 正号（x本身）
print("+x =", +x)  # 输出: 10

# 绝对值
print("abs(x) =", abs(x))  # 输出: 10
print("abs(-x) =", abs(-x))  # 输出: 10

# 类型转换
print("int(3.9) =", int(3.9))  # 输出: 3
print("float(5) =", float(5))  # 输出: 5.0

# 复数
re = 3
im = 4
c = complex(re, im)
print("complex(re, im) =", c)  # 输出: (3+4j)

# 共轭复数
print("c.conjugate() =", c.conjugate())  # 输出: (3-4j)

# divmod 返回商和余数
print("divmod(x, y) =", divmod(x, y))  # 输出: (3, 1)
# divmod用途，将秒数转换为“小时:分钟:秒”格式：
total_seconds = 3725

minutes, seconds = divmod(total_seconds, 60)
hours, minutes = divmod(minutes, 60)

print(f"{hours}:{minutes:02d}:{seconds:02d}")  # 输出: 1:02:05
# 进制转换
def to_base(n, base):
    digits = "0123456789ABCDEF"
    if n == 0:
        return "0"
    res = []
    while n:
        n, r = divmod(n, base)
        res.append(digits[r])
    return ''.join(reversed(res))

print(to_base(255, 16))  # 输出: FF

# 分页计算
total = 95
page_size = 10

full_pages, last_page_items = divmod(total, page_size)
total_pages = full_pages + (1 if last_page_items else 0)

print(f"总页数: {total_pages}, 最后一页有 {last_page_items or page_size} 条")
# 输出: 总页数: 10, 最后一页有 5 条

# 幂运算
print("pow(x, y) =", pow(x, y))  # 输出: 1000
print("pow(x, y , z) =", pow(2, 3 , 5))  # pow支持第三个参数 2和3幂运算，再拿结果和5取余  2 ** 3 % 5

print("x ** y =", x ** y)  # 输出: 1000