# 单词计数
count=0
column_num=0
# 文件首字母出现t, 需要使用左斜杠
with open("D:\Work Space/研究僧\就业\学\Python/test.txt", "r", encoding='UTF-8') as word_file:
    # 得到每行组成的列表
    word_list=word_file.readlines()
    print(word_list)
    for i in word_list:
            # 统计文件行数
            column_num+=1
            # print(i, type(i))
            # 统计列表中每个字符串中单词出现次数
            c=i.count('elif')
            # 记录次数
            if c!=0:
                count+=1
with open("D:\Work Space/研究僧\就业\学\Python/test.txt", "a", encoding='UTF-8') as word_file:
    word_file.write('\n666')
for line in open("D:\Work Space/研究僧\就业\学\Python/test.txt", "r", encoding='UTF-8'):
     print(line)
        # word_str_to_list=list(i)
        # for j in word_str_to_list:
        #     print(j)
            # if i=='elif':
            #     count+=1
# print(word_str_to_list)
print('文件test.txt中，总共有%d行，其中‘elif’出现的次数为%d' % (column_num, count))
