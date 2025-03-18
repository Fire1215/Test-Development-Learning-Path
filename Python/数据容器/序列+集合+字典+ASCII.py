"""
序列 列表、元组、字符串均可视为序列, 可接在其他语句后
 操作
    切片 从序列中取出子序列(不影响序列本身)
     序列[起始下标:结束下标:步长]
      起始下标留空表示从头开始
      结束下标不包含, 但留空时表示到结尾，此时可以取到
      步长1表示逐个取, 步长n表示每次隔n-1个元素取(默认为1)
      步长负数表示反向取，同时下标也要反向
集合 不支持元素重复(自动去重)，无序(操作后顺序不固定)
     不支持下标索引
 {元素, 元素, ……}; 变量={元素, 元素, ……}
      空集合: 变量=set()
      不支持嵌套
 操作
    集合.add(元素) 将元素添加至集合中任意位置
    集合.remove(元素) 移除元素
    集合.pop() 随机弹出元素，有返回值
    集合.clear() 清空集合
    集合1.difference(集合2), 取集合差集(1有而2没有的),得到新集合且1, 2不变
    集合1.difference_update(集合2), 删除集合1中与集合2相同的元素
    集合1.union(集合2) 集合1与集合2合并得到新集合, 1,2不变, 注意自动去重
    len(集合) 注意自动去重
    集合只能for循环遍历

字典 存储元素是键值对，通过关键信息(key)找到对应信息值(value)
 {key:value, key:value, ……};    变量={key:value, key:value, ……}
 空字典: 变量={}/dict();    定义重复key:不允许！重复了找靠后的值
 key和value可以使任意数据类型, 但key不可作为字典(字典可以嵌套)
 操作
    取值 字典.[key][key]
    新增(更新)元素 字典[key]=value
    删除元素 字典.pop(key) 获得指定key的value,同时该键值对从字典删除(有返回值)
    清空字典 字典.clear()
    dict.get(key, default)获取dict中对应key的value，若不存在key，则返回默认值
    获取字典中全部的key 字典.keys() 有返回值(只能顶层操作)
        可结合for循环遍历字典
      for key in 字典:(挨个得到key)
    统计元素数量 len(字典)

数据容器
    max(容器)，取容器中最大元素
    min(容器)， 取容器中最小元素
    转换 list(容器)，tuple(容器)，str(容器)，set(容器)
        字典转字符串，key和value都能保留下来
    对容器进行升序排序 sorted(容器, [reverse=1]) reverse默认为0
        !字典时，排的是key
        !排序结果均为列表

ASCII码（字符串比较是基于此,按位比较，只要有一位大整体就大）
    大小写字母：a-z(97-122),A-Z(65-90)
    数字：0-9(48-57)
    特殊符号


"""
my_list=["show python", 4, 6, 0]
# 全取出
new_list1=my_list[:]
# 全取出，隔一个取
new_list=my_list[::2]
print(new_list1, '\n', new_list)
# 对原序列进行反转取出 
new_list2=my_list[::-1]
print(new_list2)
#################################################################
# 集合
my_set={"大乃容有", "川百纳海", 2428, "大乃容有", "学大川四", "川百纳海", 2428,}
my_set_1={"大乃容有", "川百纳海", 2428, "大乃容有", 666}
empty_set=set()
print(my_set, empty_set)
# 位置不定
my_set.add(24258)
print(my_set)
new_set=my_set_1.difference(my_set)
print(new_set)
my_set_1.difference_update(my_set)
print(my_set_1)
##############################################################################
# 字典
my_dict={
    "name":{
        "Juanjuan Zhu":'今年26岁', "Moumou Niu":'今年25岁'
    },
    "age":26, 
    "phone number":{
        "J":1281598,
        "M":1281588
    }
}
print(f"""Juanjuan Zhu{my_dict['name']["Juanjuan Zhu"]}, 
电话为{my_dict['phone number']['J']}""")
keys=my_dict.keys()
print(keys)
print(len(my_dict))
#########################################################################
# ASCII码
print(f'abc大于Abcd: {'Abc'>'Abcd'}')

