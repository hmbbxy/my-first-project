'''Part1 字符串拼接_URL（统一资源定位符）'''

# 将字符串"http://"赋值给protocol
protocol = "http://" #访问协议

# 将字符串"nocturne-spider.baicizhan.com"赋值给hostname
hostname = "nocturne-spider.baicizhan.com"  #主机名

# 将字符串"/2020/07/29/example-post/"赋值给filePath
filePath = "/2020/07/29/example-post-3/"  #文件路径

# 使用加号（+）按顺序连接字符串，赋值给url
url = protocol + hostname + filePath

# 使用print输出url
print(url)

'''Part2 请求与响应——状态码（3位数字组成）用于表示服务器对请求的处理结果'''

'''Part3 基础爬虫'''
# 使用import导入requests模块
import requests
#请求网页内容
#requests.get()函数可用于模拟浏览器请求网页的过程，在Python语言中使用该函数，就能够获取网页数据。
#get()函数中传入要访问网页的URL，就像浏览器打开URL一样。
#例如，获取夜曲编程首页的链接就要写:requests.get("https://np.baicizhan.com/")

# 使用requests.get()方法获取url的内容，将结果赋值给response
response = requests.get(url)

# 输出response
print(response)

#获取状态码
# 使用.status_code属性获取状态码，并赋值给statusCode
statusCode = response.status_code
# 输出statusCode
print(statusCode)

'''Part4 判断请求是否成功'''
# 使用if语句判断.status_code属性获取的状态码等于200时
if response.status_code == 200:
    # 输出response.status_code
    print(response.status_code)
    # 使用.text属性获取网页前1000个字符的内容，并赋值给content
    content = response.text[:1000]
    # 输出content
    print(content)
# 不满足条件时
else:
    # 输出：请求数据失败
    print("请求数据失败")
##备注：这是HTML语言，全称为HyperText Markup Language，超文本标记语言，它用来定义网页内容和结构。
##HTML是由一系列的标签组成，这些标签组合起来就是我们浏览器看到的网页。