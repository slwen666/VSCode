'''
num = input("请输入你的分数：")
num = int(num)
if num  >= 90:
    print("A")
elif num >= 80:
    print("B")
elif num >= 70:
    print("C")
elif num >= 60:
    print("D")
else:
    print("E")

month  = input("请输入月份：")
if month == "一月":
    print("豆包")
if month == "二月":
    print("大雨大肉")
if month == "三月":
    print("竹筒饭")



count = 1
while count <= 8:
    print("111")
    count = count + 1


while True:
    s = input("键入说明信息：")
    if s == "q":
        break
    if "fxxx" in s:
        print("包含非法字符")
        continue
    print("说明信息是" + s)


# 1+2+3+4+5..+100
sum = 0
count = 1
while count <= 100:
    sum = sum + count
    count = count + 1
print(sum)


count = 1
while count <= 100:
    if count % 2 != 0:
        print(count)
    count = count + 1


name = input("请输入你的名字：")
age = input("请输入你的年龄：")
hobby = input("输入你的爱好：")
gender = input("请输入你的性别：")
# print(name + "今年" + age + "岁，是一个老头，爱好是" + hobby + "性别是" + gender)
# %s字符串占位符
print("%s今年%s岁，是一个老头，爱好是%s,性别是%s" % (name,age,hobby,gender))

a = 108
s = "梁山水泊有%d个牛逼的任务" % (a)
print(s)


name = "alex"
print("%s已经喜欢了沙河%%2的女生" % (name))
print("wuse很色，喜欢了昌平%5的女生")

print(2**0)
print(2**1)
print(2**2)
print(2**3)



a = 10
a += 20 # a = a + 20
print(a)

print(3>4 or 4<3  and  1==1)
print(2 > 1  and  3 < 4 or 4 > 5 and  2 < 1)
print(1 > 2  and  3 < 4 or 4 > 5 and  2 > 1  or 9 < 8)
print(1 > 1  and  3 < 4 or 4 > 5 and  2 > 1  and  9 > 8 or 7 < 6)
print(not  2 > 1  and 3 < 4  or 4 > 5  and 2 > 1  and 9 > 8  or 7 < 6) 

print(1 or 2) 
print(2 or 3)  
print(0 or 3) 
print(0 or 4) 

# print(1 1 or 5)    
# print(1 and 2)  # 2
# print(2 and 0)  # 0
# print(0 and 3)  # 0
# print(0 and 4)  # 0


print(0 or 4 and  3 or 7 or 9 and  6)

print(2 < 1 and 4 > 6 or 3 and 4 > 5 or 6)



count = 1
while count  <= 10:
    print(count)
    count = count + 1
    if count == 5:
        break
else:
    print("这里是else")


print(2 > 3 and 3) 


print("我叫%s,今年22岁了,学习Python%%2了" % "王尼玛")




a = 10
b = 20
c = b/a
d = b % a #取余
e = b //a # 取整数
print(c)
print(d)
print(e)

# while 循环，如果通过Break退出，那么While后面的else将不会被执行，只有while条件判断是假的时候才会执行
index = 1
while  index < 11:
    if index == 8:
        break
    print(index)
    index = index + 1
else:
    print("hello")


content = input("请输入内容：")
if "zhangsan" in content or "lisi" in content:
    print("输入的内容不合法")
else:
    print("评论成功")

'''

