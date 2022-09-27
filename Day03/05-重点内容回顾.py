'''
########第三章节重点知识回顾#########

####求二进制长度####
a = 3
print(a.bit_length())



####数据类型转换####
#1. 数据类型转换 - 字符串转换成数字
s = "128"
print(type(s)) 
i = int(s)
print(type(i)) # 转换成数字
ss = str(i)
print(type(ss)) # 再转换成字符串

# 2. 数据类型转换 - bool转换成数字（True：1 False：0）
b = False
c = int(b)
print(c) # 输出的结果是 0
print(type(c))

# 3. 数据类型转换 - int类型转换成bool（零：False 非零：True）
a = 0
b = bool(a)
print(type(b))

# 4. 数据类型转换 - 非零等同于True
while 1: # 等同于 True，但是效率比True高一点点，因为计算机只认0和1
    print("123")

# 5. 数据类型转换 - 空的字符串也表示False，非空字符串标识True
s = ""
if s:
    print("123")
else:
    print("456")


# 6. 数据类型转换 - 空的东西都是False，非空的都是True
m = None # 空 连空气都不是  真空 代表False
if m:
    print("789")
else:
    print("8910")

#####数据类型转换过程中小结#########
#1. 综上可以得出. 你想转换成什么就用什么把目标括起来
#2. 字符串可以转数字；数字可以转换成字符串
#3. bool可以转换成数字，数字可以转换成bool 
#4. 只要是代表空的东西都是False，非空的都是True（True: 1  False:0）（零: False 非零: True）（"" 空字符串表示False, 非空字符串表示:True）



####索引####
s = "今天是个好日子"
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])
print(s[5])
print(s[6])
print(type(s[0])) #通过索引获取到的内容还是字符串


####切片####
s = "zhangsan和lisi是好朋友"
s1 = s[5:10] # 与索引起始位置一样，同样是自左往右从0开始，但是结束位置为前一位，取出的值为"san和l"
print(s1)

s2 = s[0:4] + s[5:10] # 可以拼接
print(s2)

s3 = s[5:] # 默认直接到结尾
print(s3)

s4 = s[:5] # 默认从0开始
print(s4)

s5 = s[:] # 默认都切出来
print(s5)

s6 = s[-2:] #从-2 切换到结尾，从左往右切
print(s6)

####切片小结####
#1. 语法 s[起始位置，结束位置] 
#2. 特点 骨头不顾腚
#3. 切片方向 从左往右切（即使是切负数也是从左往右）


####步长####
s = "zhangsan和lisi是好朋友"
s1 = s[1:5:2] # 从1开始，到5结束，每2个取1个
print(s1)

s2 = s[::3] # 从头到尾，每3个取一个
print(s2)

s3 = s[6:2:-1] # 从后往前数，取每一个字符（- 负号标识反着来），但还是遵循“顾头不顾腚”原则，取出的值为：asgn
print(s3)


s = "这个标点符号很蛋疼"
s1 = s[7::-2] # 从第7位索引开始，到最前，从后往前，每2个取一个，也就是：蛋号点个
print(s1)

s2 = s[-1:-6:-2] # 反方向，从-1到-6，每2个取一个，也就是：疼很符。
print(s2)


####切片小结####
#步长：代表着多少个字符为一组，取第一个，如果最后一组不够数同样还是取第一个
#语法：s[起始位置:结束位置:步长]
#特点：依然是顾头不够腚。
#方向：默认是从左往右，如果想从右往左，步长必须为复数


####字符串常见操作####
#1. upper() 和  lower()   大小写转换
s = "Alex is not a Good Man. "
print(s.upper()) # 全部转换成大写
print(s.lower()) # 全部转换成小写

while True:
    content = input("键入要输入的内容：")
    if content.upper() == "Q":
        break
    print("你输入的内容是" + content)


#2. strip() 去掉左右两边的内容，包含空格和特殊字符

username = input("键入用户名").strip() # 去掉空格的
password = input("键入密码").strip()
if username == "zhangsan" and password == "123":
    print("登陆成功")
else:
    print("登陆失败")

s1 = "****12***3*******"
print(s1.strip("*")) #去掉的是左右两边的内容，而非中间的内功。典型用法


#3. replace() 替换
s = "alex wusir alex sb taibai"
s1 = s.replace("alex","zhangsan") # 使用"zhangsan" 替换 "alex"
print(s1)
s2 = s.replace(" ","") # 去掉所有空格
print(s2)
s3 = s.replace("alex","lisi",2) # 使用lisi替换第二个alex
print(s3)

#4. split()  切割
s = "alex_wuse_taibai_bubai"
lst = s.split("_taibai_")    # 要切什么，就在括号里面指明，此示例切完之后为：['alex_wuse', 'bubai']
print(lst)
print(type(lst)) #切完的东西是列表. 列表装的是字符串 <class 'list'>


#5. format() 格式化输出
s = "我叫{},今年{},我喜欢{}".format("zhansan",18,"lisi") #格式化输出
print(s)

s1 = "我叫{1},今年{2},我喜欢{0}".format("zhansan",18,"lisi") # 也可以指定位置
print(s1)

s2 = "我叫{name},今年{age}岁,我喜欢{mingxing}".format(name="wangwu",age=22,mingxing="323") # 也可以手动定义参数
print(s2)


#6. find() 查找
s = "汪峰的老婆不爱汪峰了"
print(s.find("老")) # 计算xxx字符串在原字符串中的位置，查找方式："汪""峰""的""老"；返回值：3
print(s.find("老婆")) # 计算xxx字符串在原字符串中的位置，；查找方式："汪峰""峰的""的老""老婆"；返回值：3
print(s.find("老婆不"))  #   计算xxx字符串在原字符串中的位置；查找方式："汪峰的""峰的老""的老婆""老婆不"；返回值：3
print(s.find("国际章"))  #   计算xxx字符串在原字符串中的位置；查不到返回值：-1
print(s.find("汪峰"))  #   计算xxx字符串在原字符串中的位置；找到了之后会立刻返回，不会向后查询，返回值：0
print(s.find("汪峰",3))  # 计算xxx字符串在原字符串中的位置；自第3个字符往后找，一直到最后，查找方式："0-汪""1-峰""2-的""3-老"""4-婆不""5-不爱""6-爱汪""7-汪峰"；返回值：7


#7. startswith() 判断是否以xxx开头
s = "汪峰的老婆不爱汪峰了"
s1 = s.startswith("汪峰") # 输出为布尔类型
print(s1)
print(type(s1))



#8. len() 字符串长度. 内置函数  __len__()
s = "今天你喝酒了么"
print(s.__len__())   # 字符串长度不等于索引的下标，字串床长度是1、2、3...等；而索引的下标是0、1、2、3....等


#9. 遍历字符串
s = "小学老师，你好漂亮"
# a. 用while循环来进行遍历
count = 0 # 定义一个变量从0开始，因为索引的第一位位是0
while count < s.__len__(): # 条件：如果索引的字符小于此字符串的长度
    print(s[count]) # 执行打印当前个索引的对应的字符
    count = count + 1 # 将索引每次循环都加1

# b. 用for循环来进行遍历
for c in s: # 把变量s中的每一个字符交给前面的c，并循环
    print(c)


'''


s = "ZhangSan lisi WanGwu"
print(s.swapcase()) # 