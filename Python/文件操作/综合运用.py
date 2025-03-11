"""
有一份账单文件，记录了收支情况
  将文件写出到bill.txt.bak中作备份
  将测试行数据丢弃
"""
del_str=input('请输入你要删除的字符：')
# 备份文件
for ori_information in open("D:\Work Space\研究僧\就业\学\Python/bill_test.txt", 'r', encoding='UTF-8'):
    # 去除首尾空格及换行符
    column_infor=ori_information.strip()
    # 以‘，’分割形成列表
    column_infor_list=column_infor.split('，')
    # 若该行有‘测试’，寻找测试所在列表下标
    if del_str in column_infor_list:
        continue
        # # 得到index
        # index=column_infor_list.index('测试')
        # # 若列表[index]项不为测试，则保留
        # if column_infor_list[index]!='测试':
        #     # 需要使用追加，不然写入有覆盖
    else:
        with open("D:\Work Space\研究僧\就业\学\Python/bill_test.txt.bak", 'a', encoding='UTF-8') as new_bill_file:
                new_bill_file.write(ori_information)
