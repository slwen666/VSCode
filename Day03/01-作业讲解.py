
#####昨日作业讲解########


'''
#猜字游戏 - if/else语句
n = 66
num = input("你猜一下大小：")
if int(num) > 66:
    print("大了")
elif int(num) < 66:
    print("小了")
else:
    print("正确")


#猜字游戏 - where循环
n = 66
while True:
    num = input("你猜一下大小：")
    if int(num) > 66:
        print("大了")
    elif int(num) < 66:
        print("小了")
    else:
        print("正确")
        break

#猜字游戏 - where循环,只能猜3次
n = 66
count = 1
while count <= 3:
    num = input("你猜一下大小：")
    if int(num) > 66:
        print("大了")
    elif int(num) < 66:
        print("小了")
    else:
        print("正确")
        break
    print("你已经猜了%d次了" % count)
    count = count + 1
else:
    print("太笨了")


#1234568910 - 方法1

count = 1
while count <= 10:
    if count != 7:
        print(count)
    count = count + 1


#1234568910 - 方法2

count = 1
while count <= 10:
    if count == 7:
        count = count + 1 #如果不加此条件，执行到7的时候，会一直卡在7上，程序永远跳不出来
        continue
    print(count)
    count = count + 1

#1234568910 - 方法3

count = 1
while count <= 10:
    if count == 7:
        count = 8
    print(count)
    count = count + 1

# 求1 -100的所有数的和
count = 1
sum = 0
while count <= 100:
    sum = sum + count # 关键是此步，翻译过来就是0+1，下一次是0+1+2....最后加到100的时候，打印sum
    count = count + 1
print(sum)

# 求1 -100以内所有的奇数
count = 1
while count <= 100:
    if count % 2 != 0:
        print(count)
    count = count + 1



# 求1 -100以内所有的奇数
count = 1
while count <= 100:
    if count % 2 == 0:
        print(count)
    count = count + 1

#求1-2+3-4+5-6....99的和 （这道题的关键是“奇数相加，偶数相减”）

sum = 0
count = 1
while count <= 99:
    if count %2 ==0: #偶数相剑
        sum = sum - count
    else:
        sum = sum + count #奇数相加
    count = count + 1
print(sum)

#用户登陆（三次输错机会）且每次错误时显示剩余错误次数，要求使用字符串格式化
count = 1
while count <= 3:
    username = input("请输入用户名：")
    password = input("请输入密码：")
    if username == "zhangsan" and password == "123":
        print("登陆成功")
        break
    else:
        print("登陆失败，还剩%d次机会" % (3-count)) #使用格式化输入，注意中/英文字符和表单符号
    count = count + 1
else:
    print("今日已没有登陆机会")


# 输入广告标语，不能包含关键词“第一”、“稀缺”、“国家级”等字眼
ad = input("请输入广告词：")
if "第一" in ad or "稀缺" in ad or "国家级" in ad:
    print("你输入的内容不合法") 
else:
    print("合法")



'''

