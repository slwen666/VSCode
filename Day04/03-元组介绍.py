##########Tuple-元组和元组嵌套#######
#元组的介绍
#   元组也是python的基础数据类型之一，用小括号括起来，用逗号隔开，里面可以方任何类型的数据   
#   俗称不可变的列表，也被称为只读列表
#   元组的中的数据，可以查询、循环、切片，不能进行增、删、改
#   （元组不可变指的是子元素不可变，但是子元素内部的数据是可以边的，这却决于子元素是否为可变对象）


'''

# 示例说明 - 01
tu = (100,"nihao","wohao","tahao")
print(type(tu)) # Tuple
print(tu)

# 元组的索引
print(tu[0])
print(tu[1])
print(tu[2])
print(tu[3])

#for 循环遍历元组
for el in tu:
    print(el)

# 尝试进行则直接进行报错
tu[1] = "修改001" # 报错 'tuple' object does not support item assignment
print(tu)


#示例说明 - 02
tu =(1,"haha",[],"hehe")
#tu[2] = ["ererer"] # 直接进行修改则会报错
#说明：
#元组不可变指的是子元素不可变，但是子元素内部的数据是可以边的，这却决于子元素是否为可变对象
tu[2].append("添加01") # 这样是可以添加的
tu[2].append("添加02")
print(tu)

# 示例 - 03
# 元组中即使只有一个元素也要加逗号，否则就不是元组了，容易出错的地方！！！！
tu = (1,)
print(type(tu))
print(tu)





# 元组也具备count(),index(),len()等方法



'''







