"""
正则表达式
    re模块 
      match
        re.match(匹配规则，被匹配字符串)
         从被匹配字符开始，匹配成功返回匹配对象，不成功返回空
      search
        re.search(匹配规则，被匹配字符串)
         搜索整个字符串，从前往后，找到第一个后停止
      findall
        re.findall(匹配规则，被匹配字符串)
         匹配整个字符串，找出全部匹配项，找不到返回[]

    !元字符匹配规则
        单字符规则有：
          .  匹配任意字符
          [] 匹配中括号中的任意一个字符
          找出全部英文字母 re.findall('[a-zA-Z]', 'abc123')  # ['a', 'b', 'c']
          \d 匹配数字
          \D 匹配非数字
          \s 匹配空白字符
          \S 匹配非空白字符
          \w 匹配单词字符 a-z A-Z 0-9 _
          \W 匹配非单词字符 找特殊字符
          re.findall('\d', 'abc123')  # ['1', '2', '3']
          字符串前加r，代表字符s中的转义字符无效，就是普通字符
          re.findall(r'\d', 'abc123')  # ['1', '2', '3']
        数量匹配规则有：
          * 匹配0次或多次
          + 匹配1次或多次
          ? 匹配0次或1次
          {n} 匹配n次
          {n,} 匹配n次或多次
          {n,m} 匹配n次到m次
        边界匹配规则有：
          ^ 匹配字符串开始位置
          $ 匹配字符串结束位置
          \b 匹配单词边界
          \B 匹配非单词边界
        分组匹配规则有： findall适用
          |  匹配左右任意一个表达式
          () 将括号中字符作为一个分组

递归  方法（函数）自己调用自己的编程写法
      典型的用于找出文件夹内全部文件
      要有明确判断条件
"""
from re import *
# match匹配
my_str='list but string, python, string'
my_str1='1list but string, python'
# 从头开始匹配字符
result=match('list', my_str)
print(result)
print(result.span())  # 打印字符串下标位置
print(result.group())

result1=match('list', my_str1)
print(result1)

# 搜索字符串
result2=search('string', my_str)
print(result2)

# 匹配整个字符串
result3=findall('string', my_str)
print(result3)
################################################
# 元字符匹配规则
print(findall('\d', 'abc123') )   # ['1', '2', '3']
    # 找出全部英文字母
print(findall(r'[a-zA-Z]', 'asfdbjahsfiASDFG481234') ) 

    # 匹配账号，只能由字母和数字组成，长度6-10
# 规则
rule_str='^[a-zA-Z0-9]{6,10}$'
s=input('请输入账号：')
if match(rule_str,s):
    print('登录成功')
else:
    print('登录失败')
################################################
    # 匹配QQ号，纯数字，长度5-11，且第一位不为零
qq_rule_str='^[1-9]{1}[0-9]{4,10}$' # 匹配整个字符串规则包含^ $
# qq_rule_str='^[1-9]0-9]{4,10}$'  # 功能同上
s=input('请输入QQ账号：')
if findall(qq_rule_str, s):
    print('登录成功')
else:
    print('登录失败')
  # 匹配邮箱
email_rule_str='^\w+@\w+\.\w+$'
s=input('请输入邮箱：')
if findall(email_rule_str, s):
    print('登录成功')
else:
    print('登录失败')

############################################################
############################################################
# 递归
  # 递归找出文件夹内全部文件
import os

def lis_content():
    # 打印路径内的所有内容
    print(os.listdir('D:\Work Space\研究僧\就业\学\Python\my_utils'))
    # 判断路径文件是否为文件夹
    print(os.path.isdir('D:\Work Space\研究僧\就业\学\Python\my_utils/__pycache__'))
    # 判断路径是否存在
    print(os.path.exists('D:\Work Space\研究僧\就业\学\Python\my_utils'))
    # 路径拼接
    print(os.path.join('D:\Work Space\研究僧\就业\学\Python', '测试'))

lis_content()
# 从给定的路径获取全部文件列表
def get_files_list(path):
    # 判断文件路径是否存在
    if os.path.exists(path):
        print(f'该路径{path}为文件夹，其中有文件: {os.listdir(path)}')
    else:
        print('所给文件路径不存在')
        return None
    # 遍历文件
    for file_name in os.listdir(path):
        # 判断文件是否为文件夹
        new_path=os.path.join(path, file_name) # 文件路径拼接
        if os.path.isdir(new_path):   
            get_files_list(new_path)
        else:
            continue
# 主程序

while True:
  real_path=input('请输入要检查的路径')
  while True:
    if get_files_list(real_path):
        pass
    else:
        break
  # 键盘键入ESC退出程序
  if input('输入X以退出, 继续查询按下回车键\n')=='X':
      break
  else:
      pass
  
      
