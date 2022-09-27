'''
第一章重点回顾：

1. 变量: 
    变量是程序运行过程中产生的中间值. 暂时存储在内存中. 供后面的程序使用
    重点名命规则：不能是数字开头, 更不能是纯数字、不要用中文、禁止用关键字、区分大小写

2. 注释
    #
    """ """
    ''' '''
3. python不存在绝对的常量. 一般, 所有字母大写. 常量

4. 常见数据类型
    字符串
    整数
    布尔：只有True, False两个值

5. 查看数据类型
    a = 128
    print(type(a))	# 打印变量a的数据类型  a 是int类型
        
6. 运算
    字符串：+ *
        示范01：
        s1 = "sylar"
        s2 = "wusir"
        s3 = "alex"
        s4 = s1 + s2 + s3	# 字符串拼接(连接)
        print(s4)

        示范02：
        s = "考试\n"	
        print(s*3)	# s重复 3次，并自动换行（默认不换行）
        
    整数：+ - * /
        示范01：
        a = 9
        b = 3
        print(a%b) # 取余
        print(a/b)
        print(a//b) # 取整

        示范02：
        num = input("输入一个数字:")
        num = int(num)
        if num % 3 == 0:
            print("是三的倍数")
        else:
            print("不是")

7. 条件判断（if else）
    示范01：
    gender = input("您是男的还是女的:")
    if gender == "女的":
        age = input("年龄:")
        age = int(age)
        if age > 30:
            print("再见")
        else:
            print("请进")
    else:
        print("滚蛋")
    
    示范02：
    money = input("请输入你手里的钱:")
    if int(money) > 500:
        print("和啤酒吃炸鸡. 生活美滋滋")
    else:
        if int(money) > 300:
            print("吃个盖浇饭. 生活乐无边")
        else:
            if int(money) > 50:
              print("方便面走起")
            else:
                print("减肥")    

    示范03：
    money = input("请输入你手里的钱:")
    if int(money) > 500:
        print("和啤酒吃炸鸡. 生活美滋滋")
    elif int(money) > 300:
        print("吃个盖浇饭. 生活乐无边")
    elif int(money) > 50:
        print("吃个方便面. 开心")
    else:
        print("减肥")


第二章重点回顾
1. while 循环
    示范01：
    count = 1
        while count < 8:
        print("123")
        count = count + 1

    示范02：
    while True:
    s = input("输入内容：")
    if s == "q":
        break
    if "zhangsan" in s or "lisi" in s:
        print("关键字符")
        continue
    else:
        print("输入的内容是:" + s)
    
    示范03：1+2+3+...100
    count = 1
    sum = 0
    while count <= 100:
        sum = sum + count # 1+2+3+..100
        count = count + 1 # 1、2、3、4、100
    print(sum)

    示范04：打印所有奇数
    count = 1
    while count <= 100:
    if count % 2 != 0:
        print(count)
    count = count + 1


    示范04：while else
    count = 1
    while count < 10:
        print(count)
        count = count + 1
    else: # 条件不成立时执行
        print("超初范围")

    
    示范05：break
    count = 1
    while count < 10:
    print(count)
    count = count + 1
    if count == 9:
        break # 彻底停止循环. 不会执行后面的else
else:
    print("超初范围")
2. 格式化输出
    示范01：%s 代表文本
    name = input("name:")
    age = input("age:")
    hobby = input("hobby")
    gender = input("gender")
    print(name + "今年" + age + "岁，是一个老头，爱好是" + hobby + "兴趣是" + gender) # 字符串拼接
    print("%s今年%s岁，是一个老头，爱好是%s,兴趣是%s" % (name,age,hobby,gender)) # 格式化输出

    示范02：%d 代表整数
    a = 108
    s = "梁山有%d位好汉" % (a) # %d 如果占位符是%d ，只能是整数
    print(s)

    示范03：如果字符串中有了占位符. 那么后面的所有的%都是占位. 需要转义-%%
    name = "zhangsan"
    s = "%s获胜的机率是%%50" % (name)
    print(s)

3. 比较运算
    a = 10
    b = 20
    print(a == b) # False # 等于
    print(a != b) # True # 不等于
4. 赋值运算
    a = 10
    a += 20 #等同于 a = a + 20
    print(a)
5. 逻辑运算
    and:两边都为真，才为真的，否则为假
    or：其中一个为真，即为真，否则为假
    运算顺序：()>not>and>or
    X or Y：如果X = 0，即为Y，否则为X
    X and y：如果X = 0，即为0，否则为Y
    False 相当于 0；True相当于 非0

    示范01：()>not>and>or
    print(3>4 or 4<3  and  1==1) # False
    print(not  2 > 1  and 3 < 4  or 4 > 5  and 2 > 1  and 9 > 8  or 7 < 6) # F

    示范02：X or Y：如果X = 0，即为Y，否则为X
    print(1 or 2) # 1
    print(0 or 2) # 2

    示范03：X and y：如果X = 0，即为0，否则为Y
    print(1 and 2) # 2
    print(0 and 2) # 0

    示范04：整数逻辑运算
    print(0 or 4 and  3 or 7 or 9 and  6) # 3

    示范05： 布尔逻辑运损
    print(2 > 3 and 3) # False

    示范06： 整数和布尔逻辑运算
    print(2 < 1 and 4 > 6 or 3 and 4 > 5 or 6)


第三章 重点回顾
上一章节回复
1. while else
    习题01：猜数
    count = 1
    n = 66
    while  count <= 3:
        num = int(input("输入数字:"))
        if num > n:
            print("大")
        elif num < n:
            print("小")
        else:
            print("正确")
            break
        print("你已经猜了%d了，还剩%d机会了" % (count,3-count))
        count = count + 1
    else:
        print("没有机会了")
    

    习题02：打印1 - 10 ，没有7 
    count = 1
    while count <= 10:
    if count == 7:
        count = 8
        continue
    print(count)
    count = count + 1

    习题03：1-2+3-4....+99
    count = 1
    sum = 0
    while count < 100:
        if count % 2 == 0: # 偶数
            sum = sum - count
        else:
            sum = sum + count
        count = count + 1
    print(sum)

    习题04：仅3次登陆机会，并提升剩余登陆次数
    count = 1
    while count <= 3:
        username = input("username:")
        password = input("password:")
        if username == "zhangsan" and password == "123":
            print("success")
            break
        else:
            print("Failed")
            print("还剩%d机会了" % (3-count))
            count = count + 1
    else:
        print("没有机会了")

    习题05：广告标语不能包含关键字
    ad = input("广告标语：")
    if "第一" in ad or "最好" in ad:
        print("不合法")
    else:
        print(ad)

1. int操作方法
    bit_length()：求整数的二进制长度
    示范01
    a = 100
    print(a.bit_length())

2. bool操作方法
    转换成什么就用什么把目标括起来
    True: 1  False:0
    零: False 非零: True
    "" 代表空字符串，空字符表示False, 非空字符串表示:True
    None代表空，连空气都不如. 真空, False

    示范01：字符<-->整数
    s = "128"
    i = int(s) # 字符串转整数
    print(i)
    print(type(i))
    ss = str(i) # 整数转字符串
    print(ss)
    print(type(ss))

    示范02：布尔-->整数（True: 1  False:0）
    b = False
    c = int(b) # 输出为：0；
    print(c)
    print(type(c))

    示范03：整数-->布尔（零: False 非零: True）
    a = 2
    b = bool(a) # 输出为：True
    print(b)
    print(type(b))

    示范04：1的效率比True 稍微高一点点
    while 1:
        print("222")

    示范05："" 代表空字符串，空字符表示False, 非空字符串表示:True
    s = "" 
    if s:
        print("hehe")
    else:
        print("haha")  # ""相当False，所以输出为haha

    示范05：None 真空, False
    m = None 
    if m:
        print("a")
    else:
        print("b") # None 相当False，所以输出为b

3. Str 操作方法 - 索引、切片、步长
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


    示范01：索引    
    s = "今天是个好日子"
    print(s[0]) # 今
    print(s[1]) # 天

    print(s[-1]) # 子
    print(s[-2]) # 日

    示范02：切片
    s = "zhangsan和lisi是好朋友"
    s1 = s[1:3]
    print(s1) # 输出：ha
    s2 = s[0:4] + s[5:10] # 可以字符串拼接，输出：zhansan和l
    print(s2 )
    s3 = s[:5] # 不输入开始位置，默认从头开始。输出的内容是：zhang
    print(s3) #
    s4 = s[5:] # 不输入结束位置，默认到最后。输出的内容是：san和lisi是好朋友
    print(s4)
    s5 = s[:] # 什么都不输入，默认输出全部内容
    print(s5)
    s6 = s[-4:] # 可以倒着切，但方向依然是从左往右，输出内容是：是好朋友
    print(s6)

    示范03：步长
    s = "今天气温很低，不上想上班"
    s1 = s[1:5:3]
    print(s1) # 正着切（从左往右），每3个取一个，最后一组即使不够3个也取一个，输出为：天很

    s2 = s[::3]   
    print(s2) #与切片一样，起始位置和结束位置什么都不写代表所有内容，输出为：今温，想

    s3 = s[6:2:-1]
    print(s3) # 如果步长为负数，代表反着取（从右往左取），输出为：，低很温

    s4 = s[7::-2]
    print(s4) # 同样为反着取，输出为：不低温天

    s5 = s[-1:-6:-2] # 依然为反着取，输出为：班想不
    print(s5)

4. Str常用场景 - 转换
    s.capitalize() #字符串中第一个单词的首字母大写,其余变成小写
    s.upper() #全部大写
    s.lower()  #全部小写
    s.swapcase() # 大小写互换
    s.title() # 被特殊字符（包含中文、空格）隔开的首字母大写
    s.center(9,"*") # 补充为9个字符，原字符串居中，不足的以*补充
    s.strip() # 删除字符左右两端的内容（空格或者字符），但包含在中间的不动
    s.replace("被替换的内容","新内容","数量") # 替换指定内容，如果不指定数量，默认替换所有
    z.split("_lisi") #删除指定内容，输出的是列表，删除掉的内容在输出的中标注为","，例如：['zhangsan', '_bu_shi_peng_you']


    示范01：
    s = "nihao and wohao dajiahao"
    s1 = s.capitalize()
    print(s1) # 字符串中第一个单词的首字母大写，输出为：Nihao and wohao dajiahao

    示范02：
    s2 = s.upper()
    print(s2)   # 全部大写，输出为：NIHAO AND WOHAO DAJIAHAO

    示范03：
    s3 = s.lower()
    print(s3)   #全部小写，输出为：nihao and wohao dajiahao


    示范04：
    while True:
        s = input("请喷:")
        if s.upper() == "Q":
            break
        else:
            print("喷的内容是:" , s)

    示范05：
    m = "ZhSan Lisi Wangwu"
    m1 = m.swapcase() # 大小写互换，输出为：zHsAN lISI wANGWU
    print(m1)

    示范06：
    n = "jintian是个 haorizi"
    n1 = n.title()  # 每个被特殊字符（包含中文、空格）隔开的首字母大写，输出为：Jintian是个 Haorizi
    print(n1)

    示范07：
    o = "张三"
    o1 = o.center(9,"*")    #补充为9个字符，原字符串居中，其余以*补充，输出为：****张三***
    print(o1)

    示范08：
    username = input("请输入用户名:").strip() # 去掉左右两端的空格（中间的不管）
    password = input("请输入密码:").strip()
    if username == "zhangsan" and password == "123":
        print("登陆成功")
    else:
        print("登陆失败")
    
    示范09：
    c = "***sjdh*sd*****" 
    c1 = c.strip("*") # 去掉左右两边的*，中间的不管，输出为：sjdh*sd
    print(c1)

    示范10：
    x = "zhangsan lisi wangwu"
    x1 = x.replace("zhangsan","张三") # zhangsan换成张三，输出为：张三 lisi wangwu
    print(x1)

    示范11：
    x = "zhangsan lisi zhangsan wangwu zhangsan liliu"
    x1 = x.replace("zhangsan","张三") # zhangsan全部换成张三，输出为：张三 lisi 张三 wangwu 张三 liliu
    print(x1)

    示范12：
    x2 = x.replace(" ","") # 去掉所有空格，输出为：zhangsanlisizhangsanwangwuzhangsanliliu
    print(x2)

    示范13：
    x3 = x.replace("zhangsan","张三",2) ## 张三换成zhangsan，仅替换前2个，剩余的不变，输出为：张三 lisi 张三 wangwu zhangsan liliu
    print(x3)

    示范14：
    z = "zhangsan_lisi_bu_shi_peng_you"
    z1 = z.split("_lisi") # 刀切指定内容，输出的东西是列表，列表里面是字符串，输出内容为：['zhangsan', '_bu_shi_peng_you']
    print(z1)

5. str常用场景 - 查找
    s = "礼拜六和礼拜日不用上班"       
    print (s.startswith("礼拜"))# 判断是否以xxx开头，输出类型为bool，此处输出为：True
    print(s.endswith("下班")) # 判断是否以xxx结尾，此处输出为：False
    print(s.count("礼拜")) # 判断xxx字符长出现的次数，此处输出为：2
    print(s.find("礼拜")) # 查找指定字符出现的位置，如原文中有多个，此处只返回第1个出现的位置，找不到的返回-1，次处输出为：0
    print(s.find("礼拜", 3,6)) # 切片差找指定内容，切片的方式与常规切片不同，此处输出的内容是：4
    print(s.index("礼拜")) # 也是差找，但相比于find，index差找不到内容会直接报错

6. Str常用操作 - 判断
    s = "nihao123"
    print(s.isdigit())  #判断原字符串是仅由 数字 组成。 此处输出为：False
    print(s.isalpha())  # 判断原字符串仅由 字母 组成。此处输出为：False
    print(s.isalnum())  # 判断原字符串是否由 数字和字母 组成。次数输出为：True

    s = "二千136万"
    print(s.isnumeric()) # 判断原字符串是仅由 数字 组成，相对比s.isdigit()，此参数识别中文数字，但识别率不是100%

7. 格式化输出
    s = "我叫%s，今年%d，我喜欢%s" % ("zhangsan",18,"lisi") # %s 和 %d 作为占位符
    print(s)

    s1 = "我叫{}，今年{}，我喜欢{}" .format("zhangsan",18,"lisi") # 以{} 作为占位符，并以.formar 隔开
    print(s1)

    s2 = "我叫{1}，今年{2}，我喜欢{0}" .format("zhangsan",20,"lisi") # 以{} 作为占位符，占位符中可以指定位置
    print(s2)

    s3 = "我叫{name}，今年{age}，我喜欢{aihao}" .format(name="zhangsan",age=18,aihao="lisi") # 以{} 作为占位符，可以指定变量
    print(s3)

8. 求字符串长度
    s = "一二三四五六"
    s1 = len(s) # 求字符串长度(不是二进制长度)，与input、print一样都是python内置函数，输出为：6
    print(s1)
    s2 = s.__len__() # len() 实际执行的就是它
    print(s2)


9. 迭代查询
    语法：
        for bianliang  in  可迭代对象:
            循环体
    对比：
        优势：简单
        劣势：没有索引

    s = "今天天气一般"
    #方式1 - 使用while循环进行遍历
        count = 0
        while count < len(s):
            print(s[count]) # 逻辑：索引的长度小于字符串长度，则遍历打印索位对应的字符串
            count = count + 1

    # 方式2 - 使用for循环进行遍历
        s = "今天天气一般"
        for c in s:
            print(c)

练习01 - 判断数字出现的次数
    s = "I am sylar, I'm 14 years old, I have 2 dogs!"
    count = 0
    for c in s:
        if c.isdigit(): # 遍历查询每一个字符，如果查询到的对象是 数字 ，那么计数加一，最后打印计数，此处输出为：3
            count = count + 1
    print(count)
    
练习02 - 判断是否为小数
    s = "-123.12"
    s = s.replace("-","") # 替换掉负号
    if s.isdigit(): # 判断是否为 整数
        print("是整数")
    else:
        if s.count(".") == 1 and not s.startswith(".") and not s.endswith("."): # 判断是否包含小数点，并且即不在开头也不在结尾
            print("是小数")
        else:
            print("不是小数")

第四章 重点回顾
上一章节回顾
    习题01：查找a出现的位置（此处仅查询了前两个）
    name = "zhangsan and lisi"
    e1 = name.find("a",0,6)
    print(e1)
    e2 = name.find("a",6)
    print(e2)
    
    习题02：使用while循环查找a的位置
    name = "zhangsan and lisi"
    count = 0 # 定义一个变量做为索引的开始值
    while count < len(name): # while循环，如果索引值小于原字符串的二进制长度，则执行如下循环
        if name[count] == "a": # 如果源字符串的索引位置输出的是 a
            print(count) # 则打印输出索引位置
        count = count + 1 # 索引循环

    习题03：仅首字母大写（此处如果使用s.capitalize()虽然第一个字母能实现大写，但是后面的字母就都会变成小写）
    name = "zhangSan and Lisi"
    name01 = name[0]
    name02 = name[1:]
    print(name01.upper() + name02)

    习题04：仅首字母大写
    name = "zhangSan and Lisi"
    print(name.replace("z","Z",1))

    习题05：使用for循环和while循环遍历打印字符串
    name = "abcdef"
    for c in name:
        print(c)

    习题06：使用for循环和while循环遍历打印字符串
    name = "abcdef"
    count = 0
    while count < len(name):
        print(name[count]) # 打印索引位，输出的是每个索引对应的字符串
        count = count + 1

    习题07：使用for循环，倒计时 3、2、1 出发
    s = "321"
    for c in s:
        print(c)
    else:
        print("出发")

    习题08：实现一个整数加法计算机（例如：1+3）
    s = input("请输入内容:")
    c = s.split("+") # 使用s.split()参数，删除+，之后输出的为列表
    c1 = c[0]
    c2 = c[1]
    d1 = int(c1)
    d2 = int(c2)
    print(d1 + d2)

    习题09：判断输入的内容有多少数字
    s = input("请输入内容:")
    count = 0
    for  c in s:
        if c.isdigit():
            count = count + 1
    print(count)

    习题10：1-2+3-4...+99 去掉 88
    count = 1
    sum = 0
    while count < 100:
        if count == 88:
            count = 89
            continue
        if count % 2 == 0:
            sum = sum - count # 偶数相减
        else:
            sum = sum + count
        count = count +1 # 奇数相加
    print(sum) # 输出sum

    习题11：判断输入的内容是否是回文
    s = input("输入内容：")
    s1 = s[::-1] 
    if s == s1: # 将输入的内容倒过来并与原文对比
        print("是回文")
    else:
        print("不是回文")

    习题12：判断输入的内容包含多少数字，大写字母、小写字母、其它
    content = input("输入内容")
    digit = 0
    upper = 0
    lower = 0
    other = 0
    for c in content:
        if c.isdigit():
            digit = digit + 1
        elif c.isupper():
            upper = upper + 1
        elif c.lower():
            lower = lower + 1
        else:
            other = other + 1
    print(digit)
    print(upper)
    print(lower)
    print(other)

    习题13：格式化输出
    name = input("name:")
    address = input("address:")
    hobby = input("hobby:")
    print("{name}在{address}{hobby}" .format (name = name ,address = address , hobby = hobby))

    习题14：循环打印，张、张三、张三三
    s = "张三三"
    ss = ""
    for c in s:
        ss = ss + c
        print(ss)
    
    习题15：输入ABC选择输出对应的出行方案
    while True:
    lu = input("输入ABC选择对应的出行方案:").upper().strip()
    if lu == "A":
        content = input("公交车还是步行")
        if content == "公交车":
            print("10min")
            break
        elif content == "步行":
            print("20min")
            break
        else:
            print("不知道")
    elif lu == "B":
        print("走小路回家")
        break
    elif lu == "C":
        print("绕路回家")
        content = input("去哪里？")
        if content  == "网吧":
            print("2小时到家")
        else:
            print("1小时到家")
    else:
        print("输错了")


1. 列表 - 索引、切片、步长
    列表可以存放多种类型数据
    列表同样适用索引、切片、步长，并且操作方法与字符串一致
    列表中的元素是可以直接改变，这里与字符串不同
    示范01：
    lst = ["str",1,True,["嵌套"]] # 存放多种类型数据
    print(lst[0]) # 索引
    print(lst[:3]) # 切片
    print(lst[::-2]) # 步长

    lst[0]= "字符串"   # 列表可以直接修改
    print(lst)


2. 列表 - 增加
    lst.append(元素) # 末尾增加一个元素
    lst.insert(位置，内容) # 指定位置插入一个元素
    lst.extend([元素]) # 迭代添加（添加多个元素）


    示范01：
    lst = ["周杰伦", "王力宏", "周润发"]
    lst.append("伍佰") # 列表 末尾 增加一个新的元素,输出：['周杰伦', '王力宏', '周润发', '伍佰']
    print(lst)
    lst.insert(1,"张三") # 指定位置插入一个新的元素，输出：['周杰伦', '张三', '王力宏', '周润发', '伍佰']
    print(lst)
    lst.extend(["lisi","wangwu"]) # 迭代添加，相比lst.append(),末尾可以添加多个元素,输出：['周杰伦', '张三', '王力宏', '周润发', '伍佰', 'lisi', 'wangwu']
    print(lst)

    示范02：录入学生姓名，之后打印
    lst = []
    while True:
        name = input("录入姓名:")
        if name.upper() == "Q":
            break
        else:
            lst.append(name) # 把录入的姓名添加到列表中
    print(lst)


3. 列表 - 删除
    lst.pop(索引) # 默认删除最后一个元素，也可以指定索引位置进行删除
    lst.remove(元素) # 删除指定元素
    del lst[其实位置:结束位置] # 切片删除
    lst.clear() # 清空所有元素


    示范01：
    lst = ["zhangsan","lisi","wangwu","zhaoliu"]
    e = lst.pop() # 默认删除最后一个元素
    print(e) 
    print(lst)
    e1 = lst.pop(1) # 删除指定索引位置的元素
    print(e1)
    print(lst)

    示范02：
    lst = ["zhangsan","lisi","wangwu","zhaoliu"]
    e1 = lst.remove("lisi") # 删除指定元素
    print(lst)

    示范03
    lst = ["zhangsan","lisi","wangwu","zhaoliu"]
    del lst[1:] # 切片删除
    print(lst)

    示范04
    lst = ["zhangsan","lisi","wangwu","zhaoliu"]
    lst.clear() # 清空
    print(lst)

4. 列表 - 修改
    lst = ["zhangsan","lisi","wangwu","zhaoliu"]
    lst[0] = "ZS" # 索引修改,输出为：['ZS', 'lisi', 'wangwu', 'zhaoliu']
    print(lst)
    lst [1:3] = "MQ"  # 切片修改，迭代修改，输出为：['ZS', 'M', 'Q', 'zhaoliu']
    print(lst)
    lst [1:3] = ["周杰伦", "他媳妇", "王力宏"] # 切片修改，修改为新的元素，输出为：['ZS', '周杰伦', '他媳妇', '王力宏', 'zhaoliu']
    print(lst)

5. 列表 - 查询
    示范01：使用for循环遍历每一个元素
    lst = ["zhangsan","lisi","wangwu","zhaoliu"]
    for c in lst: # for循环遍历查询
        print(c)

    示范02：
    lst = ["王尼玛", "我记着你", "伟哥", "放学天台见","王尼玛", "王尼玛"]
    print(len(lst)) # 打印元素的个数
    print(lst.count("王尼玛")) # 查询"王尼玛"总计出现了几次

6. 列表 - 排序
    lst.sort() # 升序
    lst.soft(reverse=True) # 倒序

    示范01
    lst = [1,8,23,10,15]
    lst.sort() # 升序
    print(lst)
    lst.sort(reverse=True) # 倒序
    print(lst)

7. 列表 - 嵌套
    定位元素：lst[元素][子元素]
    列表可以进行嵌套
    lst[3][1].append("user001") # 追加新的元素
    lst[2] = lst[2].capitalize() # 更改元素内容,字符串本事是不可变对象，如果直接引用lst[2].capitalize() 是不能直接修改的，所以应该是修改完再复值回去，及s[2] = [2].capitalize()
    lst[1] = lst[1].replace("白","黑") # 更改元素内容

    lst = [1, "太白", "wusir", ["麻花疼", ["可口可乐"], "王剑林"]]
    print(lst[3][1][0]) #输出：可口可乐

    lst[3][1].append("user001") # 添加新的元素。输出：[1, '太白', 'wusir', ['麻花疼', ['可口可乐', 'user001'], '王剑林']]
    print(lst)
    lst[2] = lst[2].capitalize() # 更改元素。输出：[1, '太白', 'Wusir', ['麻花疼', ['可口可乐', 'user001'], '王剑林']]
    print(lst)
    lst[1] = lst[1].replace("白","黑") # 输出为：[1, '太黑', 'wusir', ['麻花疼', ['可口可乐'], '王剑林']]
    print(lst)

8. 元组
    不可变的列表，以括号"（）"表示，以逗号","隔开
    
    示范01：
    lit = (1,False,"花生")
    print(lit[2:]) # 列表可以查询
    lit[2] = "大豆" # 不允许修改，会直接报错

    示范02：支持for循环遍历查询
    lit =(1,False,"花生",[23])
    for c in lit:
        print(c)

    示范03
    lit =(1,False,"花生",[23])
    print(lit[3])
    lit[3].append("zhangsan") # 列表本身不可修改，但当列表中的元素为可更改对象时，则可以进行修改
    print(lit)

9. for循环中的Range
    for c in range(10): # 输出：0.1.2.3.4...9
    print(c)

    for c in range(2,8): # 输出2.3.4...7，同样遵循"骨头不顾腚"原则
    print(c)

    for c in range(2,8,2): 输出2、4、6 ，同样适用 步长 
    print(c)

    for c in range(10,-10,-5):输出：10.5.0.-5,同样可以倒着取
     print(c)

    #计算1-2+3-4....+99-100
    sum = 0
    for c in range(1,101):
        if c % 2 == 0:
            sum = sum - c 
        else:
            sum = sum + c
    print(sum)


第五章 重点回顾

1. 字典 - 增加
    dic[key] = value # 直接增加，如有key已存在，则替换
    dic.setdefault(key,value) # 增加，如果key已存在，则不添加

    示范01：
    dic = {"name01":"zhangsan","name02":"lisi"}
    dic["name03"] = "wangwu" # 直接增加
    print(dic)
    dic["name03"] = "wangwu02" # 内容重复会替换
    print(dic)

    示范02：
    dic.setdefault("name04","zhaoqi") # 增加
    print(dic)
    dic.setdefault("name04","zhaoqi02") # 内容重复不会替换
    print(dic)

2. 字典 - 删除
    dic.pop(key) # 删除元素，同时会返回被删除的value
    dec dic[key] # 直接删除
    dec.popitem() # 随机删除，但是被删除的元素，以元组形式放回

    示例01：
    dic = {'name01': 'zhangsan', 'name02': 'lisi', 'name03': 'wangwu02', 'name04': 'zhaoqi'}
    ret = dic.pop("name04")
    print(ret) # 会删除元素，同时返回被删除的value
    print(dic)

    示例02：
    del dic["name03"] # 直接删除，没有返回
    print(dic)

    示例03：
    ret2 = dic.popitem() # 随机删除，但是会以元组形式返回被删除的元素
    print(ret2)
    print(dic)

3. 字典 - 修改
    dic[key] = dic[key] +-*/ int  #对value为int的数据做运算
    dic1.update(dic2) #用字典dic2的内容替换字典dic1，如果key存在则替换，不存在则新增

    示例01：
    dic = {"id":1, 'name':'李嘉诚', 'money':10000000}
    dic["money"] = dic["money"]  - 1000 # 直接用key去修改
    print(dic)


    示例02：
    dic1 = {1:"zhangsan",2:"lisi",3:"wangwu"}
    dic2 = {1:"zhangsan001",4:"liliu",5:"zhaoqi"} # 用dic2的内容替换dic1，如果key存在则替换，不存在则新增
    dic1.update(dic2)
    print(dic1)

4. 字典 - 查询
    print(dic[key]) #直接查询，如果key存在则返回value，如果不存在，则报错
    print(dic.get(key)) # 查询，如果不存在则返回Nona
    print(dic.get(key,"不存在")) # 查询，如果不存在可以指定返回的默认值

    示例01
    dic = {"及时雨":"宋江","黑旋风":"李逵","小李广":"花容"}
    dic["智多星"] = "吴用" # 直接新增
    print(dic)
    dic["小李广"] = "花容02" # 等同赋值操作，直接修改
    print(dic)

    示例02：
    print(dic["及时雨"]) # 直接查询，如果存在则返回value，如果不存在，直接报错

    示例03：
    print(dic.get("黑旋风")) # 直接查询，如果存在则返回value，如果不在村返回None

    是例04：
    print(dic.get("黑旋风00001","不存在")) #  直接查询，如果存在则返回value，如果不存在，可以指定返回值

5. 关于dic.setdefault()
    1. 首先判断原来的字典中有没有这个key . 如果没有. 执行新增
    2. 用这个key去字典中查询, 返回查到的结果

    示例01：   
    dic = {"及时雨":"宋江","黑旋风":"李逵","小李广":"花容"}
    dic.setdefault("大刀", "关胜") # 新增
    dic.setdefault("大刀", "关胜01") # key重复不增加
    print(dic)

    示例02：
    ret = dic.setdefault("豹子头","林冲") #  如果没有新增，并再去字典中查询返回新增的value
    print(ret) 
    print(dic)


6. 常用操作
    print(dic.keys()) # 打印所有key，返回key的集合,即:dict_keys(['key01', 'key02', 'key03']),可遍历
        for key in dic.keys(): #可遍历，返回所有key

    print(dic.values()) #打印所有value，返回key的集合,即:dict_values(['value01', 'value02', 'value03'])，
        for value in dic.values() #遍历，返回每一个value

    print(dic.items())  # 打印所有键值对，dict_items([('k01', 'v01'), ('k02', 'v02'), ('k03', 'v03')])，
        for item in dic.items() # 遍历，返回每一组键值对(key,value)

    示范01：
    dic = {"及时雨":"宋江","黑旋风":"李逵","小李广":"花容"}
    print(dic.keys()) # 打印所有key，返回key的集合,即:dict_keys(['及时雨', '黑旋风', '小李广'])
    for key in dic.keys(): # 遍历，返回每一个key
        print(key)

    示范02：
    print(dic.values()) # 打印所有value，返回key的集合,即:dict_values(['宋江', '李逵', '花容'])
    for value in dic.values(): #遍历返回每一个value
        print(value)

    示范03：
    print(dic.items()) # 打印所有键值对，dict_items([('及时雨', '宋江'), ('黑旋风', '李逵'), ('小李广', '花容')])
    for item in dic.items(): # 遍历返回每一组键值对(key,value)
        print(item) # 
        print(item[0]) # 输出所有key
        print(item[1]) # 输出所有value


7. 解构
    a,b = 1,2
    print(a) # 1
    print(b) # 2
    print(a,b) # 1 2

    a = 1,2
    print(a) # 输出为元组(1,2) 

    a,b = (1,2)
    print(a) # 1
    print(b) # 2
    print(a,b) # 1 2

    a,b = [1,2]
    print(a)
    print(b)


    示范01
    dic = {"及时雨":"宋江","黑旋风":"李逵","小李广":"花容"}
    #print(dic.items()) 

    #for item in dic.items(): #遍历，输出的是(key,value)
        #print(item)

    #for item in dic.items(): #使用解构方式，遍历
        #k,v = item 
        #print(k,v) 输出的是key,value，而非列表
        #print(k)
        #print(v)

    for k,v in dic.items():  # 依然为解构原理
        print(k)
        print(v)


8. 列表嵌套
    1. 字典的嵌套，指的实在value层级上进行嵌套，可以继续嵌套dict，也可嵌套list等
    2. 多层级的打印，为print(dic[key01][sub-key001]),或者print(dic[key01][索引位置][sub-key001])

    示范01
    dic = {
        "name":"汪峰",
        "age":58,
        "wife":{ # 嵌套字典
            "name":"章子怡",
            "age":37,
            "salary":100000
        },
        "children":[ # 嵌套元组
            {"name":"老大","age":18}, # 元组里面继续放字典
            {"name":"老二","age":10}
        ]

    }

    print(dic["children"][1]["age"]) # 打印二儿子的年纪
    print(dic["wife"]["salary"]) # 打印汪峰爱人的工资

9. 字典的for循环
    dic = {"及时雨":"宋江","黑旋风":"李逵","小李广":"花容"}
    for c in dic:
        print(c) # 直接拿是key
        print(dic[c]) # 此时拿到是的是value

'''











 






