'''
dic = {'jay':'周杰伦','jj':'林俊杰','eason':'陈奕迅'}
print(dic)

dic = {1:"马化腾",False:"阿里巴巴","sylar":"帅的不行不行的",(1,"haha"):"元组",["吼吼"]:"列表"} # 列表不能作为key
print(dic)

## 增加
    1. dic[key] = value # 等同于直接赋值，key如果存在执行替换，如果不存在执行新增
    2. dic.setdefault(key,value) #key如果存在不做操作，如果不存在执行新增，同时返回新增的value
    
    dic = {"昆凌":"周杰伦的老婆"}
    dic["国际章"] = "汪峰的老婆" # 新增，输出为：{'昆凌': '周杰伦的老婆', '国际章': '汪峰的老婆'}
    dic["国际章"] = "雄壮的老外" # 如果key重复，会替换原value，输出为：{'昆凌': '周杰伦的老婆', '国际章': '汪峰的老婆'}
    dic.setdefault("马蓉","王宝强的前妻") # 输出为；{'昆凌': '周杰伦的老婆', '国际章': '雄壮的老外', '马蓉': '王宝强的前妻'}
    dic.setdefault("马蓉","宋哲的现任么？？") # 如果key已经存在，将不会替换，输出依然为：{'昆凌': '周杰伦的老婆', '国际章': '雄壮的老外', '马蓉': '王宝强的前妻'}


## 删除
    1. dic.pop(key) # 删除对应的key，同时可以返回被删除key对应的value
    2. del dic[key] # 直接删除，没有返回
    3. dic.popitem() # 随机删除，返回的是元组，包含(key:value)

    示范：
    dic = {"nihao":"zhangsan","wohao":"lisi","dajiahao":"wangwu","buhao":"qianliu"}
    dic.pop("nihao") # 直接删除，打印dic的输出为：{'wohao': 'lisi', 'dajiahao': 'wangwu', 'buhao': 'qianliu'}
    dic1 = dic.pop("wohao") # 删除这个key，并且会返回对应的value，打印dic1的输出为：lisi
    del dic["dajiahao"] # 直接删除，没有返回 ,打印dic的输出为：{'buhao': 'qianliu'}

    dic = {"nihao":"zhangsan","wohao":"lisi","dajiahao":"wangwu","buhao":"qianliu"}
    dic.popitem() # 随机删除
    dic2 = dic.popitem() # 返回的元组，包含被删除的key；value，打印dic2的输出为：('dajiahao', 'wangwu')


## 修改
    1. dic[key] = dic[key] -+*/ value # value 必须为整数
    2. dic1.update(dic2) # dic2中的内容更新到dic1中，key存在替换，不存在则新增
    3. dic[key] = value # key不存在则新增，存在则修改

    示范
    dic = {"ID":1,"name":"李嘉诚","money":1000}
    dic["money"] = dic["money"] - 100 # 用key去修改，类似赋值操作，输出为：{'ID': 1, 'name': '李嘉诚', 'money': 900}
    print(dic)

    dic1 = {"李晨":"范冰冰","邓超":"孙俪","王祖蓝":"李亚男"}
    dic2 = {"李晨":"张馨予","郑凯":"baby","王宝强":"马蓉"}
    dic1.update(dic2) # 把dic2中的内容更新到 dic1 , 如果存在了key. 替换. 如果不存在,添加
    print(dic1)

    dic = {"及时雨":"宋江","小李广":"花荣","黑旋风":"李逵","易大师":"剑圣"}
    dic["大宝剑"] = "盖伦" # 新增
    dic["及时雨"] = "张三" # 修改



## 查询
    1. print(dic[key]) # 如果key存在返回value，如果不存在直接报错：keyerror
    2. print(dic.get(key)) # 如果key存在返回value，如果不存在返回None
    3. print(dic.get(key,默认值)) # 如果key存在返回value，如果不存在可以返回指定的默认值

    示范
    dic = {"及时雨":"宋江","小李广":"花荣","黑旋风":"李逵","易大师":"剑圣"}
    print(dic["易大师"]) # 查询，如果key存在返回value，如果不存在直接报错：keyerror
    print(dic.get("易大师")) # 查询，如果key存在返回value
    print(dic.get("易大师111")) # 查询，如果查询的Key不存在，返回None
    print(dic.get("易大师111","默认")) # 查询，如果查询的key不存在可以指定默认值
    #print(dic)


## 关于dic.setdefault()
    1. 首先去原字典中查询，判断有没有key，如果没有执行新增
    2. 用这个key再去字典中查询，同时返回查询的结果

    示范
    dic = {"好人":"张三","坏人":"李四"}
    dic.setdefault("不好不坏","王五") # 增加
    dic1 = dic.setdefault("及时雨222","宋江222") # 返回查询结果
    print(dic1)
    print(dic)


'''


