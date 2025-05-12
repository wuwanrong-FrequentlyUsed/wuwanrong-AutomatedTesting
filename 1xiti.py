# name = input("请输入你的姓名：")
# print("你好," + name +"!")

# while 'c':
#     print('ac!')

# i=10
# while i:
#     print('ccc')
#     i=i-1

# DaysPeryear = 365
# HoursPerDay = 24
# MinutesPerHour = 60
# SecondsPerMinute = 60
# OneYear = DaysPeryear * HoursPerDay * MinutesPerHour * SecondsPerMinute
# print(OneYear)

# num = input("请输入1-100之间的数字：")
# guess = int(num)
# if 1 <= guess <= 100:
#     print("你真棒")
# else:
#     print("错啦")

# num = int(input("请输入一个整数："))
# i = 1
# while i <= num:
#     print(i)
#     i = i+1

# num = int(input("请输入一个整数："))
# while num:
#     print(num)
#     num -=1

# num = 8
# while num:
#     print("*",end=" ")
#     num = num -1

# num = int(input("请输入一个整数："))
# while num:
#     i = num -1
#     while i:
#         print(" ",end="")
#         i -=1
#     j = num
#     while j:
#         print("*",end="")
#         j = j-1
#     print()
#     num = num -1

# member = [1,2,3,4]
# member.append(['竹林小溪', 'Crazy迷恋'])
# #member.extend(['竹林小溪', 'Crazy迷恋'])
# print(member)

# name = ['F', 'i', 'h', 'C']
# name.insert(2,'s')
# print(name)

# member = ['小甲鱼', '黑夜', '迷途', '怡静', '秋舞斜阳']
# member.insert(1,88)
# member.append(88)
# member.insert(3,90)
# member.insert(5,85)
# member.insert(7,90)
# print(member)

# member = ['小甲鱼', '黑夜', '迷途', '怡静', '秋舞斜阳']
# member = ['小甲鱼', 88, '黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88]
# print(member)

member = ['小甲鱼', 88, '黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88]
len=len(member)
print(len)
for each in range(len):
    if each%2 ==0:
        print(member[each],member[each+1])

