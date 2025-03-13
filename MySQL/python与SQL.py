from pymysql import *
# 构建到MySQL数据库的链接
conne=Connection(
    host='localhost',    #主机名（IP）
    port=3306,          # 端口
    user='root',         # 账户
    password='990108'   # 密码
)
# 获取服务器信息
print(conne.get_server_info())
# 执行非查询性质SQL
    # 获取游标对象
cursor=conne.cursor()
    # 选择数据库  大小写无影响
conne.select_db("NEW_DATABASE")
    # 执行SQL, 传入SQL语句，只能用双引号
    # 分号可以不写
# cursor.execute("CREATE TABLE TEST_PYMYSQL(是否成功 varchar(20), "
# "次数 int);")
# cursor.execute("drop TABLE TEST_PYMYSQL;")
# 执行查询性SQL
cursor.execute("select * from mysql")
    # 查询结果
result: tuple=cursor.fetchall()
for r in result:
    print(r)
    #  插入数据
# cursor.execute("INSERT into mysql VALUES('东北大学', '驴昂昂', "
# "'5122', 24)")
        # 还需要确认
conne.commit()
        # 或自动确认
autocommit=True
# 关闭链接
conne.close()