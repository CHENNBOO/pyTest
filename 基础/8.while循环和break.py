"""
用Python设计第一个游戏
"""

import random  # 导入随机数模块

# 设置猜测次数
counts = 3

# 生成一个1到10之间的随机整数作为答案
answer = random.randint(1, 10)

# 循环允许用户最多猜3次
while counts > 0:
    # 提示用户输入猜测的数字
    temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
    # 将输入转换为整数
    guess = int(temp)

    # 判断是否猜中
    if guess == answer:
        print("你是小甲鱼心里的蛔虫嘛？！")
        print("哼，猜中了也没奖励！")
        break  # 猜中后退出循环
    else:
        # 如果没猜中，判断大小
        if guess < answer:
            print("小啦~")
        else:
            print("大啦~")
        # 每次猜测后减少一次机会
        counts = counts - 1

# 游戏结束提示
print("游戏结束，不玩啦^_^")