# 长字符串，一般用于程序的说明文档
""" 用python设计的第一个游戏 """
# input用于接受客户的输入，并且返回给temp
temp =  input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
# int(temp) 就可以把temp转换为数字，赋值给guess
guess = int(temp)

if guess == 8:
    print("你是小甲鱼心里的蛔虫吗？！")
    print("哼，猜中了也没奖励！")
else:
    print("猜错啦，小甲鱼现在心里想的是8！")

print("游戏结束，不玩啦")