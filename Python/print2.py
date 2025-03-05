"""
主要内容：
数据类型
type()查看字符类型(查看的是变量存储数据的类型)，会给出结果即有返回值
变量无形数据有型

！数据类型转换
任何类型都可以转换为字符串，但是字符串不一定能转换为其他类型，转换时
需保证字符串内容为数字

标识符（用以给变量、类、方法等命名）-由字母、中文（不建议）、数字、
下划线组成，不能以数字开头

！算术运算符
+、-、*、/、%、**、// 含义分别代表加、减、乘、除、取余、幂、取整
！赋值运算符
=、+=、-=、*=、/=、%=、**=、//= 含义分别代表赋值、加后赋值、减后赋值、
乘后赋值、除后赋值、取余后赋值、幂后赋值、取整后赋值
比较运算符
==、!=、>、<、>=、<= 含义分别代表等于、不等于、大于、小于、大于等于、小于等于
逻辑运算符
and、or、not 含义分别代表与、或、非
成员运算符
in、not in 含义分别代表在序列中、不在序列中
身份运算符
is、is not 含义分别代表是、不是
位运算符
&、|、^、~、<<、>> 含义分别代表按位与、按位或、按位异或、按位取反、左移、右移
"""
# print直接输出类型信息
print(type("hello world"))
print(type(10))
print(type(666.6))
# 使用变量存储type语句结果
str_type=type("hello world")
int_type=type(10)
float_type=type(666.6)
print(str_type)
print(int_type)
print(float_type)
# type()查看变量类型
money=130
name_type=type(money)
print(name_type)
##############################################################
##############################################################
# 数据类型转换
# 字符转字符串
int_to_str=str(10)
print("值为：", int_to_str, "类型为：", type(int_to_str))
float_to_str=str(666.6)
print("值为：", float_to_str, "类型为：", type(float_to_str))
# 字符串转数字
str_to_int=int("10")
print("类型为：", type(str_to_int), "值为：", str_to_int)
str_to_float=float("666.6")
print("类型为：", type(str_to_float), "值为：", str_to_float)

"""
str_to_int=int("hello world")
print("类型为：", type(str_to_int), "值为：", str_to_int)
错误的，转换时需保证字符串内容为数字
"""
# 数字转数字
int_to_float=float(10)
print("类型为：", type(int_to_float), "值为：", int_to_float)

float_to_int=int(666.6)
print("类型为：", type(float_to_int), "值为：", float_to_int) # 丢失精度
##############################################################
##############################################################
# 标识符
"""
关键字: python保留的关键字, 不能用作标识符,  有以下几种:
False、None、True、and、as、assert、break、class、continue、def、del、elif、
else、except、finally、for、from、global、if、import、in、is、lambda、nonlocal、
not、or、pass、raise、return、try、while、with、yield(有大小写之分)
"""
# 变量命名规范
""" 
1、明了 
2、简洁
3、下划线命名
4、字母全小写
"""
##############################################################
##############################################################
# 算术运算符
print("2的3次方:\n", 2**3)
# 赋值运算符
money=105
money//=11
print("除后取整的值为：", money)