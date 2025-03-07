#九九乘法表的实现
"""
思路1：首先x*y=z，应该有三个变量，循环限制条件应该由x和y控制
每次运算后输出计算结果
print(end='')输出不换行, \t制表符，使多行字符串对齐
"""
x=0
z=0
while x<9:
    x+=1
    y=1   
    while y<=x:
        z=x*y
        print(f'\t{x}*{y}={z} ', end='')
        y+=1
    print('\n')
"""
思路2：九九乘法表的标准排列类似金字塔，可以通过数值和行的关系进行生成
需要使用2个变量: x, y
"""
# 定义变量
x=0
# 控制行，执行换行
while x<9:
    x+=1
    y=0
    # 控制每行个数，内层不换行且控制对齐
    while y!=x:
        y+=1
        print(f'\t{y}*{x}={x*y}', end='')
    # 也可以空内容，即为换行   
    print()
# for和while嵌套
# 外层，即行的控制
for row_value in range(1, 10):
    column_value=0
    # 重要关系，每行的列数等于所在行
    while column_value<row_value:
        column_value+=1
        print(f'\t{column_value}*{row_value}={column_value*row_value}', end='')
    print()
# for循环
for row_value in range(1, 10):
    for column_value in range(1, row_value+1):
        print(f'\t{column_value}*{row_value}={column_value*row_value}', end='')
    print()
#################################################################################
#################################################################################

# 数数字符
name=input('输入你要统计字符的文字：')
count=0
find_A=input('输入你要查找的字符：')
# in 覆盖过程
for find_a in name:
    if find_a==find_A:
        count+=1
"""
输出是s的个数，因为find_a存放的是遍历name的内容
print('在你给出的表述中，%s的个数为:%d' %(find_a, count))
并且根据变量作用域原则，这是不规范的，虽然可以访问到
"""
print('在你给出的表述中，%s的个数为:%d' %(find_A, count))
# 有几个偶数
print('输入你要统计偶数个数的区间：')
num1=int(input('左闭区间：'))
num2=int(input('右开区间：'))
count=0
for find_even in range(num1, num2):
    # 寻找偶数，余2为0
    if (find_even%2)==0:
        count+=1
print('在你给定区间内，偶数的个数为：%d' % count) 
