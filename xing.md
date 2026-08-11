+ smtplib模块负责发送邮件的动作配置，包括连接邮箱服务器、登录邮箱、发送邮件。email模块负责构造邮件，例如发件人、收件人、主题、正文和附件的设置
+ 使用import导入smtplib模块
import smtplib
+ 使用from...import导入邮件协议的协议头模块
from email.header import Header
+ 使用from...import导入邮件正文内容数据处理模块
from email.mime.text import MIMEText
+ 使用from...import导入邮件发送多种形式内容模块
from email.mime.multipart import MIMEMultipart
***
<img width="2213" height="563" alt="屏幕截图_11-8-2026_125626_np baicizhan com" src="https://github.com/user-attachments/assets/1cfb1d97-02b6-4bab-81cb-6c7328db4af8" />
+ 设置附件
"Content-Type"主要指网页中文件的类型和编码，目的是告诉浏览器要以哪种形式和编码来打开这个文件，这里设置"application/octet-stream"说明是一个附件。
+ 设置邮件在接收方的展示形式，add_header()需要传入三个参数。
第一个参数Content-Disposition表示响应头中标记内容的展示形式；第二个参数"attachment"表示这是一个附件，可以下载到本地；第三个参数为filename表示下载后的文件名。
这里使用的是美食排行的Excel文档，给filename赋值为"美食排行.xlsx"。
***
+ 将附件对象设置到邮件内容里
我们发送的邮件既有文本信息，也有附件等内容，遇到多种表现对象需要使用MIMEMultipart()对象，它可以将正文的文本和附件组合起来。
这里调用MIMEMultipart()对象，并赋值给message
+ 前面我们将美食排行.xlsx文档处理，并赋值给了att1，这里使用attach()函数，将att1传入函数就完成了对邮件附件的设置。

***
+ 完成邮件附件内容设置后，对晔晔的邮箱进行设置。
1. 对QQ邮箱服务器设置；
2. 使用晔晔的邮箱授权码和账号；
3. 使用smtplib()建立连接并登录邮箱。
<img width="769" height="364" alt="屏幕截图_11-8-2026_13613_np baicizhan com" src="https://github.com/user-attachments/assets/f1c950c7-66ca-4bfb-bfff-cd1820751bee" />
***
#使用smtplib模块登录晔晔的邮箱：
首先使用smtplib.SMTP_SSL(服务器, 端口号)与外部建立服务器建立连接，前面已经将"smtp.qq.com"邮箱服务器地址赋值给了变量mailHost，465是SMTP常用的端口号。
然后使用login()函数，该函数的第一个参数为账号，第二个参数为授权码，这样就完成邮箱登录操作啦
+ 使用smtplib.SMTP_SSL(服务器, 端口号),端口号为465，赋值给smtpObj
smtpObj= smtplib.SMTP_SSL(mailHost, 465)
+ 使用login()函数传入邮箱账户和授权码，登录邮箱
smtpObj.login(mailUser, mailPass)

***
#为了实现名字和邮箱一对一发送邮箱，我们可以使用字典来存储邮箱和姓名。
我们要批量发送邮件，就需要使用for循环读取每一个邮箱和姓名，因此，先使用items()将字典转成可遍历的列表。
+ 定义一个字典mail_dict={}
mail_dict = {"桐桐":"abd123@yequ.com", "小倩":"def456@yequ.com"}
+ 使用items()函数将字典转成可遍历的列表，赋值给mail_list
mail_list = mail_dict.items()
+ 使用for循环遍历列表中的每一项的key value
for key, value in mail_list:
    + 使用格式化输出key value，中间空一格
    print(f"{key} {value}")
***
#编辑邮件内容
右侧代码对邮件的正文、发送者、收件人和主题进行了设置。
MIMEText()函数用于编辑邮件的正文，该函数需要传入三个参数，第一个参数为**邮件正文**，第二个参数设置为"plain"表示**纯文本**，第三个参数表示**邮件的编码**，设为"utf-8"。
+ mail_content = MIMEText("这是邮件正文。", "plain", "utf-8")

##对邮件的正文、发送者、收件人和主题进行了设置。
+ message['From']用于表示发送者信息， Header()中需要填入发送者的姓名，用双引号包围
message['From'] = Header("晔晔<xxx@qq.com>")
+ message['To']用于表示收件人信息， Header()中需要填入收件人的姓名，用双引号包围
message['To'] = Header("李同学<xxxx@qq.com>")
+ message['Subject']用于表示邮件的主题， Header()中需要填写邮件的主题并用双引号包围
message['Subject'] = Header("北京和上海旅游信息汇总")

***
+ 发邮件操作的最后一步。
使用attach()函数将设置到邮件正文；
调用sendmail()函数发送邮件，该函数需要传入三个参数，第一个参数是发送者邮箱，第二个参数是收件人邮箱，第三个参数是.as_string()，它能够将邮件内容转为字符串再发送。
+ 使用message.attach()函数上传邮件正文
    message.attach(mail_content)
    + 使用sendmail(发送人，收件人，message.as_string())发邮件
    smtpObj.sendmail(mailUser, value, message.as_string())
    + 获取姓名输出"xx的邮件发送成功"
    print(f"{key}的邮件发送成功")
```python
# 使用import导入smtplib模块
import smtplib
# 使用from...import导入邮件协议的协议头模块
from email.header import Header
# 使用from...import导入邮件正文内容数据处理模块
from email.mime.text import MIMEText
# 使用from...import导入邮件发送多种形式内容模块
from email.mime.multipart import MIMEMultipart

# 使用with...as语句配合open()函数，以二进制只读"rb"打开文件，赋值给food_file
# 文件路径"/Users/yequ/美食排行.xlsx"
with open("/Users/yequ/美食排行.xlsx", "rb") as food_file:
    # 使用read()函数读取信息，赋值给food_content
    food_content = food_file.read()
# 使用MIMEText()函数，传入要发的附件food_content，设置邮件的编码为base64, 设置附件的内容编码为gb2312，赋值给att1
att1 = MIMEText(food_content, "base64", "gb2312")
# 设置附件的["Content-Type"]内容类型为application/octet-stream表示附件
att1["Content-Type"] = "application/octet-stream"
# 调用add_header()添加"Content-Disposition"，并设置"attachment"表示附件
# 设置附件名字为"美食排行.xlsx"
att1.add_header("Content-Disposition", "attachment", filename="美食排行.xlsx")

# 使用with...as语句配合open()函数，以二进制只读"rb"打开文件，赋值给view_file
# 文件路径"/Users/yequ/城市景点.xlsx"
with open("/Users/yequ/城市景点.xlsx", "rb") as view_file:
    # 使用read()函数读取信息，赋值给view_content
    view_content = view_file.read()
# 使用MIMEText()函数，传入要发的附件view_content，设置邮件的编码为base64, 设置附件的内容编码为gb2312，赋值给att2
att2 = MIMEText(view_content, "base64", "gb2312")
# 设置附件的["Content-Type"]内容类型为application/octet-stream表示附件
att2["Content-Type"] = "application/octet-stream"
# 调用add_header()添加"Content-Disposition"，并设置"attachment"表示附件
# 设置附件名字为"城市景点.xlsx"
att2.add_header("Content-Disposition", "attachment", filename="城市景点.xlsx")

# 邮箱服务器设置，"smtp.qq.com"赋值给mailHost
mailHost = "smtp.qq.com"
# 邮箱账号设置，"ahuayequ@qq.com"赋值给mailUser
mailUser = "ahuayequ@qq.com"
# 邮箱授权码设置，"wiscbwlrcodprabd"赋值给mailPass 
mailPass = "wiscbwlrcodprabd"

# 使用smtplib.SMTP_SSL(服务器, 端口号),端口号为465，赋值给smtpObj
smtpObj= smtplib.SMTP_SSL(mailHost, 465)
# 使用login()函数传入邮箱账户和授权码，登录邮箱
smtpObj.login(mailUser, mailPass)

# 定义一个字典mail_dict={}
mail_dict = {"桐桐":"abd123@yequ.com", "小倩":"def456@yequ.com"}
# 使用items()函数将字典转成可遍历的列表，赋值给mail_list
mail_list = mail_dict.items()
# 使用for循环遍历列表中的每一项
for key, value in mail_list:
    
    # 使用MIMEMultipart()创建实例，用于构造附件，并赋值给message
    message = MIMEMultipart()
    # 使用attach()将附件att1设置到邮件内容里
    message.attach(att1)
    # 使用attach()将附件att2设置到邮件内容里
    message.attach(att2)
    
    # 使用MIMEText()设置邮件正文，赋值给mail_content
    mail_content = MIMEText(f"{key}同学，附件是今日北京和上海美食和景点信息，请查收！", "plain", "utf-8")
    # 使用格式化设置邮件发件人名称为 旅游社晔晔<ahuayequ@qq.com>
    message['From'] = Header(f"旅游社晔晔<{mailUser}>")
    # 使用格式化设置邮件收件人名称 XX同学<xxxx@qq.com>
    message['To'] = Header(f"{key}同学<{value}>")
    # 设置邮件主题 北京和上海旅游信息汇总
    message['Subject'] = Header("北京和上海旅游信息汇总")

    # 使用message.attach()函数上传邮件正文
    message.attach(mail_content)
    # 使用sendmail(发送人，收件人，message.as_string())发邮件
    smtpObj.sendmail(mailUser, value, message.as_string())
    # 获取姓名输出"xx的邮件发送成功"
    print(f"{key}的邮件发送成功")
```
