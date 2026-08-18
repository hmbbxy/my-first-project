import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体为黑体
plt.figure(figsize=(8,6),facecolor='lightblue')  # 设置图形大小和背景颜色
plt.show()
import pandas as pd
data=pd.read_csv(r"C:\Users\Hmbb7\Downloads\涔﹀簵鍥句功閿€閲忓拰骞垮憡璐圭敤.csv",encoding='gbk')
df=pd.read_csv(r"C:\Users\Hmbb7\Downloads\涔﹀簵姣忔湀閿€閲忔暟鎹櫨鍒嗘瘮.csv",encoding='gbk')
plt.plot(data['date'],data['ads_fee'],color='orange',marker='o',label='总收入')
plt.xlabel('月份')
plt.ylabel('收入')
plt.title('月度收入趋势')
plt.legend()
plt.show()

plt.bar(data['date'],data['ads_fee'],color='lightgreen',label='总收入',width=2)
plt.xlabel('月份') 
plt.ylabel('收入')
plt.title('月度收入柱状图')
plt.legend()
plt.show()

#多个图表的运用
plt.subplot(2,2,1)
plt.scatter(data['date'],data['ads_fee'])
plt.xlabel('月份')
plt.ylabel('收入')

plt.subplot(2,2,2)
plt.plot(data['date'],data['ads_fee'],color='blue',marker='o',label='总收入')
plt.xticks(rotation=90)
plt.xlabel('月份')
plt.ylabel('收入')
plt.title('月度收入折线图')
plt.legend()

plt.subplot(2,2,3)
df.plot.bar('month',['一楼','二楼','三楼'],stacked=True,ax=plt.gca())
plt.xlabel('月份')
plt.ylabel('楼层')
plt.title('各楼层每月收入柱状图')
plt.legend()

plt.subplot(2,2,4)
plt.plot(data['date'],data['ads_fee'],color='orange',marker='o',label='总收入')
plt.twinx()
plt.bar(data['date'],data['sales'],color='lightgreen',label='总销量',width=2)
plt.xlabel('月份')
plt.ylabel('收入/销量')
plt.title('月度收入与销量趋势图')
plt.legend(loc='upper right')

plt.tight_layout()
plt.show()