##访问tushare,获取需要交易的交易数据
import tushare as ts
#通过账号访问数据源
token='b4c91a6bbe01015e2d68dc77309e24aa91ccdaf59b05097263c89549'
pro=ts.pro_api(token) #初始化token，并赋值给变量pro 用pro——api方法访问数据源
#获取交易日历
#参数分别位 交易所 开始日历 结束日期
stock_exchang=['SSE','SZSE'] #交易所数据简称
#存储数据列表
data=[]
#获取两个交易所的数据
for exchange in stock_exchang:
    df=pro.trade_cal(exchange=exchange,start_date='20200101',end_date='20201231')
     #通过trade-cal()接口获取各大交易日历数据
    #将数据存储到data列表中
    data.append(df)
print(data)
##创建数据库以及交易日历表格
'''part 2 '''
#导入驱动
import pymysql
#连接数据库
conn=pymysql.connect(host="localhost",port=3306,user="root",password="20071203hxy",database="nocturneshop",charset="utf8")
#创建游标对象
cur=conn.cursor()
#创建数据库
SQL1='''
CREATE DATABASE tushare charset='utf8';
'''
#通过游标执行
cur.execute(SQL1) #通过游标对象提供的execute方法将SQL1代码传递给数据库并执行。
#创建交易日历表格
SQL2='''CREATE TABLE trade_cal(
`exchange` VARCHAR(100) NOT NULL,
`cal_date` date NOT NULL,`is_open`bit,`pretrade_date`date
);'''
#输出参数是：exchange（交易所），数据类型varchar
#cal_date（日历日期），数据类型date
#is_open（是否交易），数据类型bit
#pretrade_date（上一个交易日），数据类型date
#通过游标执行
cur.execute(SQL2)

##在数据库中插入数据
'''part 3'''
#为表中插入数据
for df in data:
    #获取每一行数据
    #1. for循环遍历data
    #2. 使用iterrows()方法获取每一行的数据
    #3. 使用list()方法将数据转换为列表形式
    #4. 使用INSERT INTO语句预留参数
    #5. 使用execute()方法插入并传递参数。
    for index,row in df.iterrows():
        #转化为列表
        row=list(row)
        #预留参数
        SQL3='''
            insert into trade_cal(exchange,cal_date,is_open)values(%s,%s,%s);
            '''
        #插入并传递参数
        cur.execute(SQL3,row)
#提交 
conn.commit()
#关闭游标
cur.close()
#关闭数据库连接 
conn.close()