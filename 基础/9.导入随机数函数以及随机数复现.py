import random

# 生成一些随机数
print("第一次生成：")
for _ in range(5):
    print(random.randint(1, 10))

# 保存状态
state = random.getstate()

# 再生成一些随机数
print("\n中间插入其他操作...")
for _ in range(3):
    print(random.randint(1, 10))

# 恢复状态
random.setstate(state)

# 再次生成，结果与第一次相同
print("\n恢复后再次生成：")
for _ in range(5):
    print(random.randint(1, 10))