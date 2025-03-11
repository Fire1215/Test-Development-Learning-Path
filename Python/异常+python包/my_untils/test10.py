# 利用自定义包，完成某些任务
 #
from my_utils import str_util as s
from my_utils import file_util as f
my_str='上 海 自 来 水 来 自 海 上'
if s.str_reverse(my_str)==my_str:
    print('hei~你小子真他娘是个人才')

new_str=s.substr(my_str, 4, 17)
print('上 海 的 '+new_str)

 #
my_file=input('请输入待处理的文件路径: \n ')
def prit_func():
    global my_file
    # 打印文件内容
    f.print_file_info(my_file)

def append_func():
    data=input('请输入要追加的文字')
    f.append_to_file(my_file, data)
print('------------------主菜单-------------------\n'
      '选择你要进行的操作:' )
print('文件预览\t[输入1]')
print('追加文字\t[输入2]')  # 通过\t对齐输出

num=int(input('请输入对应操作功能的序号'))
if num==1:
    prit_func()
elif num==2:
    append_func()
else:
    print('请输入正确序号')