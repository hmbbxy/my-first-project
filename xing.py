import smtplib
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

qqMail=smtplib.SMTP_SSL("smtp.qq.com",465)
mailUser="872633982@qq.com"
mailPass="kbeexsnfxffebdic"
qqMail.login(mailUser,mailPass)

sender="872633982@qq.com"
receiver="yequbiancheng@baicizhan.com"
message=MIMEMultipart()
message["Subject"]=Header("致你的一封信")
message["From"]=Header(f"xy<{sender}>")
message["To"]=Header(f"yqbc<{receiver}>")

textContent="万事胜意"
mailContent=MIMEText(textContent,"plain","utf-8")

filePath=r"C:\Users\Hmbb7\Downloads\屏幕截图_14-7-2026_214530_np.baicizhan.com.jpeg"
with open(filePath,"rb") as imageFile:
    fileContent=imageFile.read()

attachment=MIMEImage(fileContent)
attachment.add_header("Content-Disposition","attachment",filename="入门课成绩单.jpg")

message.attach(mailContent)
message.attach(attachment)

qqMail.sendmail(sender,receiver,message.as_string())
print("发送成功")