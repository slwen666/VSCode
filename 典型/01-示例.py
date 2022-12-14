'''
Str 操作方法 - 索引、切片、步长
索引：
    正数下标从0开始，倒数下标从-1开始
    通过索引获取到的内容. 还是一个字符串
切片：
    通过索引截取指定内容
    语法： s[开始位置:结束位置]
    方向：从左往右
    特点：顾头不顾腚
步长：
    通过索引可以 跳着 取指定内容
    步长代表：多少个取第一个,例如：步长为3，代表每3个取第一个，最后一组不足3个的也算是一组，同样取第一个。
    语法：s[起始位置:结束位置:步长]
    如果步长为负数，代表从左往右取（默认从右往左取），注意 起始位置 > 结束位置

Str常用场景 - 转换
    s.capitalize() #字符串中第一个单词的首字母大写,其余变成小写
    s.upper() #全部大写
    s.lower()  #全部小写
    s.swapcase() # 大小写互换
    s.title() # 被特殊字符（包含中文、空格）隔开的首字母大写
    s.center(9,"*") # 补充为9个字符，原字符串居中，不足的以*补充
    s.strip() # 删除字符左右两端的内容（空格或者字符），但包含在中间的不动
    s.replace("被替换的内容","新内容","数量") # 替换指定内容，如果不指定数量，默认替换所有
    z.split("_lisi") #删除指定内容，输出的是列表，删除掉的内容在输出的中标注为","，例如：['zhangsan', '_bu_shi_peng_you']

str常用场景 - 查找
    s = "礼拜六和礼拜日不用上班"       
    print (s.startswith("礼拜"))# 判断是否以xxx开头，输出类型为bool，此处输出为：True
    print(s.endswith("下班")) # 判断是否以xxx结尾，此处输出为：False
    print(s.count("礼拜")) # 判断xxx字符长出现的次数，此处输出为：2
    print(s.find("礼拜")) # 查找指定字符出现的位置，如原文中有多个，此处只返回第1个出现的位置，找不到的返回-1，次处输出为：0
    print(s.find("礼拜", 3,6)) # 切片差找指定内容，切片的方式与常规切片不同，此处输出的内容是：4
    print(s.index("礼拜")) # 也是差找，但相比于find，index差找不到内容会直接报错


Str常用操作 - 判断
    s = "nihao123"
    print(s.isdigit())  #判断原字符串是仅由 数字 组成。 此处输出为：False
    print(s.isalpha())  # 判断原字符串仅由 字母 组成。此处输出为：False
    print(s.isalnum())  # 判断原字符串是否由 数字和字母 组成。次数输出为：True


列表 - 索引、切片、步长
    列表可以存放多种类型数据
    列表同样适用索引、切片、步长，并且操作方法与字符串一致
    列表中的元素是可以直接改变，这里与字符串不同
    示范01：
    lst = ["str",1,True,["嵌套"]] # 存放多种类型数据
    print(lst[0]) # 索引
    print(lst[:3]) # 切片
    print(lst[::-2]) # 步长

列表 - 增加
    lst.append(元素) # 末尾增加一个元素
    lst.insert(位置，内容) # 指定位置插入一个元素
    lst.extend([元素]) # 迭代添加（添加多个元素）

列表 - 删除
    lst.pop(索引) # 默认删除最后一个元素，也可以指定索引位置进行删除
    lst.remove(元素) # 删除指定元素
    del lst[其实位置:结束位置] # 切片删除
    lst.clear() # 清空所有元素



把班级学生数学考试成绩录入到一个列表中:  并求平均值.  要求:  录入的时候要带着学生姓名和成绩,  例如:  张三_44
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