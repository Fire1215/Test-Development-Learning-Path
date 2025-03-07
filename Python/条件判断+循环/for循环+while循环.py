"""
循环语句
while语句(小于等于时条件会大1)
    while 条件：
        满足可做1
        满足可做2
        循环条件有限性
 while循环嵌套, 类似if嵌套, 注意空格
for语句(轮询机制, 对一批内容进行逐个处理)
    for 临时变量 in 序列类型: # 将序列类型中的内容依次取出覆盖临时变量
        循环满足条件时执行的代码
 for循环无法定义循环条件, 由于数据集不可能无限大, 不会无限循环
    range(num) 获取一个从0开始, 到num结束的数字序列(不含num)
    range(num1, num2) 获取从num1开始到num2结束的数字序列(不含num2)
    range(num1, num2, step) 以步长为step(默认1), 获取从num1到num2的数字序列(不含num2)
    变量作用域
 for循环嵌套, 空格缩进控制

for循环和while循环可以相互嵌套
continue和break
 continue 中断本次循环，进行下一次循环(只针对所在循环)
    可用于for和continue
 break 跳出循环(只针对所在循环)
"""
# while循环基础运用
i=1
while i<=100:
    print('长期主义')
    i+=1
print(i)
# 从1加和到100
j=1
x=0
while j<=100:
    x+=j
    j+=1
print(j, x)

# while嵌套
# 假设有1000个字，每天练5个，要用上多少天练完
# 同时每天读10面书，能看多少面
sum=1000
k=0
page=0
while sum>0:
    sum=sum-5
    k+=1
    s=0
    while s<10:
        s+=10
        page+=s
print(f'你过关！用了{k}天,同时你完成了{page}面书的阅读')
###########################################################################
###########################################################################
# for循环
name="Sichuan University"
for spelling in name:
    print(spelling, ' ', end='')
# range语法
for i in range(0, 15, 3):
    print(i)
# 变量作用域
for i in range(5):
    print(i)

print(i)

# for嵌套
# 假设有1000个字，每天练5个，要用上多少天练完
# 同时每天读10面书，能看多少面
count_day=0
count_page=0
for i in range(0, 1000, 5):
    count_day+=1
    for j in range(0, 10):
        count_page+=1
print(f'你过关！用了{count_day}天,同时你完成了{count_page}面书的阅读') 
