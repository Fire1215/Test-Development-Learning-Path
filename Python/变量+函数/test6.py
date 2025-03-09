"""
ATM案例
主菜单常驻，可实现查询余额，存款，取款，退出功能(退至输入电话阶段)
存款取款后显示余额
输入错误时程序退出
"""

# 主界面菜单
def menu():
    print('------------------主菜单-------------------\n'
      '尊敬的%s, 您好! 请选择您要办理的业务:' %phone_number)
    print('查询余额\t[输入1]')
    print('存款\t\t[输入2]')  # 通过\t对齐输出
    print('取款\t\t[输入3]')
    print('退出\t\t[输入4]')
    return int(input('请输入您的选择:'))

# 查询余额界面
def balance(show_header):
    if show_header:
        print('-----------------查询余额------------------')
    print('尊敬的%s, 您好! 您的账户余额为:%d ' %(phone_number, account_balance))
    
# 存款
def deposit(d, a):
    print('-------------------存款--------------------\n'
          f'尊敬的{phone_number}, 您好! 您的存款金额为{a}')
    d+=a
    return d
"""
def deposit():
    print('-------------------存款--------------------\n'
          f'尊敬的{phone_number}, 您好! 您的存款金额为{50000}')
    #定义成全局变量
    global account_balance
    account_balance+=50000
    return account_balance
"""

# 取款
def withdraw(w, c):
    print('-------------------取款---------------------\n'
          f'尊敬的{phone_number}, 您好! 您的取款金额为{c}')
    w-=c
    return w

# 主程序
# 定义全局变量
while True:
    import random
    account_balance=random.randint(100000, 5000000)
    print('-------------------白日梦银行---------------------')
    phone_number=int(input('请输入您的身份证后四位:'))
    while True:
        func=menu()
        if func==1:
            balance(1)
            continue  # 结束本次循环，再次回到主菜单（似乎不需要也行）
        elif func==2:
            num=int(input('请输入你的存款金额:'))
            account_balance=deposit(account_balance, num)
            balance(0)
        elif func==3:
            num=int(input('请输入你的取款金额:'))
            account_balance=withdraw(account_balance, num)
            balance(0)
        elif func==4:
            break
        else:
            print('请输入有效数字!')
            continue
    break