"""
数据容器 可容纳多份数据(元素)的数据类型 (2^[63]-1个)
    根据存放元素不同分为: 列表、元组、字符串、集合、字典
 列表
        [元素1, 元素2, ……]; 变量=[元素1, 元素2, ……]
    正向索引                     [0]    [1]
    反向索引                     [-*]   ……   [-1]  
        空列表: 变量=[]/list()
        支持嵌套 [[元素1, 元素2……], [元素1, 元素2……]]
    索引        [0][0]  [0][1]    [1][0]  [1][1]
    元素索引
        变量[下标索引]
    常用操作(内部存在一系列可供选择的函数) [了解有这些就行]
        将函数定义为class的成员, 该函数称为方法
        格式
        class Student:
            def add(self, x, y):
                return x+y
        调用
        student=Student()
        num=student.add(1, 2)
        
        查询功能 指定函数在列表的下标, 查找第一个出现的(只能查询顶层元素)
         列表.index(元素)
         index就是列表对象内置的方法
        修改元素值
         列表[下标]=值
        插入元素 在指定下标位置插入元素(只能操作顶层元素)
         列表.insert(下标，元素)
        追加元素 将指定元素追加到列表尾部
         列表.append(元素) 元素整个追加
         列表.extend(其他数据容器) 将其他数据容器内容取出，依次追加到列表尾部
        元素删除
         del 列表.[下标]
         列表.pop(下标) 可得到返回值(只能操作顶层元素)
         列表.remove(元素) 删除某元素在列表中第一个匹配项(只能操作顶层元素)
        清空列表
         列表.clear() (只能操作顶层元素)
        统计某元素在列表内的数量
         列表.count(元素)(只能操作顶层元素)
        统计列表中有多少元素
         len(列表)
    遍历列表元素
        while循环 通过列表[下标]取出
         index=0
         while index<len(list):
            index+=1
        for 临时变量 in 数据容器:
            对临时变量进行处理

 元组  一旦定义完成便不可修改, 但有列表，其内的元素可以更改
       若只有一个数据，后面需要添加逗号
    (元素1, 元素2, ……); 变量=(元素1, 元素2, ……)
    空元组: 变量=[]/tuple()
    支持嵌套, 索引: 元组[*][*]
    操作
        元组.index(); 元组.count(); len(元组)
        while, for遍历
 字符串 无法修改的数据容器,只可以存储字符串
    索引方法同列表
    操作
     新字符串=字符串.replae(字符串1, 字符串2)
        将字符串内的 全部 字符串1替换为字符串2
     新字符串=字符串.split(分隔符字符串)
        将字符串划分为多个字符串，并存入列表中
     去字符串首尾字符串
        字符串.strip() 不传参数，删首尾空格
        字符串.strip(字符串) 删首尾字符小串
     统计字符串出现次数
        字符串.count(字符串
     while, for遍历
"""
# 列表
my_list=[ [1, "list", "python"], [23423, True, False] ]
print(my_list[0])
# 正向索引
print(my_list[0][2])
# 反向索引
print(my_list[-1][-2])
print(type(my_list))
    # 查询
"""
index()方法只能查找顶层元素, 而23423位于第二个子列表内部, 并非顶层元素
index=my_list.index(23423)
print(f'"23423"在列表中的索引值为{index}')
"""
index=my_list.index([1, "list", "python"])
print(f'嵌套列表"[1, "list", "python"]"在列表中的索引值为{index}')
    #修改
my_list[0][2]="show time"  # 将"python"改为"show time" 
print(my_list)
    #插入
student="1"
my_list.insert(1, student)
print(my_list)
    #追加
a = [1, 2]
b = []
b.append(a)  # b 变为 [[1, 2]]
print(f'此时b列表为:{b}')
# b.append(a) 实际存储的是 a 的引用，因此后续修改 a 会影响 b 的内容
a.append(3)  # a 变为 [1, 2, 3]，b 同步变为 [[1, 2, 3]]
print(a, f', 此时b列表为:{b}')
my_list.extend(a)
print(my_list)
    #删除
del my_list[-4][-3]
print(my_list)
my_list_copy=my_list.pop(-2) #这不是列表
print(my_list_copy)
print(my_list)
# True等价于1
my_list.remove(True)
my_list.remove(3)
print(my_list)
    # 清空
b.clear()
print(b)
    #统计某元素数量
num=my_list.count('1')
print(num)
    #统计列表中有多少元素
sum=len(my_list)
print(sum)
print(my_list)

#遍历列表
    #while
def list_while_func():
    n=0
    while n<len(my_list):
        my_list_1=my_list[n] # 不出现'1'，因为弹出列表[0]后，'1'的位置变为列表[0]
        print(my_list_1)
        n+=1
    return()
    #for
def list_for_func():
    for n in my_list:
        print(n)
list_while_func()
list_for_func()
###############################################################################
###############################################################################
#元组
t1=((2, 3, 5), 4, 6, 9)
#从元组中取出5
x=t1[0][2]
print(x)

"""
元组不可修改
t1[1]="3"
"""
t2=([8, 2, 4], (12, "元组"))
# 元组中的列表内的元素可以修改
t2[0][2]=6
print(t2)

# 练习
t=('卷卷', 11, ['football', 'music'])
print(f'年龄所在的索引为:{t.index(11)}')
name=t[0]
print(f'该学生的姓名为:{name}')
del t[-1][-2]
t[2].append('coding')
print(t)
##############################################################################
##############################################################################
# 字符串
my_str="my name is juan'juan' Zhu!"
letter=my_str[9]
letter1=my_str[15]
print(letter, letter1)
index=my_str.index("j")
print(index)
    #替换
new_str=my_str.replace('juan', 'JJ')
print(new_str)
    #切分
my_str_list=my_str.split(' ')
print(f'my_str经空格切分后, 得到{my_str_list}')
    #规整
my_new_str=" my name is juan juan Zhu21"
# 去首尾空格
my_new_str_1=my_new_str.strip()
# 去字符串,被划分为了两个子串'1','2'
my_new_str_2=my_new_str.strip("12")
print(my_new_str_1, '\n', my_new_str_2)
    #统计字符串
count=my_new_str_2.count('a')
print(count)