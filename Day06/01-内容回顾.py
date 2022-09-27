'''
a = 2021
print(a.bit_length()) # int二进制长度
b = "2121"
print(len(b)) # str 字符串长度


a = 0
a1 = bool(a) #  # 0是False
b = 1
b1 = bool(b) # 非0 是True
print(a1) 
print(b1)


s = "nihao/wohao/dajiahao"
print(s[0]) # 索引
print(s[1:5]) # 切片
print(s[1:5:2]) # 步长
print(s.upper()) # 全部转为大写
print(s.lower()) # 全部转为小写
print(s.replace("o","k",1)) # 替换，将第一个"o",替换为"k"
print(s.split("/")) # 剪切，剪完之后变成列表
print(s.startswith("n")) # 判断开头是x，返回True或者False
print(s.find("o")) # 查找x所属的位置（仅会返回第一个）
print(s.count("a")) # 计算x字符总计出现了几次

name = input("name:")
age = int(input("age:"))
print("{name}今年{age}岁了" .format(name = name,age = age))
print("{}今年{}岁了" .format(name,age))
print("{1}今年{0}岁了" .format(age,name))
print("%s今年%d岁了" % (name,age))


l = ["字符串",100,("zhangsan",20),["lisi",20]]
print(l[0]) # 索引
print(l[1:]) # 切片
print(l[1::2]) # 步长

l.append("wangwu") # 增加（末尾）
l.insert(1,1000) # 指定位置插入
l.extend(["多个元素01","多个元素02"]) # 迭代添加，可以添加多个字符

l.pop(0) # 删除指定位置的元素
l.remove(100) # 删除指定元素
del l[1:] # 删除指定范围的元素
l.clear() # 清空所有
print(l)


l = ["字符串",100,("zhangsan",20),["lisi",20]]
for c in l:
    print(c)


a = [10,2,5,7,9,3,4,6,8,8]
a.sort() # 升序
print(a)
a.sort(reverse=True) # 倒序
print(a) 
print(len(a)) # 计算元素的个数
print(a.count(8)) # 计算机x元素出现的个数



b = (100,"字符串",[20,"zhangsan"],("元组"))
print(b[0])
print(b[1:])
print(b[1::2])
b[2].append("lisi")


for c in b:
    print(c)


a,b = 100,200
print(a)
print(b)

for c in range(10):
    print(c)


for s in range(5,10):
    print(s)


for n in range(5,10,3):
    print(n)

dit = {"key01":"zhangsan",100:"lisi",("元组"):20}
dit["key02"] = 30 # 新增
dit.setdefault("key03","value03")  # 新增
'''


dit = {"key01":"zhangsan",100:"lisi",("元组"):20,"黑旋风":"李逵","及时雨":"宋江"}
dit.pop("key01") # 删除（字符串中的pop指定的位置）
del dit[100]
dit.popitem()

print(dit)
























