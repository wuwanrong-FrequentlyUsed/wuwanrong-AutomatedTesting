# BIF == Built-in function 内置函数，方便程序员快速调用。小写的为bif内置函数
# ==判断是否相等，=赋值
print("----游戏----")
# 字符串
temp = input("数字: ")
# 转换为整型
guess = int(temp)
while guess != 8:
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
print("游戏结束啦")




