"""
文件处理工具
print_file_info
append_to_file
"""
def print_file_info(file_name):
    my_file=None
    try:
        my_file=open(file_name, 'r', encoding='UTF-8')
    except Exception as problem:
        print(f'打开文件异常，因为{problem}')
    else:
        print(my_file.readlines())
    finally:
            if my_file:
                my_file.close()

def append_to_file(file_name, data):
    my_file=open(file_name, 'a', encoding='UTF-8')
    my_file.write('\n')
    my_file.write(data)
    my_file.close()
    for i in open(file_name, 'r', encoding='UTF-8'):
        print(i)
if __name__=='__main__':
    # print_file_info('D:\Work Space\研究僧\就业\学\Python\my_utils/test1.txt')
    print_file_info('D:\Work Space\研究僧\就业\学\Python\my_utils/test1.txt')