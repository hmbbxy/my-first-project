# 1. 从aip中导入AipImageClassify
from aip import AipImageClassify
# 将AppID赋值给变量APP_ID
APP_ID = '123996115'
# 将API Key赋值给变量API_KEY
API_KEY = '6Au3WThUHOLygc0RPihMoPUU'
# 将Secret Key赋值给变量SECRET_KEY
SECRET_KEY = 'zOATNtiNHqmjDjrOnFrPXBrc2sJaHjOO'
# 新建一个AipImageClassify，并赋值给变量client
client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)
# 输出client
print(client)

#处理单张图像
#为了更高效地学习，我们将“处理单张图像”拆分成以下几步完成：
##1. 读取图像文件
##2. 调用通用物体识别
##3. 提取图像分类信息
##4. 对应分类文件夹还未创建时，创建文件夹
##5. 移动图像到对应文件夹
filePath=r'C:\Users\Hmbb7\Desktop\微信图片_2026-08-19_205617_840.jpg'

# 2. 读取图像文件
##"rb"读取二进制文件
with open(filePath,'rb') as f:
    # 使用read()读取f，赋值给变量image
    image = f.read()
    
# 调用通用物体识别
# 调用通用物体识别接口并把结果赋值给ending
ending = client.advancedGeneral(image)
print(ending)

# 3.提取图像分类信息
# 从第一个结果中提取出图片分类并赋值给变量value
value = ending['result'][0]['root']
# 字符串拼接'/Users/img'、'/'、变量value并将结果赋值给变量targetPath
targetPath = r'C:\Users\Hmbb7\Pictures' + '\\' + value
# 使用print()输出变量targetPath
print(targetPath)

# 4.对应分类文件夹还未创建时，创建文件夹
# 使用import导入os模块
import os
# 如果目标文件夹不存在
if not os.path.exists(targetPath):
    # 使用os.mkdir()函数创建文件夹
    os.mkdir(targetPath)

# 5. 移动图像到对应文件夹
# 导入shutil模块
import shutil
# 使用shutil.move()函数移动文件，将图像移动到目标文件夹中
# 将结果赋值给变量newPath
newPath = shutil.move(filePath, targetPath)
# 使用格式化输出“已经移动到：{newPath}”
print(f"已经移动到：{newPath}")