"""
异常的捕获
 常规异常
    try:
        可能发生错误代码
    except:
        如果出现异常执行的代码
    else: # 可以省略
        没有异常要执行的
    finally: # 可以省略
        无论是否异常都要执行
 指定异常 
    except 异常类型 as 变量名:
 捕获多个异常
    except (异常类型1, 异常类型2) as 变量名：
 捕获全部异常
    except Exception as 变量名:
异常具有传递性 那么就不需要追根溯源，在顶层语句就可以处理

python的模块  即为python文件，定义了函数、类、变量，可直接调用实现某种功能
    [from 模块名] import [模块 |类 |变量 |函数 |*] [as 变量名]
        import 模块名
            模块名.功能名()
        from 模块名 import 类、变量、方法等功能名 (调用某一函数)
        from 模块名 import *  (可直接使用全部功能，除非出现'__all__'变量)
            功能名()
        更名
            import 模块名 as 变量名
            from 模块名 import 功能名 as 变量名
    自定义模块
     若出现重复调用功能名，后面模块会覆盖前面的
        测试模块 在自定义的模块中，程序员调用功能
         解决办法
            在模块文件中加入 if __name__=='__main__'，表示模块作为主程序运行时才会
            执行
        若模块文件中有'__all__'变量，*导入时只能导入该列表中元素
python包 存放了模块的文件夹,还包含__init__.py,后者存在，该文件夹才能为包
        project/
    │── main.py                  # 主程序
    │── my_package/              # 你的 Python 包
    │   ├── __init__.py          # 让 Python 识别为包（可留空）
    │   ├── module1.py           # 你的模块 1
    │   ├── module2.py           # 你的模块 2
    import my_package.my_module
    my_module.test()
        在__init__.py中写入__all__变量, 可决定*调用包时能使用的模块
        __all__=['my_module']
    常见的第三方包，及其代表的含义，安装方式:pip install 包名
    或使用pip install 包名 -i https://pypi.tuna.tsinghua.edu.cn/simple
        numpy: 数值计算库  pandas: 数据处理库   matplotlib: 画图库
        scikit-learn: 机器学习库     requests: 网络请求库     
        beautifulsoup4: 网页解析库    flask: web框架      django: web框架 
        scrapy: 爬虫框架     tensorflow: 深度学习库        keras: 深度学习库   
        pytorch: 深度学习库  jupyter: 交互式笔记本    opencv-python: 计算机视觉库
        pillow: 图像处理库   pygame: 游戏开发库   pyqt: GUI开发库      
        wxpython: GUI开发库        pyinstaller: 打包工具      py2exe: 打包工具      
        py2app: 打包工具    cx_freeze: 打包工具      pywin32: Windows扩展库       
        pypiwin32: Windows扩展库      python-docx: Word文档处理库   
        xlrd: Excel文件读取库  xlwt: Excel文件写入库  openpyxl: Excel文件处理库       
        pyyaml: YAML文件处理库  paramiko: SSH库   selenium: 浏览器自动化库   
        scrapy: 爬虫框架      flask: web框架     django: web框架        
        tornado: web框架    bottle: web框架        pyramid: web框架        
        requests: 网络请求库    urllib: 网络请求库    beautifulsoup4: 网页解析库       
        lxml: 网页解析库        pyquery: 网页解析库       flask_sqlalchemy: ORM库
        sqlalchemy: ORM库        pymysql: MySQL数据库库      
        pymongo: MongoDB数据库库    redis: Redis数据库库      
        elasticsearch: Elasticsearch搜索库
    
"""
my_list=[3, [3, 4, 5, 'n'], ['y']]
try: # 碰到异常即跳转，不执行后面代码
    # x=n+y
    index=my_list.index('y')
    print(index)
# 仅仅捕获值异常
except ValueError as example1:
    n=my_list[1][3]
    y='不错'
    print(n+y, example1)

# 捕获多个异常
my_list=[3, [3, 4, 5, 'n'], ['y']]
try:
    # 碰到异常即跳转，不执行后面代码
    x=m+y
    index=my_list.index('y')
# 截停多个异常
except (NameError, ValueError) as example1:
    print(example1)
else:
    print('没有异常呀')
finally:
    print('我始终是要干活的')

#########################################################################
#########################################################################
# python 的模块
 #
import time
# 程序延时10秒
# '.'用以确定层级，即表示time.py文件中的sleep函数
time.sleep(1)
print('我醒了')
 #
from time import sleep
sleep(1)
print('我又睡了')
 # 
from time import *
sleep(1)
print('我不睡啦')
    # 自定义模块
'''
from my_module import del_output as test
result=test()
print(result)
'''
"""
直接输出3
from my_module import add_func
"""

# python包
from my_utils.my_module import add_func
print(add_func('我要', '吃粉'))

