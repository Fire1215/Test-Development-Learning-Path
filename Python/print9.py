"""
import time
time.sleep() 程序延时
文件操作
 文件编码 编码技术(翻译的规则)将内容翻译成二进制存储
    以什么编码技术写入就以什么编码技术读取 UTF-8(通用)
 !文件读取
    打开(创建)文件 文件对象=open('name', 'mode', encoding='UTF-8')
      mode: 只读，写入，追加（r, w, a）
      encoding: 编码格式（UTF-8） 顺序不是第三位，不能用位置参数
      open函数的完整格式是（file,mode,buffering,encoding,errors,newline,closefd）
    读取文件(想象指针)
     文件对象.read(num) num指读取多少字节长度字符串，若不给定num默认读取全部数据
        多次调用，会紧接上次结束的文字开始读取
     readlines()方法 行的方式把文件内容一次性读取，返回一个列表，每行对应一个元素
     readline()方法 读取一行数据，列表类型
     for循环读取文件行 （返回字符串）
        for line in open('name', 'r')  每个临时变量line，就记录了文件的一行数据
    关闭文件 文件对象.close() 避免文件被python持续占用
    with open 语句块，可以在操作完成后自动关闭文件
     with open('name', 'mode', encoding)as 文件对象:
 !文件写入 调用flush时，内容才会真正写入文件(close内置flush)
    mode=w, 从头编写，原内容会被删除
 !文件的追加写入 调用flush时，内容才会真正写入文件(close内置flush)
    mode=a 在文件最后，追加写入文件
"""
# 打开文件
f = open("D:\Work Space\研究僧\就业\兴趣公司\求职信息.txt", 'r', encoding='UTF-8')
print(type(f))
# 行读取依然续接上一功能结束文字开始
print(f.readlines(), '\n', type(f.readlines()))
# 不输出
my_file=f.read(10)
print(my_file)
print(f.read(20))
f.close()
f = open("D:\Work Space\研究僧\就业\兴趣公司\求职信息.txt", 'r', encoding='UTF-8')
# 空列表
print(f.readlines(), '\n', type(f.readlines()))
#文件读完了，从头开始
f.close()
# for循环
for line in open("D:\Work Space\研究僧\就业\兴趣公司\求职信息.txt", 'r', encoding='UTF-8'):
    print(line, '\n', type(line))
   
# import time
# time.sleep(50000000)