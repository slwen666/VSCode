###########作业讲解########
'''
# 1. 输出name变量中，e所在索引的位置
name = "   aleX leNb   "

# a 方法一
e1 = name.find("e",0,6)
print(e1)
e2 = name.find("e",6)
print(e2)

# b 方法二
#基本思路：使用while循环，遍历循环字符串的长度，循环过程中，如果匹配到目标值，则打印对应的索引
count = 0 # 定义变量，此变量的值一定为0，因为索引的下标是自0开始。
while count < len(name): #定义循环条件，如果变量的值小于name的字符串长度，则执行循环。
    if name[count] == "e": # 遍历循环索引，如果值输出的值等于e，则打印所属索引
        print(count) # 打印索引
    count = count + 1



# 2. 仅将name变量中首字母变成大写
#a. 方法1   基本思路：使用切片功能，第一步切出首字母，第二步切出除了首字母之后的位置；将首字母使用.upper()参数转换成大写+首字母之后的内容
name = "alaX leNb"
s1 = name[:1]
s2 = name[1:]
print(s1.upper()+s2)

#b. 方法2   基本思路：使用.replace()替换第一个a
s3 = name.replace("a","A",1)
print(s3)


# 3. 使用for循环遍历每一个字符
s = "asdsds2323"
for c in s:
    print(c)

# 4. 使用for循环，但是每次打印都是变量的本身（非遍历）
s = "asdsds2323"
for c in s: #循环的次数 = 变量中字符串的长度
    print(s)


# 5. 使用for循环，但是输出的内容前面加上sb
s = "asdsds2323"
for c in s:
    print("sb" + c)


# 6. 使用for循环，对s = "321",打印的内容是"倒计时3秒"、"倒计时2秒"、"倒计时1秒"，出发
#基本思路：此处涉及到for循环，以及格式化输出的用法
s = "321"
for c in s:
    print("倒计时%s秒" % c)
else:
    print("出发")

# 7. 实现一个整数加法计算器，例如：5+9、5  +9等
#基本思路：
#   使用切割方法，也就是.split()参数，将输入的内容以+切开，由于切出的格式是列表<class 'list'>，列表里面装的是字符串
#   使用索引确认用户输入的内容是什么
#   将字符串转换为数字，之后再进行相加
content = input("请输入内容:")
lst = content.split("+") # 使用切割功能，将输入的内容以+隔开，切割之后是列表，列表里面是字符串
s1 = lst[0] # 使用索引功能，确认下标为0的字符串是什么，也就是确认第1个字符是什么。
s2 = lst[1] #  使用索引功能，确认下标为1的字符串是什么，也就是确认第2个字符是什么。
a1 = int(s1) # 将字符串转换成数字
a2 = int(s2) # 
print(a1+a2) # 数字相加




# 8. 计算用户输入的内容中包含多少整数。例如：andndndijiif123232dfd
#基本思路：
#   首先：使用.isdigit()参数，在for循环中输入的内容中包含的整数
#   其次，在循环中每次循环到一个，则记录一个，最后打印
content = input("请输入内容:")
count = 0
for c in content:
    if c.isdigit():
        count = count + 1
print(count)


# 9. （升级题）计算用户输入的内容中包含多少组连续的数字

# 10. 使用while循环完成下列需求
while 1:
    lu = input("请输入ABC:").strip().upper() # 去掉空格和特殊字符，转换为大写
    if lu =="A":
        content = input("请选择公交车还是步行:")
        if content == "公交车":
            print("10分钟到家")
            break
        if content == "步行":
            print("20分钟到家")
            break
        else:
            print ("我也不知道怎么办")
    elif lu == "B":
        print("走小路回家")
        break
    elif lu == "C":
        print("绕路回家")
        content = input("去哪浪了？")
        if count == "网吧":
            print("准备接受母亲的殴打")
        else:
            print("准备接受父亲的殴打")
    else:
        print("你是不是啥")




# 11. 计算1-2+3-4.....99中除了 88以外所有书的总和
#基本思路
#   奇数相加，偶数相减
#   当循环的数字是88时候，自动加1变成89，然后继续循环
count = 1
sum = 0
while count < 100:
    if count == 88:
        count = count + 1
        continue
    if count % 2 == 0:
        sum = sum - count
    else:
        sum = sum + count
    count = count + 1
print(sum)

# 12. 判断一句话是否为回文，例如：上海自来水来着海上
#基本思路：
#   使用"步长"的功能，将原文倒序输出，然后再使用if判断是否一直。
s = "上海自来水来自海上"
s1 = s[::-1]
if s == s1:
    print("是回文")
else:
    print("不是回文")

# 13. 输入一个字符串，判断字符串中大写字母、小写字母、数字、其它字符，共计出现多少次，并输出出来
#基本思路：
#   首先，分别定义数字、大写字母、小写字母、其它（特殊字符）的变量，用于之后的计数
#   其次，使用for循环，读取用户输入的每一个字符，使用if语句判断每个字符的类型，匹配一个就添加到上一步的变量中
#   最后，将每种类型的变量打印出来
#这里引入的几个关键参数为：
#   .isdigit():判断是否为数字
#   .isupper():判断是否为大写字母（如果仅是.upper()代表全部转换为大写）
#   .islower():判断是否为小写字母（如果仅是.lower()代表全部转换为大写）
content = input("请输入一个字符")
digit_num = 0
upper_c_num = 0
lower_c_num = 0
other = 0
for c in content:
    if c.isdigit():
        digit_num +=1 # diagit_num = digit_num + 1
    elif c.isupper():
        upper_c_num += 1
    elif c.islower():
        lower_c_num +=1
    else:
        other += 1
print(digit_num)
print(upper_c_num)
print(lower_c_num)
print(other)

# 14. 制作趣味模板程序，等待用户输入名称、地点、爱好，并进行任意显示，例如：敬爱可爱的xxx，最喜欢在xxx，干xxxx
#基本思路：
#   主要考查是格式化输出，此处可以用.format()参数来实现
name = input("请输入你的名字")
address = input("请输入你的地址")
hobby = input("请输入你的爱好")
print("{name}家住在{address}，他的爱好是{hobby}".format(name=name,address=address,hobby=hobby))
print("%s家住在%s,他的爱好是%s" % (name,address,hobby)) # 之前学的方法


# 15. 每次循环，逐个字符累加
#基本思路
#   使用for循环遍历每一个字符
#   定义一个变量，此处为SS，将每一次遍历的结果都与之前的累加，最后打印ss
s = "逐个字符累加"
ss = ""
for c in s:
    ss = ss + c
    print(ss)

'''





