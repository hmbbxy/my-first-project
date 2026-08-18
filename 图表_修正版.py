# ============================================================
# 图表_修正版.py  （原文件 图表.py 未做任何修改，仅在此副本中调整）
# ============================================================
import matplotlib.pyplot as plt
import pandas as pd

# 修改①：字体设置集中放在最前面
plt.rcParams['font.sans-serif'] = ['SimHei']   # 黑体，解决中文显示
plt.rcParams['axes.unicode_minus'] = False     # 解决负号显示为方块的问题

# 修改②：先读数据，再画图（原第4行的 plt.show() 放在数据加载之前，会先弹出一个空图）
data = pd.read_csv(r"C:\Users\Hmbb7\Downloads\涔﹀簵鍥句功閿€閲忓拞骞垮憡璐圭敤.csv", encoding='gbk')
df = pd.read_csv(r"C:\Users\Hmbb7\Downloads\涔﹀簵姣忔湀閿€閲忔暟鎹櫨鍒嗘瘮.csv", encoding='gbk')

# 修改③：把 date 转成真正的日期类型（关键！）
# 原代码里 date 是字符串(object)，matplotlib 把它当“类别”排在 0,1,2… 上，
# 月份字符串又长，多个图叠在一起时标签会互相重叠、被边框裁掉，看起来就像“x轴没数据”。
data['date'] = pd.to_datetime(data['date'])


# ===================== 图1：折线图 =====================
plt.figure(figsize=(8, 6), facecolor='lightblue')
plt.plot(data['date'], data['ads_fee'], color='orange', marker='o', label='总收入')
plt.xlabel('月份')
plt.ylabel('收入')
plt.title('月度收入趋势')
plt.xticks(rotation=45)   # 修改④：日期标签旋转45°，避免横向挤成一团
plt.legend()
plt.tight_layout()        # 修改⑤：自动调整子图边距，防止标签被图框切掉
plt.show()


# ===================== 图2：柱状图 =====================
plt.figure(figsize=(8, 6))
# 修改⑥：原 width=2 是在“类别轴”上的宽度（2个单位，柱子严重重叠）。
# 现在 date 是 datetime 轴，width 表示“天数跨度”，2天太窄几乎看不见柱子，
# 改成 20 天左右（小于一个月间隔）更合理。
plt.bar(data['date'], data['ads_fee'], color='lightgreen', label='总收入', width=20)
plt.xlabel('月份')
plt.ylabel('收入')
plt.title('月度收入柱状图')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()


# ===================== 图3：2x2 子图 =====================
plt.figure(figsize=(12, 9))

plt.subplot(2, 2, 1)
plt.scatter(data['date'], data['ads_fee'])
plt.xlabel('月份')
plt.ylabel('收入')
plt.xticks(rotation=45)   # 修改④：每个子图都加上旋转

plt.subplot(2, 2, 2)
plt.plot(data['date'], data['ads_fee'], color='blue', marker='o', label='总收入')
plt.xticks(rotation=45)
plt.xlabel('月份')
plt.ylabel('收入')
plt.title('月度收入折线图')
plt.legend()

plt.subplot(2, 2, 3)
df.plot.bar('month', ['一楼', '二楼', '三楼'], stacked=True, ax=plt.gca())
plt.xlabel('月份')
plt.ylabel('楼层')
plt.title('各楼层每月收入柱状图')
plt.xticks(rotation=45)   # 修改④：月份标签旋转
plt.legend()

plt.subplot(2, 2, 4)
plt.plot(data['date'], data['ads_fee'], color='orange', marker='o', label='总收入')
# 修改⑥：同样把 width 从 2 改成 20（datetime 轴下的天数跨度）
plt.bar(data['date'], data['sales'], color='lightgreen', label='总销量', width=20)
plt.xlabel('月份')
plt.ylabel('收入/销量')
plt.title('月度收入与销量趋势图')
plt.xticks(rotation=45)
plt.legend(loc='upper right')

plt.tight_layout()        # 修改⑤：统一调整边距
plt.show()
