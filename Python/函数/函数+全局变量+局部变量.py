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
"""
# 函数初定义
# 形式参数：a,b,c
def my_personal_infom(a, b, c):
    print(f"""您就读于{a}, 将获得{b}学位, 你的Email为{c}""")
    formal_message=f'您在{a}就读'+f'将获得{b}学位'+f', 你的个人Email为{c}'
    return formal_message
    print('return后的语句是不会执行的')
# 调用
# 实际参数
# 返回值可以不使用
my_personal_infom('不知道', 6, 6)

# 带参数调用
# 输入实际参数
a=input('请输入学校:') 
b=input('请输入学历:')
c=input('请输入邮箱:')
actual=my_personal_infom(a, b, c)
print(actual)
print(my_personal_infom(a, b, c))

