"""
发工资实例练习
账户余额*元，员工*名（编号1-*），每人领取工资*元
财务判断员工绩效分，1-10随机生成，低于*，不发工资
"""
# 变量定义
# 输入公司可支配余额
account_balance=int(input('请输入公司可用于员工工资金额:'))
# 员工数
employee=int(input('请输入公司员工数:'))
# 输入绩效达标分数
employee_score=int(input('输入绩效达标分数(1-10):'))
# 绩效不达标员工数
num=0
# 员工工资
employee_salary=int(input('请输入员工固定工资:'))
for employee_number in range(1, employee+1):
    #这是财务房间，根据员工编号依次进来一位员工，查询其绩效分数
    import random
    score=random.randint(1, 10)
    if score<employee_number:
        num+=1
        continue
    account_balance-=employee_salary
    if account_balance<=0:
        break
if employee_number==employee:
    message='公司账户还剩%d元，绩效分不足的%d人工资发不了，都把绩效分往上冲冲'%(account_balance, num)
    print(message)
else:
    print(f"""同志们，经济下行，公司账户空了~这次统计了{employee_number}人，
绩效分不达标{num}人""")
