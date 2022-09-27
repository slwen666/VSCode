########list###########
#列表介绍
#    a. 列表是python基础数据类型之一，以[]括起来，以','隔开，可以存放多种数据类型，例如：
#       lst = [1,'ha',"hehe",[1,8,"baidu"],("我","叫","元","组")，{"我叫":"dict字典"},{"我叫集合","集合"}] 
#    b. 列表相比字符串，不仅可以存放不同数据类型，还可以存放大量数据
#    c. 列表是有序的，有索引、切片，可以方便取值

'''
#列表的索引属性
lst = ["张三","李四","王五","李六"]
print(lst[0]) #获取第一个元素
print(lst[1])
print(lst[2])

#列表是可以发生改变的，这里和字符串不同
lst[3] = "赵七"  #使用"赵七"替换原来索引为3的内容
print(lst) #输出的内容为：['张三', '李四', '王五', '赵七']

#列表中的元素可以改变，但是字符串不能直接改变
s0 = "一二三"
s0[1] = "六" #'str' object does not support item assignment,只有在列表中的元素才能修改，不能直接修改字符串
print(s0)

#列表同样具有索引功能，特点依然是"顾头不顾腚"

lst = ["zhangsan","lisi","wangwu","zhaoliu","sunqi"]
print(lst[0:2])
print(lst[0:3])

#列表同样具有切片功能（无论正着取还是反着取值永远以第一个值为基础，“切片”的意思是隔x个取一个）
lst = ["zhangsan","lisi","wangwu","zhaoliu","sunqi"]
print(lst[1::2])
print(lst[2::-2])# 倒着取
print(lst[-1::-2])


###列表的增删改查（list和str不一样，list可以发生改变，所以直接就在原来的对象修改了）
##列表的"增"
#示例01 - .append() 
lst = ["马化腾","林俊杰","周润发","周芷若"]
print(lst)
lst.append("wusir") # 在结尾增加（此处直接修改了原有的数据）
print(lst)

#示例02 - .append()
lst = []
while True:
    content = input("请输入你要录入的员工信息，输入Q退出：")
    if content.upper() == "Q":
        break
    lst.append(content) # 将输入的所有内容全都追加到变量lst中
print(lst)


#示例03 - .insert()
lst = ["马化腾","林俊杰","周润发"]
lst.insert(1,"张三") # 在索引为1的位置插入"张三"，原来的元素向后移动一位
print(lst)

#示例04 - .extend()
lst = ["张三","李四","王五"]
lst.extend(["你好","哈喽"]) # 迭代添加，在原变量末尾追加（相比.append(),此参数可以追加多组元素）
print(lst)

###列表的"删"
#示例01 - .pop()
lst = ["马化腾","林俊杰","周润发","周芷若"]
print(lst)
deleted = lst.pop() # 删除最后一个
print("被删除的",deleted)
print(lst)

#示例02 - .pop()
lst = ["马化腾","林俊杰","周润发","周芷若"]
e1 = lst.pop(2) #删除指定索引元素
print("被删除的",e1)
print(lst)

#示例03 - .remove
lst = ["马化腾","林俊杰","周润发","周芷若"]
lst.remove("马化腾") # 删除指定元素
print(lst)
#lst.remove("haha") # 如果指定元素不存在则会报错
#print(lst)

#示例04 - .clear()
lst = ["马化腾","林俊杰","周润发","周芷若"]
lst.clear() #  清空list
print(lst)


#示例05 - del
lst = ["马化腾","林俊杰","周润发","周芷若"]
del lst[1:3] # 删除切片位置（同样遵从顾头不顾腚原则）
print(lst)


###列表的"改"
#示例01 - 索引修改
lst = ["张三","李四","王五"]
lst[1] = "lisi"
print(lst)


#示例02 = 步长修改
#切边+步长，是将范围的元素全都修改
#如果步长唯1则可以随便增加元素
#如果步长不是1，那么元素的数量必须在步长以内）
lst = ["第一","第二","第三","第四","第五","第六"]
lst[1:4:2] = ["修订01","修订02"] # 在此示例中，最多两个能有两个元素，超过了就会报错，因为步长的限制
print(lst)

#示例03 = 切片修改
lst = ["第一","第二","第三","第四","第五","第六"]
lst[1:4] = ["nihaonihao"] #如果切片没有步长，或者步长为1，可以随便增加元素
print(lst)
lst[1:4] = "马化腾" # 输出为['第一', '马', '化', '腾']，迭代修改
print(lst))


###列表的嵌套
lst = [1, "太白", "wusir", ["⻢虎疼", ["可口可乐"], "王剑林"]]

# 找到wusir
print(lst[2])

#找到太白和wusir
print(lst[1:3])

#找到太白的白字
print(lst[1][1])

#将wusir拿到，然后首字母大写再扔回去
s = lst[2]
s = s.capitalize()
lst[2] = s
print(lst)
#简写
lst[2] = lst[2].capitalize()
print(lst)

# 把天白换成太黑  
lst[1] = lst[1].replace("白","黑")
print(lst)

#把马虎疼换成马化腾
lst[3][0] = lst[3][0].replace("虎","化")
print(lst)

# 可口可乐后面追加芬达
lst[3][1].append("芬达")
print(lst)





###列表的查询
#示例01
#列表是一个可迭代对象，所以可以进行for循环
lst = ["第一","第二","第三","第四","第五","第六"]
for el in lst:
    print(el)


# 查询元素出现的次数
lst = ["nihao","wohao","dajiahao","nihao","wohao","dajiahao"]
c = lst.count("nihao") # 查询nihao出现的次数
print(c)

#将元素排序
lst = [1,11,22,2]
lst.sort() # 排序，默认是升序
print(lst)
lst.sort(reverse=True) # 降序
print(lst)

lst = ["nihao","wohao","dajiahao","nihao","wohao","dajiahao"]
print(lst)  
lst.reverse() # 倒序
print(lst)
l = len(lst) # 列表的长度（注意和索引区分，此处输出是6）
print(l)

'''






