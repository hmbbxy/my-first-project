# 关键字
+ SELECT 用来选择要查找的**数据内容（字段名）**
  + from 要置于select之后，不可省略
+ 分号表示本次查询结果
+ as 关键字 用来重命名要查找的数据内容
+ order by 关键字，默认升序**排列**
+ limit 对要取的数据的数量进行限制
   + `limit 10，3`
   + 数值10，表明要跳过的行数
   + 数值3，表明要显示的行数
+ distinct 表示要对某列精选去重，后面加要进行去重处理的列
+ 在存储数据时某行无效或者缺失的值，在数据库中以NULL表示
+ where 用来筛选从表中提取的数据，后面加限制条件

***
# 函数
## 聚合函数（组函数）
+ 定义： 对一组值进行计算，并返回单个值
+ 可以用distinct关键字去除重复值
+ 可以进行列与列之间**加减乘除**
### 常见公式~~select~~
+ count 进行计数
 + count（*）表示对表中所有行的数目进行计数
 + count（column）对特定列中非NULL的行进行计数
 + count（distinct column）可得到特定列中去除重复行的行数
+ max（）
 + 定义：得到指定列中的最大值或者最新日期值，忽略NUll
 + 可以用于文本列按字母排序的最高值
+ min（）
  + 与max（）相反
+ sum（）
  + 返回指定列值的和，忽略列值为Null的行
+ avg（）
  + 定义：用于计算指定列
  + 只用于计算指定列的平均值，如果需要计算多列的平均值，则需要使用多个avg（）的函数
***
## 时间函数与字符串函数
### 时间函数
+ now（）
   + select now（）可以获得当前日期与时间
   + select
+ timestampdiff（）
   + 定义：用于计算日期之间的整数差
   + 用法举例：timestampdiff（year/day/...，计算差值中较远的日期，计算差值中较近的日期）
   + select
***     
### 字符串函数
+ concat（）
  + 定义：用于将多个字符串连接为一个字符串
  + 函数内填写选取的字段，需要拼接的字段用英文逗号分隔
  + select
+ substr（）
  + 定义：用于从指定的字符串中选取指定的字段
  + 用法举例：substr（string，start，length）
    + string 指定的要截取的字符串
    + start 规定在字符串的何处开始
    + length 指定要截取的字符串长度
***
# 计算公式
## ROI
+ 投资回报率=产出（销售收入）/投入（成本）
  + >1 可继续投入
  + =1 一般情况下可以继续投入
  + <1 除非有特殊用途，例如烧钱扩大知名度，一般情况下会停止投入
## RFM模型
+ 定义：衡量客户价值的一种常用模型
+ 具体含义
  + R代表最近一次消费（Recency）最近一次消费时间越近，则用户价值越大
  + F代表消费频率（Frequency）消费频率越高，则用户价值越大
  + M代表消费金额（Monetary）消费金额越大，则用户价值越大
***
# 分组与数据统计
+ group by+字段名
  + 后面可以设置多列，表示按照多列进行分组
    + 列名之间用逗号进行分隔
+ having
  + 关键字having，表示对分组设置筛选条件
  + having+筛选条件
  + having必须在group by 后使用，表示对分组后的结果进行筛选
  + 与where的区别：where过滤行，having过滤组
<img width="1325" height="842" alt="day9" src="https://github.com/user-attachments/assets/725c21d4-1675-469c-b0f3-bef08113434f" />

***

# 表格的合并与联结

## 联结
  + 定义：一个或多个表格通过某种关系横向合并为一个表格的过程
  + 分类：1.联结（笛卡尔积）
          2.内联结
          3.外联结
  + UNION
    + 作用：将多个查询结果进行合并
    + UNION 关键字应处于两次查询之间
    + select..
      from...
      UNION
      select...
      from...
+ 内联结
  <img width="2512" height="1822" alt="day11" src="https://github.com/user-attachments/assets/da290f5b-421b-4fb9-9b59-b5c091bd7cc2" />

+ 外联结
  <img width="5098" height="3046" alt="day12" src="https://github.com/user-attachments/assets/f0d0196a-eff5-4fe3-af10-eedad3bc554f" />

  ***

  + JOIN
    + 用来获取两个表格相互组合的所有可能性，及笛卡尔积
    + JOIN的位置应处于FROM后
    + 使用JOIN进行表格的联结时，若出现重复的表名，需要给每个表名设定不一样的别名。若要显示的列名重复，需要以“表名.列名”的方式限定，避免出现歧义

# 嵌套查询（子查询）

 <img width="2510" height="1784" alt="day13" src="https://github.com/user-attachments/assets/411d32fe-f79b-4a84-a587-e21120f479d2" />

 <img width="2466" height="2432" alt="day14" src="https://github.com/user-attachments/assets/51b11b44-ff63-4c5c-9173-e91d87959bda" />

 



