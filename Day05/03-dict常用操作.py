'''
## 字典常用操作
    1. print(dic.keys()) # 拿到所有的key, 返回key的集合,即:dict_Keys(['key1','key2','key3'])像是列表. 但是不是列表
        迭代循环：for key in dic.keys():输出的是key

    2. print(dic.values()) # 拿到所有的value, 返回value的集合,即:dict_Keys(['value1','value2','value3'])像是列表. 但是不是列表
        迭代循环：for value in dic.values():输出的是所有Value

    3. print(dic.items()) # 拿到键值对，返回所有key,value的集合，即dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3')]),像是列表.但是不是列表，列表里面包含元组
        迭代循环：for item in dic.items():# 输出的键值对，每个键值对是一个元组,即(key1,value1)
    

## 解构
    1. a, b = 1,2
        print(a) # 输出为：1
        print(b) # 输出为：2

    2. a,b = (1,2)
        print(a) # 输出为：1
        print(b) # 输出为：2

    3. a = 1,2
        print(a) # 输出为：(1, 2),也就是元组

    4. a, b = [1, 2]
        print(a, b) # 输出为：1 2

    5. for item in dic.items(): #可以进行迭代循环
            k,v = item #按照解构的方式
            print(k) #打印所有的Key
            print(v) # 打印所有的value
            print(k,v) # 此处输出的是 key value,注意此处输出的不是以元组显示显示的(key,value)
    
    6. for k,v in dic.items(): # 理论与上面一样
            print(k)
            print(v)
            print(k,v)



#示范01：打印key
    dic = {"及时雨":"宋江","易大师":"剑圣","维恩":"暗影猎手"}
    print(dic.keys())  # 输出为：dict_Keys(['易大师','维恩','及时雨'])

    for key in dic.keys(): # 可以进行迭代循环，输出的是key
        print(key) 

示范02：打印value
    dic = {"及时雨":"宋江","易大师":"剑圣","维恩":"暗影猎手"}
    print(dic.values()) #输出为：dict_values(['剑圣','暗影猎手','宋江'])

    for value in dic.values(): # 可以进行迭代循环，输出的是所有Value
        print(value)


示范03：打印items
    dic = {"及时雨":"宋江","易大师":"剑圣","维恩":"暗影猎手"}
    print(dic.items()) #拿到键值对,即：dict_items([('及时雨', '宋江'), ('易大师', '剑圣'), ('维恩', '暗影猎手')])

    for item in dic.items():# 可以进行迭代循环
        print(item) # 输出的是所有key,value,每个键值对是一个元组
        print(item[0])  # 输出的是所有key
        print(item[1])  # 输出的是所有value


示范04：解构
    a,b,c = ("zhangsan","lisi","wangwu")
    print(b) # 输出为：lisi

    dic = {"及时雨":"宋江","易大师":"剑圣","维恩":"暗影猎手"}
    #for item in dic.items(): #可以进行迭代循环
        #print(item) #输出的是(key,value)

        #k,v = item #按照解构的方式
        #print(k) #打印所有的Key
        #print(v) # 打印所有的value
        #print(k,v) # 此处输出的是key value,注意此处此处与直接print(item) 输出的是元组(key,value)不同


    for k,v in dic.items():
        print(k) # 这样更方便可以直接拿到key
        print(v) # 这样更方便可以直接拿到value
        print(k,v) # 这样更方便可以直接拿到key value





'''
