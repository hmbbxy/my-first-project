# 使用from...import从bs4模块中导入BeautifulSoup
from bs4 import BeautifulSoup

#BeautifulSoup 把不标准的 HTML 代码重新进行了自动更正。
'''示范'''
html = '''
<title>网络爬虫课程</title>
<body>
    <h1 align="center">我的第一个标题-居中显示</h1>
    <h2>我的第二个标题，不居中显示</h2>
    <p>我的第一个段落
    </p>
'''
soup = BeautifulSoup(html, "lxml")
print(soup)
#提取节点 法一：
ps = soup.find_all(name = "h1")
print(ps)
# 法二:
ps = soup.find_all("h1")
print(ps)

'''BeautifulSoup解析网页内容'''
# 使用import导入requests模块
import requests

# 将URL地址赋值给变量url
url = "https://nocturne-spider.baicizhan.com/2020/08/07/1/"

# 将变量url传入requests.get()，赋值给response
response = requests.get(url)

# 将服务器响应内容转换为字符串形式，赋值给html
html = response.text

# 使用BeautifulSoup()读取html，添加lxml解析器，赋值给soup
soup=BeautifulSoup(html,'lxml')

# 使用print输出soup
print(soup)

content=soup.find_all('em')
print(content)
