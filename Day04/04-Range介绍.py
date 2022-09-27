# 相比与while循环，在for循环中需要使用range参数来遍历int
# range也是从0开始计算，
# range同样类似索引、切片、步长的编写格式，也同样遵循"顾头不顾腚"原则
'''

# 输出10个整数
for num in range (10):
    print(num) # 输出 0、1、2、3、4.....9


# 输出的范围类似切片，同样遵循"顾头不顾腚"原则
for num in range (3,7): #输出3、4、5、6
    print(num)

#输出的范围类似步长，在1 - 10 范围内，每2个取一个
for num in range (1,10,2):# 输出1、3、5、7、9
    print(num)

# 也可以倒序的输出
for num in range (10,1,-2): 输出10、8、6、4、2
    print(num)

'''

# 用for循环计算1-2+3-4.....+99-100
sum = 0
for count in range (1,101):
    if count % 2 == 0:
        sum = sum - count
    else:
        sum = sum + count
print(sum)


