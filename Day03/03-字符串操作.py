'''

####字字符串相关的操作####

#capitalize()   首字母大写
s = "alex and wusir and taibai"
s1 = s.capitalize() 
print(s) #原字符串不变
print(s1)


# upper() 和  lower()   大小写转换，全部转换成大写或者小写，在程序判断不区分大小写过程中会用到
s = "Alex is not a Good Man"
print(s.upper()) # 全部转换成大写
print(s.lower()) # 全部转换成小写

while True:
    content = input("请开始喷:")
    if content.upper() == "Q": # 无论用户输入的是否为大Q还是小q，此处都会转换成大Q
        break
    print("你喷了:"content)


#大小写相互转换
s = "ZhangSan lisi WanGwu"
print(s.swapcase()) # 输出的内容是：zHANGsAN LISI wANgWU



#title()    每个单词的首字母大写，输出为：Al麻花腾Ex And Wu Sir Sir Se
s = "al麻花腾ex and wu sir sir se"
print(s.title()) 


#center()   将字符居中，不足的以*代替，代替为9个字符，输出为：***麻花疼***
s = "麻花疼"
print(s.center(9,"*"))


#strip()    去掉空格或者特殊字符，但是去掉的永远是左右两边的内容，而非中间的内容
username = input("用户名：").strip() #去掉空格,去掉是左右两边的空格，中间的不管
password = input("密码：").strip()
if username == "zhangsan" and password == "pass01!":
    print("登陆成功")
else:
    print("登陆失败")




s = "***呵呵**呵呵*****"
print(s.strip("*")) #去掉*，但是去掉的也仅仅是两边的*


#replace（）    内容替换，使用特定内容替换原来的内容
s = "alex wusir alex sb taibai"
s1 = s.replace("alex","小雪") #使用原字符串不变。使用"小雪"替换"alex"
print(s1)
s2 = s.replace(" ","") #去掉上述字符串中所有的空格
print(s2)
s3 = s.replace("alex", "sb", 2) # 用"sb"替换"alex"，但是只替换前2个（容易陷入误区，此处和索引和字符串长度没有关系）
print(s3)

# split()   切割    要切什么，就在括号里面指明
s = "alex_wuse_taibai_bubai"
lst = s.split("_taibai_") #切出的格式是列表<class 'list'>，列表里面装的是字符串，此处切出的内容是['alex_wuse', 'bubai']
print(lst)
print(type(lst))


#格式化输出-01
s = "我叫{}，我今年{}岁了，我喜欢{}".format("zhangsan",18,"lisi") #默认从左往右
print(s)

#格式化输出-02
s = "我叫{1}，今年{0}岁，我喜欢{2}".format("sylar",18,"周杰伦的老婆") # 可以指定位置0、1、2
print(s)

#格式化输出
s = "我叫{name},今年{age},我喜欢{mingxing}".format(name="zhangsan",mingxing="汪峰的老婆",age=18) #定义别名并引用
print(s)




#find() 字符串查询检索,从0开始检索，找不到则返回-1,输出的是索引位置
s = "汪峰的老婆不爱汪峰"
print(s.find("老")) # 计算xxx字符串在原字符串中的位置，查找方式："汪""峰""的""老"；返回值：3
print(s.find("老婆")) # 计算xxx字符串在原字符串中的位置，；查找方式："汪峰""峰的""的老""老婆"；返回值：3
print(s.find("老婆不"))  #   计算xxx字符串在原字符串中的位置；查找方式："汪峰的""峰的老""的老婆""老婆不"；返回值：3
print(s.find("国际章"))  #   计算xxx字符串在原字符串中的位置；查不到返回值：-1
print(s.find("汪峰"))  #   计算xxx字符串在原字符串中的位置；找到了之后会立刻返回，不会向后查询，返回值：0
print(s.find("汪峰",3))  # 计算xxx字符串在原字符串中的位置；自第3个字符往后找，一直到最后，查找方式："0-汪""1-峰""2-的""3-老"""4-婆不""5-不爱""6-爱汪""7-汪峰"；返回值：7

#index()
print(s.index("国际章"))  # 对比之下，find如果没有查到会返回-1.而index中的内容如果不存在，则直接报错


#条件判断，判断字符串的组成格式-01
s = "123abc"
print(s.isdigit()) # 判断字符串是否由数字组成（非包含）
print(s.isalpha()) # 判断是由由字母组成（非包含）
print(s.isalnum()) #判断是是否由数字和字母组成

#条件判断，判断字符串的组成格式-02
s = "二千136万萬"
print(s.isnumeric()) # 判断是否包含数字，数字包含123、一二三、壹贰叁、千萬


#求字符串的长度-01（字符串的长度是1、2、3....而索引是0、1、2、3.....）
s = "你今天喝酒了么密码"
i = len(s) #判断字符串的长度。  print()   input()     len() python的内置函数
print(i) 
#求字符串长度-02
i = s.__len__() # 也可以求长度，len()实际执行的就是这个,__为双下划线
print(i)

len

#把字符串从头到尾遍历！！！！两种方式都要会写！！！！必须要会
s = "晓雪老师.你好漂"
print (len(s))  # 长度是８(长度是从1开始数)　；索引到7（索引是从0开始）
# 1、使用while循环来进行遍历
count = 0 # 定义一个变量从0开始，因为索引的第一位位是0
while count < s.__len__(): # 条件：如果索引的字符小于此字符串的长度
    print(s[count]) # 执行打印当前个索引的对应的字符
    count = count + 1 # 将索引每次循环都加1


# 2、用fot循环来遍历字符串
#优势：简单；劣势：没有索引
#语法：for 变量 in 可迭代对象：# 可迭代对象代表：可一个一个拿的对象，例如：字符串、列表
         循环体

for c in s: #c为新指定的变量，此语法为：把s中的每一个字符串交给c    循环输出
    print(c)


补充：
for循环中也有else，此处为循环完之后会出行（While中的else是条件不成立时执行），但都有一个共性就是while中出现break都会跳出循环
语法：
for 变量 in 可迭代对象：
    循环体
else：
    代码块

''' 





