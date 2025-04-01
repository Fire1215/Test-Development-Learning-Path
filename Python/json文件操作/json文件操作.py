"""
json文件
  介绍：
    其为独立于语言的轻量级纯文本文件，可以直接使用read（）和write（）方法去操作，但不方便
    常用在做测试时，将数据定义为json文件格式，使用代码读取json文件，即读取测试数据，进行传参（参数化）
    数据交换格式，后端给前端的数据（json，html，xml）
  基本语法规则
    后缀*.json，主要数据对象为，对象{}(类似python中的字典)和数组[]（类似列表），可相互嵌套
    一个json文件是一个对象或数组（最外层要么是｛｝，要么是[] ）
    json对象是由键值对组成，类似python，字符串必须使用双引号""
    数字类型--->int float
    string字符串--->str
    布尔类型 true false（小写）
    null代表python中的None
  读取json文件
    导包 import json
    以读方式打开文件
    读文件  json.load(文件对象)
        返回的是 字典（若文件内是对象） 列表（文件内为数组）
  写入json文件
    导包
    以写方式打开文件
    写入文件 json.dump(python中的数据类型, 文件对象)
"""
import json     #导入

# 读方式打开文件
# with open('Python\print_13_json.json', encoding='UTF-8') as my_file:
    # # 读取文件
    # info=json.load(my_file)
    # print(type(info))
    # # 姓名
    # print(info.get('name'))
    # # 年龄
    # print(info.get("address").get("country"))
my_list=[ [1, "list", "神"], [23423, True, False] ]
# 以写方式打开文件
with open('Python\print_13_json.json', 'w', encoding='UTF-8') as my_file:
    # json.dump(my_list, my_file, ensure_ascii=False) # 直接显示中文，不以ASCII码显示
    json.dump(my_list, my_file, ensure_ascii=False, indent=2) # 直接显示中文，不以ASCII码显示，缩进2
