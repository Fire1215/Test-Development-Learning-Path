# 猜字游戏
import random
num=random.randint(1, 10)
print('听说你最近学了一套魔法？我心中想一个(1-10)的数，你把住我的脉就可以确定这个数？\n"你咋知道嘞，那我给你小露一手！"')
guess_num=int(input('观其手微微贴在脉上，作沉思状~~,能猜中不？（输入数字）\n')) # 第一次输入的值
if guess_num!=num: 
    if guess_num>num:
       print('给你降低点难度，这次给的数大了')
    else:
       print('给你降低点难度，这次给的数小了') 
       
    guess_num=int(input('第二次机会：\n'))
    if guess_num!=num:
        if guess_num>num:
            print('大了')
        else:
            print('小了') 

        guess_num=int(input('快点的，最后一次机会：\n'))
        if guess_num!=num:
            print(f'衰仔，我心里想的数字是 {num}')
        else:
            print('我了个逗，不是哥们你真会啊！')
    else:
        print('我了个逗，不是哥们你真会啊！')
else:
    print('我了个逗，不是哥们你真会啊！')

