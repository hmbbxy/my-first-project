# -*- coding: utf-8 -*-
# 修正版：评论情感分类模型
# 修正日期：2026-08-19
# 修正内容：指定文件编码为 utf-8（Windows 默认 GBK 读取 UTF-8 文件会报 UnicodeDecodeError）

# ============== 1. 读取文件（修正点） ==============
import csv
# 【改了什么】原来只写 'r'，Python 在 Windows 下会用系统默认编码（GBK）打开文件
#            当 CSV 文件实际是 UTF-8 编码时，GBK 解码第 8 字节 0x80 时会抛 UnicodeDecodeError
# 【为什么改】显式声明 encoding='utf-8'，让 Python 按文件真实编码读取，
#            这样无论在 Windows 还是其他系统都能稳定运行
file = open(r"C:\Users\Hmbb7\Downloads\yequ (6)\yequ\TVComments.csv", 'r', encoding='utf-8')

## 读取数据集
reader = csv.reader(file)

# ============== 2. 中文分词 ==============
import jieba
## 存储数据
data = []
for info in reader:
    data.append(info)
file.close()  # 读取完毕后立即关闭文件，释放资源

## 分词并存储
word = []
for row in data:
    text = row[0]
    ret = jieba.lcut(text)        # jieba.lcut 输出为列表
    ret = ' '.join(ret)           # 用空格拼接为字符串（CountVectorizer 要求）
    word.append(ret)

# ============== 3. 特征提取（词频向量化） ==============
from sklearn.feature_extraction.text import CountVectorizer
vect = CountVectorizer()
x = vect.fit_transform(word)
keyword = vect.get_feature_names_out()   # 无参数调用
print("关键词提取成功，词汇表大小：", len(keyword))

# ============== 4. 提取特征矩阵与标签 ==============
X = x.toarray()
y = []
for allInfo in data:
    label = allInfo[1]
    y.append(label)

# ============== 5. 划分训练集 / 测试集 ==============
from sklearn.model_selection import train_test_split
result = train_test_split(X, y, train_size=0.8, random_state=1)
train_feature, test_feature, train_label, test_label = result
print("数据集划分成功，训练集：%d 条，测试集：%d 条" % (len(train_label), len(test_label)))

# ============== 6. 搭建与训练模型 ==============
from sklearn.neural_network import MLPClassifier
mlp = MLPClassifier(random_state=1)   # 固定随机种子，结果可复现
mlp.fit(train_feature, train_label)

# ============== 7. 预测与评估 ==============
from sklearn.metrics import accuracy_score
test_pred = mlp.predict(test_feature)
print("测试集预测完成")
print("模型准确率：%.4f" % accuracy_score(test_label, test_pred))
print("前 20 条预测结果：", test_pred[:20])
