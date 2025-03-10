# 切片操作
# 方法1
my_str="大乃容有, 学大川四, 川百纳海"
# 得到四川大学
new_str=my_str[-7:-11:-1]
print(new_str)
# 方法2
    # 取出列表
my_new_str=my_str.split(", ")
index=my_new_str.index("学大川四")
my_new_str1=my_new_str[index][::-1]
print(my_new_str1)
# 方法3
result=my_str[::-1][6:10]
print(result)

# 列表去重
my_list=[ 1, "list", "python", 23423, True, False, 1, 0]
my_set=set()
for element in my_list:
    my_set.add(element)
print(my_set)

"""
员工升职加薪
字典操作
"""
employee_infor={
    "马吼吼":{
        "apartment":'科技部',
        "salary":3000,
        "level":1
    },
    "牛哞哞":{
        "apartment":'市场部',
        "salary":5000,
        "level":2
    },
    "猪噜噜":{
        "apartment":'科技部',
        "salary":4000,
        "level":1
    },
    "羊咩咩":{
        "apartment":'市场部',
        "salary":7000,
        "level":3
    },
}
print(f'全体员工当前信息如下：\n{employee_infor}')
for i in employee_infor:
    # 得到员工的级别
    level=employee_infor[i]["level"]
    # 判断员工级别
    if level==1:
        # 升职加薪
        employee_infor[i]["salary"]+=1000
        employee_infor[i]["level"]+=1
print(f'全体级别为1的员工完成升职加薪后，员工信息为：\n{employee_infor}')
