"""
字符串定义（单引号、双引号、三引号）

字符串的拼接
字面量和变量的拼接，变量和变量的拼接
!字符串格式化，占位拼接%s %d %f,分别代表字符串、整数、浮点数
格式化的精度控制, %10.2f, 保留两位小数, 宽度限制10(宽度小于不生效，小数四舍五入)
快速字符串格式化,f"{变量名} {变量名}"(不关注类型，不关注精度)

表达式的格式化, 表达式指一条具有明确执行结果的代码语句(1+1, type())

获取键盘输入
input语句,获取的始终为字符串
"""
example="""三引号可以定义多行字符串, 若不用变量接收，则可以用来注释"""
exa_type=type(example)
print(example, '\n', exa_type)

# 字符串内包含单引号或双引号，使用转义字符“\”
introduction="我是川大研二的'卷卷'"
introduction2='我是川大研二的"卷卷"'
introduction3="我是川大研二的\"卷卷\""
print(introduction, "\n", introduction2, "\n", introduction3)
##################################################################
##################################################################
# 字面量之间拼接
print("四川大学"+"位于"+"成都"+"一环路南二段上")
# 变量之间拼接
school="四川大学,"
place="处于成都"
road="一环路南一段上"
Zip_code="610065"
tel=28854012340
print("我在"+school+place+road+ ", 邮编为"+Zip_code+", 联系电话为:"+str(tel))

# 数字转为字符串，相当于str(tel)
message1="我在%s%s%s, 邮编为%s, 联系电话为%d" % (school, place, road, Zip_code, tel)
print(message1)

"""
print("我在"+school+place+road+",邮编为"+Zip_code+ ",联系电话为"+tel) 
类型错误,无法和非字符串拼接
"""

# 占位符拼接
zip_code=610065
message="邮编为: %s, 联系电话为: %s" %(zip_code, tel)
print("我在"+school+place+road+", "+message)

# 格式化的精度控制
stock_price=10.24523
stock_num=9910
print("股票价格为：%5.2f, 股票号为：%5d" % (stock_price, stock_num))
print("股票价格为：%3.2f, 股票号为：%3d" % (stock_price, stock_num))

# 快速字符串格式化
print(f"股票价格为: {stock_price}, 股票号为: {stock_num}")
##################################################################
##################################################################
# 表达式的格式化
print(f"2的3次方为: {2**3}")
print("2的3次方为: %d" % 2**3)
print("'四川大学'在Python中的类型名为: %s" % type('四川大学'))
##################################################################
##################################################################
# input语句
print("say my name!")
name=input()
"""等价于
name=input("say my name!\n")
"""
# 可增加条件判断语句，从而对数据进行转换 
name=int(name)
print("yeah! %d" %name, type(name))
