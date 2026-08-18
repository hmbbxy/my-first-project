import pymysql
print(pymysql.__version__)
conn=pymysql.connect(host="localhost",port=3306,user="root",password="20071203hxy",database="nocturneshop",charset="utf8")
#创建游标对象
cur=conn.cursor()
#存储SQL指令

SQL="select * from brand";

#执行SQL指令
ret=cur.execute(SQL)
print(f'本次查询共获得了{ret}条数据')
#获取一条数据
data=cur.fetchone()
print(data)
#接着获得4条数据
data=cur.fetchmany(4)
print(data)
#获取所有剩下的数据
data=cur.fetchall()
print(data)
#关闭游标对象
cur.close()
#关闭数据库连接
conn.close()    
