#列表常用功能练习

my_list=[21, 25, 21, 23, 22, 20]
my_list.append(31)
my_list.extend([29, 33, 30])
list_1=my_list[0]
list_2=my_list[-1]
print(f'列表my_list={my_list}中第一个元素为{list_1}, 最后一个元素为{list_2}')
position=my_list.index(31)
print(position)
print(my_list)

# 取偶数
def list_while_func():
    n=0
    while n<len(my_list):
        element=my_list[n]
        n+=1
        if element%2==0:
            new_list_1.append(element)
    return new_list_1

def list_for_func():
    for element in my_list:
        if element%2==0:
            new_list_2.append(element)
    return new_list_2

new_list_1=[]
new_list_2=[]
print(f'while循环遍历列表my_list, 其中偶数组成的新列表为{list_while_func()}')
print(f'for循环遍历列表my_list, 其中偶数组成的新列表为{list_for_func()}')


# 分割字符串
my_str="itheima itcast boxuegu"
count=my_str.count('it')
new_str=my_str.replace(' ', '|')
print(new_str)
str_list=new_str.split('|')
print(f'字符串my_str中, 字符串"it"的个数为{count}, 按|分割后，得到{str_list}')
