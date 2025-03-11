"""
字符串工具包
str_reverse 字符串反转

substr 字符串切片
"""
def str_reverse(s):
    """
    字符串反转
    :param s: 字符串
    :param new_s: 反转后的字符串
    :return: 反转后的字符串
    """
    new_s=s[::-1]
    return new_s

def substr(s, x, y):
    """
    按照下标x, y, 对字符串进行切片
    :param x: 下标
    :param y: 下标
    :param s: 字符串
    """
    new_str=s[x:y]
    return new_str
if __name__=='__main__':
    my_str='hello, this is my girlfriend, jellcy'
    print(str_reverse(my_str))
    print(substr(my_str, 7, 36))