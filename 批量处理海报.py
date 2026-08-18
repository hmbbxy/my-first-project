# 使用import导入requests模块
import requests

# 将网络图片的 URL 地址，赋值给变量 url
url = "https://npbcz.wordpress.com/wp-content/uploads/2020/09/2-2.jpg"

# 将 User-Agent 以字典键对形式赋值给 headers
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

# 将 url 和 headers 参数添加进 requests.get() 中，赋值给 response
response = requests.get(url, headers=headers)

# 使用 .content 属性获取图片的二进制数据
img = response.content

# 使用with...as以wb方式，打开文件，并赋值给f 如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件
with open("图片.jpg", "wb") as f:

    # 使用write()函数写入img
    f.write(img)

# 使用print输出"海报图片下载成功"
print("海报图片下载成功")
