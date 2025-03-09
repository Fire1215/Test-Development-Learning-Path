# 23级联欢会入口授权
#建立函数，形式参数年级g，体温t
print('欢迎大家，现在距离联欢会开始还剩30分钟，可以排队入场了！')
# 某学校23级学生有*个
import random
number=int(random.randint(1, 10))
for i in range(0, number):
    def tem_enter_permission(t):
        if t>37.5:
            outcome='尼玛的感染了，快走开~'
        else:
            outcome='欢迎光临~贵宾一位，里边请~'
        return outcome
    def gra_enter_permission(g):
        if g!=23:
            result='抱歉, 这是23级的活动噢~'
        else:
            temperature=random.randint(34, 40)
            # temperature=float(input('体温:'))
            result=tem_enter_permission(temperature)
        return result
    grade=int(input('你所在年级是:')) 
    print(gra_enter_permission(grade))
print(f'{number}人参加')