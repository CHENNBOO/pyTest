"""
python特殊写法

is 用于判断是否是同一个对象（也就是内存地址）
is not：判断两个对象的 id(内存地址) 是否不相等
is 和 is not 都是比是否是同一个对象的，不是一个对象就false

== 用于判断是否是同一个值，不同的对象，只要内容一样，就是true
"""

# Python 比较运算符（关系运算符）示例
# 用于比较两个值或对象，并返回布尔值 True 或 False

# 1. 小于 (<)：判断左边是否小于右边
a = 3
b = 5
print(a < b)        # 输出: True   （因为 3 < 5）
print(b < a)        # 输出: False  （因为 5 不小于 3）

# 2. 小于等于 (<=)：判断左边是否小于或等于右边
print(a <= b)       # 输出: True   （因为 3 <= 5）
print(b <= a)       # 输出: False  （因为 5 不小于等于 3）
print(a <= a)       # 输出: True   （因为 3 == 3）

# 3. 大于 (>)：判断左边是否大于右边
print(a > b)        # 输出: False  （因为 3 不大于 5）
print(b > a)        # 输出: True   （因为 5 > 3）

# 4. 大于等于 (>=)：判断左边是否大于或等于右边
print(a >= b)       # 输出: False  （因为 3 不大于等于 5）
print(b >= a)       # 输出: True   （因为 5 >= 3）
print(a >= a)       # 输出: True   （因为 3 == 3）

# 5. 等于 (==)：判断左右两边是否相等（值相等）
x = 10
y = 10
print(x == y)       # 输出: True   （值相同）
z = "hello"
w = "hello"
print(z == w)       # 输出: True   （字符串内容相同）

# 6. 不等于 (!=)：判断左右两边是否不相等
print(x != y)       # 输出: False  （因为 x == y）
print(x != z)       # 输出: True   （整数和字符串不同）


# 7. is：判断两个对象的 id 是否相等（即是否是同一个对象）
# 注意：is 比较的是对象的身份（内存地址），不是值
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 == list2)  # 输出: True  （值相等）
print(list1 is list2)  # 输出: False （是两个不同的列表对象）

# 8. is not：判断两个对象的 id 是否不相等
print(list1 is not list2)  # 输出: True （不是同一个对象）

# 特殊情况：None 和常量
none_var = None
print(none_var is None)      # 输出: True   （推荐用 is 判断 None）
print(none_var == None)      # 输出: True   （但不推荐，因为可能被重载）

# 注意：is 和 == 的区别
# - == 比较值（value）
# - is 比较对象身份（identity，即内存地址）

# 示例：数字小整数缓存（Python 会缓存 -5 到 256 的整数）
a = 100
b = 100
print(a is b)           # 输出: True （因为小整数会被缓存为同一个对象）

c = 1000
d = 1000
print(c is d)           # 输出: False （大整数不会缓存，是不同对象）
print(c == d)           # 输出: True  （值相等）