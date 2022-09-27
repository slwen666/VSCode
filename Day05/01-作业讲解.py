'''
习题01：
li = ["alex","sam","jenny","jordan","gavin"]
li.sort() # 升序
print(li)
li.reverse() # 降序 （li.sort(reverse=True））
print(li)
S = "user01"
li.extend(S) # 迭代添加，输出：['sam', 'jordan', 'jenny', 'gavin', 'alex', 'u', 's', 'e', 'r', '0', '1']
print(li)
li.extend([S]) # 迭代添加，输出：['sam', 'jordan', 'jenny', 'gavin', 'alex', 'u', 's', 'e', 'r', '0', '1', 'user01']
print(li)

习题02：
lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
lis[3][2][1][0] = lis[3][2][1][0].upper() # 转大写 tt - TT
lis[3][2][1][0] = lis[3][2][1][0].replace("T","A") #  TT 更换 AA
lis[3][2][1][0] = "BB" # 直接赋值更改 # 将 AA 更改为 BB
lis[3][2][1][1] = "100" # 将数字3 更改为 字符串100
print(lis)

习题03
lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
lis[3][2][1][1] = str(lis[3][2][1][1]+97) # 计算完成之后，转为字符串
print(lis)


习题04：打印01_02_03
lit = ["01","02","03"]
count = ""
for c in lit:
    count = count + c + "_" # 遍历列表中元素，每遍历到一个就在末尾添加一个下划线"_"
print(count[:-1]) # 打印开始:-1的目的是为了规避打印最后一个下划线"_"


习题05：
lit = ["user01","user02","user03","",12]
for c in range(len(lit)): # 遍历输出列表元素的索引，即：0、1、2、3、4
    print(c)


习题06：
lst = []
for i in range (1,101): 
    if i % 2 == 0:
        lst.append(i) # 将1-100中的偶数添加到列表中
print(lst)

习题07：
lst = []
for i in range(50):
    if i % 3 == 0:
        lst.append(i) # 将50以内的奇数添加到列表中
print(lst)

习题08：
for i in range (100,0,-1):
    print(i) # 使用for循环，倒序打印100、99、98、97、、、1

习题09：
count = 100
while count > 0:
    print(count)
    count = count - 1 # 使用while循环，打印100、99、98、97、、、1




习题10：
lst = []
for i in range (100,9,-1):
    if i % 2 == 0:
        lst.append(i) # 倒序打印 100 - 10 之间的偶数
print(lst)
lst1 = []
for s in lst:
    if s % 4 == 0:
        lst1.append(s) # 引用上述输出，筛选哪些是4的倍数
print(lst1)

习题11：
lst = []
for i in range (1,31):
    lst.append(i) # 将 1- 30以内的数字输入到列表lst中
net_lst = []
for e1 in lst:
    if e1 % 3 == 0:
        e1 = "*" # 如果是3的倍数，则使用* 号代替
    net_lst.append(e1)
print(net_lst)

习题12：
li = ["TaiBai ", "ale  xC", "AbC   ", "egon", " ri  TiAn", "WuSir", "  aqc"]
lst = []
for i in li:
    i = i.replace(" ","") # 替换掉空格
    if (i.startswith("A") or i.startswith("a")) and i.endswith("c"): # 筛选开头是A或者a，并且结尾是"c"的元素，or
        lst.append(i)
print(lst) # 输出：['aqc']




习题13：屏蔽用户输入的特殊字符，使用*代替
lst = []
lit = ["user01","user02","user03","user004","user005"]
content = input("请输入你的评论：")
for e1 in lit:
    if e1 in content: # 如果敏感字符包含在输入的评论中
        content = content.replace(e1,"*" * len(e1)) # 使用*号替换敏感字符，同时*号的个数应该与敏感字符的长度相同，即"*" 乘以字符串长度 len(e1)
lst.append(content)
print(lst)


习题14：遍历输出列表中的内容，其中要求所有字符串均为小写
li = [1, 3, 4, "alex", [3, 7, 8, "TaiBai"], 5, "RiTiAn"]
for e in li:
    if type(e) == list: # 判断数据类型
        for ee in e:
            if type(ee) == str:
                print(ee.lower())
            else:
                print(ee)
    else:
        if type(e) == str:
            print(e.lower())
        else:
            print(e)


习题15：把班级学生数学考试成绩录入到一个列表中:  并求平均值.  要求:  录入的时候要带着学生姓名和成绩,  例如:  张三_44

lst = []
while 1:
    stu = input("请输入学生姓名和成绩（zhangsan_90）:")
    if stu.upper() == "Q":
        break
    lst.append(stu) # 所有的学生姓名和成绩追加到列表中
print(lst) #此时输出的是：['zhangsan_100', 'lisi_200']
sum = 0
for c in lst:
    print(c) # 此时遍历输出的是：zhangsan_100、lisi_200
    c1 = c.split("_") # 
    print(c1) # 此时删除掉“_”输出的是:['zhangsan', '100']、['lisi', '200']
    sum = sum + int(c1[1]) # 将所有总成绩添加到sum变量中
print(sum / len(lst)) # 用总成绩除以变量lst中元素的个数（学生数），得出的就是平均值

'''

