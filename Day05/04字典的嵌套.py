'''
##字典嵌套方式
    1. 字典的嵌套，指的实在value层级上进行嵌套，可以继续嵌套dict，也可嵌套list等
    2. 多层级的打印，为print(dic[key01][sub-key001]),或者print(dic[key01][索引位置][sub-key001])



示范01：一个字典
    dic = {"name":"wangfeng",
            "age":58,
            "wife":"guojizhang"
        }
    print(dic)
    

示范02：字典嵌套
    dic = {"name":"wangfeng",
            "age":58,
            "wife":{ # 此处是字典嵌套字典
                "name":"guojizhang",
                "salary":10000,
                "age":37
            },
            "children":[ # 次数是字典嵌套元组、再嵌套字典
                {"name":"老大","age":18},
                {"name":"老二","age":10}
            ]
    }
    print(dic["children"][1]["age"])# 打印wangfeng二儿子的年龄
    print(dic["wife"]["salary"]) # 打印wangfeng媳妇的工资

'''




