# BIF == Built-in function 内置函数，方便程序员快速调用。小写的为bif内置函数
# ==判断是否相等，=赋值
import random
print("----游戏----")
# 字符串
temp = input("数字: ")
# 转换为整型
guess = int(temp)
i = 2
while guess != 8 and i:
    # 字符串
    temp = input("请再次输入你猜的数字: ")
    # 转换为整型
    guess = int(temp)
    if guess == 8:
        print("猜对啦")
        # print("没有奖励")
    else:
        if guess < 8:
            print("猜小了")
        else:
            print("猜大了")
    i = i-1
print("游戏结束啦")




