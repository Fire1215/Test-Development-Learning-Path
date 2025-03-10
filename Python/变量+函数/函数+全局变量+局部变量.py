"""
函数的初识: 组织好的, 可重复调用的特定功能代码段
字符串是数据容器
函数需先定义后调用才能运行
 函数的定义语法
    def 函数名(传入参数): #无参数括号需保留
        函数体
        return 返回值
    参数、返回值可省略
    变量=函数(参数)
 函数的参数 接收外部提供数据(x,……,y)可以任意个, 可以不使用参数
 函数返回值 return 程序中函数完成任务后，返还调用者的结果
    函数体在return后结束, 后面语句不执行
    无返回可以return None
    若无return语句, 函数仍然存在返回值(None字面量, 返回的无意义内容)
    None可赋予变量
 函数说明文档
    函数说明
    :param x: 形参x的说明
    :return:  返回值的说明
 函数的嵌套调用 一个函数又调用了另一个函数
 局部变量 定义在函数体内部，只在函数体内部生效，调用完后被销毁
 全局变量 定义在函数体外部，在函数体及外部都可以用
   若在函数体内更改，只在函数体起临时作用，不影响全局
   global 变量 可在函数体内声明变量为全局变量

补充
 函数的多返回值
   return m, n  可以是任意数据类型
   接收 x, y=func()
 函数多重传参方式
   位置参数 讲究顺序
   关键字参数 键=值的形式，不受位置影响
   缺省参数 某参数在函数定义时已确定（写在最后面），传参时可以不写，写了覆盖默认值
   不定长参数 用于不确定调用时会传递多少个参数
      位置不定长 def func(*args) args为元组
      关键字不定长 def func(**kwargs) kwargs为字典
       传参形式需为键值对
 匿名函数
   函数作为参数传递（嵌套） 逻辑传递
   Lambda关键字 可以定义无名称函数
      lambda 传入参数: 函数体(只有一行代码)  默认有return,无法重复使用
"""
# 函数初定义
# 形式参数：a,b,c
def my_personal_infom(a, b, c):
    print(f"""您就读于{a}, 将获得{b}学位, 你的Email为{c}""")
    formal_message=f'您在{a}就读'+f'将获得{b}学位'+f', 你的个人Email为{c}'
    intro_message=f'我在{a}读{b}, 我的Email为{c}'
    return formal_message, intro_message
    print('return后的语句是不会执行的')
# 调用
# 实际参数
# 返回值可以不使用
# 位置参数调用
my_personal_infom('不知道', 6, 6)
# 关键字参数调用
my_personal_infom(b="硕士", a="四川大学", c="12815889")
# 带参数调用
# 输入实际参数
a=input('请输入学校:') 
b=input('请输入学历:')
c=input('请输入邮箱:')
actual1, actual2=my_personal_infom(a, b, c)
print(actual2)
print(actual1)
print(my_personal_infom(a, b, c))
##############################################################################
# 传递函数
def input_func():
   a=input('请输入学校:') 
   b=input('请输入学历:')
   c=input('请输入邮箱:')
   return a, b, c

# 逻辑不确定
def my_personal_infom(input_func):
    x, y, z=input_func()
    print(f"""您就读于{x}, 将获得{y}学位, 你的Email为{z}""")

my_personal_infom(input_func)

# lambda函数
def sum_func(compute):
    sum=compute(1, 2, 3)
    print(sum)
   
sum_func(lambda a, b, c: a+b+c)
