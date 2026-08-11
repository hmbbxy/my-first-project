+ smtplib模块负责发送邮件的动作配置，包括连接邮箱服务器、登录邮箱、发送邮件。email模块负责构造邮件，例如发件人、收件人、主题、正文和附件的设置
+ 使用import导入smtplib模块
import smtplib
+ 使用from...import导入邮件协议的协议头模块
from email.header import Header
+ 使用from...import导入邮件正文内容数据处理模块
from email.mime.text import MIMEText
+ 使用from...import导入邮件发送多种形式内容模块
from email.mime.multipart import MIMEMultipart
