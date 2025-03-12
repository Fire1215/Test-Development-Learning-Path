# 记录三位学生姓名、年龄、地址
# 利用for循环，完成信息的键盘键入
# 学生信息录入至文件，同时使用print语句输出信息待学生确认
class stu_info:
    def __init__(self, name, age, adress, num):
        self.name=name
        self.age=age
        self.adress=adress
        try:
            info=f'学生姓名：{self.name}，年龄：{self.age}，地址：{self.adress}'
            my_file=open('D:\Work Space\研究僧\就业\学\Python\student_info.txt', 'a', encoding='UTF-8')
            my_file.write(info)
            my_file.write('\n')             
            print(f"""学生{num}信息录入完成，信息为："""+'【%s】' % info)
        except Exception as problem:
            print(f'出现异常了，问题为{problem}')
            # print(f"""学生{self.num}信息录入完成，信息为：【{info}】""")
        finally:
            my_file.close()
count=0
stu_1=None
stu_2=None
stu_3=None
# sum=int(input('请统计班级总人数，并填写：\n'))
for i in [stu_1, stu_2, stu_3]:
    count+=1
    print(f'Attention! 现在开始录入第{count}位学生信息，共3位学生需录入。')
    i=stu_info(input('姓名：'), input('年龄：'), input('住址：'), count)


# 设计手机类
# 私有成员变量: __is__5g__enable, 变量类型为bool，True为开启
# 私有成员方法：__check_5g,判断通信状态
# 公开成员方法：call_by_5g，打印输出私有信息

class phone_call:
    __is_5g_enable=input('请输入True或False：')
    def __check_5g(self):
        if self.__is_5g_enable==1:
            print('5g通信开启')
        else:
            print('5g关闭，使用4g通信')

    def call_by_5g(self):
        self.__check_5g()
        print('正在通话中……')
    
Huawei=phone_call()
Huawei.call_by_5g()
