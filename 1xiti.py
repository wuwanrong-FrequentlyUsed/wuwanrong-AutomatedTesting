name = input("请输入你的姓名：")
print("你好," + name)


num = input("请输入1-100之间的数字：")
guess = int(num)
if 0 <= guess <= 100:
    print("你真棒")
else:
    print("错啦")
