-- 单行注释,空格不要落下
# 单行注释
/*多行注释可行

SQL语言是对数据库、数据进行操作、管理、查询的标准计算机语言语言
特征：
大小写不敏感, 可多行分开写，语句以“;”结束即可
功能：
数据定义：DDL
	库的创建删除
        show databases;		    查看有哪些数据库
        use 数据库名；		    使用某个数据库
        show tables;	        查看数据库内有哪些表   
        exit			        退出MySQL的命令行环境
        DROP DATABASE 数据库名称；删除数据库
        SELECT DATABASE();      查看当前使用的数据库
        create database 数据库名称 [CHARSET UTF8];     创建数据库
    表的创建删除  需要选中库后操作
        SHOW TABLES;   查看表
        DROP TABLE 表名称;     删除表
            DROP TABLE IF EXISTS 表名称；         
        CREATE TABLE 表名称(
            列名称 列类型,
            列名称 列类型
        );
        列类型有
            int, float
            varchar(长度)  文本，长度为数字，做最大长度限制
                中文只能使用单引号
            data     日期类型
            timestamp  时间戳类型
数据操纵
    # 追加数据
    insert into 表[(列1， 列2，……)] values(值1, 值2,……)[(值1, 值2,……)] 
    # 删除数据
    delete from 表名称 [where 条件判断]
        条件判断: 列 操作符 值
            操作符：= < > <= >= !=
    # 更新数据
    update 表名称 set 列=值 [where 条件判断]
数据查询
    select 字段列表(或*) from 表名称 [where 条件]
        从表中，选择某些列进行展示
    分组聚合查询
        select 字段/聚合函数 from 表名称 [where 条件] group by 列
            聚合函数 
            sum(列)，avg(列)，min(列)，max(列)，count(列/*)
          任何聚合函数 字段部分只能使用条件列名
    排序分页  对查询结果排序写紧接select语句后
        select 字段/聚合函数 from 表名称 
        [where 条件] 
        group by 列
        order by 列 [ASC | DESC];
            默认ASC 从小到大 

    结果分页限制 对查询结果进行数量限制或分页显示
        select 字段/聚合函数 from 表名称 
        [where 条件] 
        group by 列
        order by 列 [ASC | DESC] limit n[, m];
            n：显示n条信息
            [n, m]: 从第n条开始, 向后取m条


*/
##################################################
# 数据定义
shoW 
DATABASEs;
USE NEW_DATABASE;
SELECT DATABASE();
SHOW TABLES;
CREATE TABLE MYSQL(
    school varchar(60),
    name varchar(10),
    student_card int,
    age int
);
####################################################
# 数据操纵
drop TABLE mysql;
# 插入数据
insert into mysql(school, name, student_card, age)
values('四川大学', '猪噜噜', '5112', 26), 
('苏州大学', '哈呼呼', '5213', 28
), ('西南民族大学', '羊咩咩', '5566',27);
    # 三个列都需填入数据时 (school, name, student_card)可以省略

# 数据删除
DELETE from mysql where school!='四川大学';
delete from mysql;  -- 清空整个表；
# 数据更新
UPDATE mysql set name='牛哞哞' where name='哈呼呼';
###########################################################
# 数据查询
select name, student_card from mysql;
    # 全部展示
select * from mysql;
    # 条件查询
select school from mysql where student_card<=5213;
    # 分组聚合查询
-- INSERT into mysql VALUES('西南民族大学', '鸭嘎嘎', '5142', 28);

-- UPDATE mysql set name='马吁吁' where age=23;
# 任何聚合函数 字段部分只能使用条件列名
select school, min(age), sum(age) from mysql 
where age<30 GROUP BY school;
# 排序分页
select * FROM mysql where age>21 order by age;
# 结果分页
select * FROM mysql limit 4;  -- 只显示四条信息
select * FROM mysql limit 3, 4;  -- 第三条开始取，显示四条
select age, count(*) from mysql 
where age<30 GROUP BY age ORDER BY age LIMIT 2, 4;