
'''
#####While循环重点练习######

# 1. 让连续循环8次
count = 1
while count <= 8:
    print("123")
    count = count + 1


#2. 让用户尽情喷，按Q退出
while True:
    s = input("你要发表什么：")
    if s == "q":
        break
    if "最" in s:   # 在xxx中出现了关键字（包含关系）
        print("不合规")
        continue    #结束本次循环，继续执行下一次循环
    else:
        print("您喷的内容是："+s)



#3. 计算1+2+3+4....100的和
count = 1
sum = 0
while count <= 100:
    sum = sum + count   把sum中的值（之前的运算结果）和当前数数相加.第1次 0+1；第二次1+2；第三次3+3；第四次6+4....
    count = count + 1 
print(sum)



#4. 输出1 - 100以内的奇数
    ##关键点是不能被2整除的为奇数

count = 1
while count <= 100:
    if count % 2 != 0: #如果不能整出2则为奇数进行打印
        print(count)
    count = count + 1


# 5. while .... else的示例
count = 1
while count <= 10:
    print(count)
    count = count + 1
    if count == 5:
        break # 此步骤为后加的，意在展示当执行到break过程中会立刻跳出程序
else:
    print("这里是else") # while 条件不成立过程中才会执行


# 6. 猜字游戏，只能猜3次
count = 1
while count <= 3:
    s = input("你猜一下：")
    if int(s) > 66:
        print("大了")
    elif int(s) < 66: # 多条件可以用elif，
        print("小了")
    else:
        print("猜对了")
        break
    print("还剩%d次机会了" % (3- count)) # 格式化输出的案列
    count = count + 1
else:
    print("超过3次了")


# 7. 打印123456 8910
count = 1
while count <= 10:
    if count ==7:
        count = 8 # 此处简单暴力的改变了变量的实际值
    print(count)
    count = count +1

# 8. 打印123456 8910
count = 1
while count <= 10:
    if count == 7:
        count = count + 1 # 当count = 7 的时候，添加1，其实和上一种方法相同
    print(count)
    count = count + 1

# 9. 计算1-2+3-4+5-6....+99 的值（此需求的关键点在于"奇数相加，偶数相减"）
count = 1
sum = 0
while count < 100:
    if count % 2 == 0:
        sum = sum - count #第二次条件成立，即：0+1-2
    else:
        sum = sum + count #第一次条件不成立所以执行else即：0 + 1；第三次条件继续不成立所以执行else，即0+1-2+3.......以此类推直到99
    count = count + 1
print(sum)


 # 10. 使用用户名：alex，密码：123登陆，只能登陆3次
count = 1
while count <= 3:
    username = input("键入用户名：")
    password = input("键入密码：")
    if username == "alex" and password == "123":
        print("登陆成功")
        break
    else:
        print("登陆失败")
    print("还剩%d次机会了" % (3-count))
    count = count + 1
else:
    print("蠢")

# 11. 键入广告标语，但是不能出现关键词

ad = input("键入广告标语:")
if "最好" in ad or "第一" in ad: # 关键词只要不连续比如：eeeee最rrrr好就没问题，如果连续了：qqq最好qqq就会自动跳出
    print("不合法")
else:
    print("广告标语是：" + ad)


'''








