'''
print("hello word")

print(1+3)
print((1+3)*2)
print((((1+3)*2)-6)*3)

a = 1+3
print(a)


__ = "zhangsan"
_a_b_1 = "lisi"
1_2_3 = "wangwu" #变量不能是纯数字
print(1_2_3)

a = 10
b = 20
b = a  #a = 0,b=10
a = 30 # a = 30 ,b = 10(没有更换过)
print(a) 
print(b)

a = 10
print(a) 
print("a") #有坑，此处打印的是字符串a，而非变量a的值

python 不存在角色的常量，一般所有字母大写为常量

PI = 3.141592665358.....
PI = 3.5 #尽量不要更改
print(PI)


a = 128
print(a)
print(type(a))  #打印变量a的数据类型，此处a为int类型

##凡是用引号引起来的全部为字符串str类型，无论是双引号，单引号，三引号
s = "zhangsan"
print(s)
print(type(s)) # 打印变量s的数据类型，此处s为str类型

c = 'znagjiahui'
print(c)
print(type(c)) # 打印变量c的数据类型，此处c依然为str类型

z = """123
3223
343
3
23
"""
print(z)
print(type(z)) #打印变量z的数据类型，此处z依然为str类型

##请你打印出: 周杰伦说:"昆凌也还不错. 我很欣慰!"
print('周杰伦说:"昆凌也还不错. 我很欣慰!"') #灵活运行引号的类型

print("hello", end="")
print("zhangsan",end="")
print("lisi",end="") # print之后，python解释器会自动添加换行符，如果想连接起来可在文本末尾添加{, end = ""}

print("zhangsan","lisi","wangwu") # 文本连接如果用逗号{,}其实是一个空格


##字符串支持相加和相乘{+ *}，相乘就是重复
s1 = "zhangsan"
s2 = "lisi"
s3 = "wangwu"
s4 = s1 +s2 + s3 #字符串使用加号{+}进行拼接
print(s4)
print("我们村有个大姑娘叫"+s1+",另外一个叫" +s2) ##字符串使用加号{+}进行拼接


s = "考试\n"
print(s*3)  #重复三次，并且自动换行(如果不加\n，则不会自动换行)




## 布尔类型bool，只有True和False两种类型
b = 2 > 1
print(b)
print(type(b)) 

s = input("请输入一个字符：") # 不会用户输入的内容，无论用户输入的str还是int，接受的内容永远是str
print("计算机收到的内容是：",s)
print(type(s))

a = input("请输入一个数字：")
a = int(a) #把用户输入的内容转换成数字int
b = input("请输入第二个数字：")
b = int(b)
print(a+b) #a和b都是int类型


##if / else 条件判断示例

#示例1：
gender = input("请输入你的性别：")
if gender == "男的":  # if语句双等于号{==}标识判断，冒号{:}标明条件
    print("滚蛋")
print("吓死我了") # 如果条件是真(True) 执⾏行行结果1, 然后结果2, 如果条件假(False) 直接结果2




#示例2：
gender = input("你是男的还是女的：")
if gender == "女的":  
    print("请进")
else:
    print("滚蛋")



#示例3：
gender = input("你是男的还是女的：")
if gender == "女的":
    age = int(input("多大年龄了？：")) #年龄超过30不开门
    if age < 30:
        print("请进")
    else:
        print("再见")
else:
    print("滚蛋")



# 输入你兜里的钱
# 如果你的钱大于500块. 和啤酒吃炸鸡. 生活美滋滋
# 如果你兜里的钱 小于500 大于300. 吃个盖浇饭. 生活乐无边
# 如果你都里的前 小于300 大于50. 吃个方便面. 开心
# 如果你兜里的钱 小于50. 今天减肥.

#示例4：
money = input("请输入你兜里的钱：")
money = int(money)
if money > 500:
    print("和啤酒吃炸鸡. 生活美滋滋")
else:
    if money > 300:
        print("吃个盖浇饭. 生活乐无边")
    else:
        if money > 50:
            print("吃个方便面. 开心")
        else:
            print("今天减肥")

#示例5：
money = input("请输入你兜里的钱：")
money = int(money)
if money > 500:
    print("和啤酒吃炸鸡. 生活美滋滋")
elif money > 300:
    print("吃个盖浇饭. 生活乐无边")
elif money > 50:
    print(" 吃个方便面. 开心")
else:
    print("今天减肥")


a = 10
b = 3
print(a/b) #常规除法
print(a//b) #取整数
print(a%b) #取余数

# 随机输入一个数字，演示是否是3的倍数
num = input("请输入一个数字：")
num = int(num)
if num % 3 == 0:
    print("是三的倍数")
else:
    print("不是三的倍数")

'''


