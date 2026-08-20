# 导入shutil模块
import shutil
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


# ====================读取所有文件=====================
# 使用import导入os模块
import os
# 将存储照片的文件夹路径'/Users/img'赋值给变量imgroot
imgroot = r"C:\Users\Hmbb7\Pictures\非自然图像-文字图"
# 使用os.listdir()函数获取该路径下所有文件，并赋值给变量imglist
imglist = os.listdir(imgroot)
## 查看输出结果，我们发现，目标文件夹中除了图像文件还包含其他文件。
##比如，系统自动生成的隐藏文件.DS_Store。

# ================遍历目录下的所有文件名===============
for imgname in imglist:
     # 使用if判断筛除非图像文件
     # 非图像文件的表示方法有很多。
     #在这里，我们对刚刚提到的两类非图像文件做处理，其他情况类似。
     ##一类是系统文件(系统文件常见的名称特点是第一个字符就是".")，一类是文件夹(文件夹的特点更为明显，没有后缀名也就是没有".")
    if imgname[0] == '.' or '.' not in imgname:
        # 如果符合if判断条件，跳出本次循环，进入下一次循环
        continue
    # ==============组合图像文件路径===============
    filePath = imgroot + '\\' + imgname
     # 使用with...as以rb方式，打开路径为filePath的图片并赋值给f
    with open(filePath, 'rb') as f:
        # 使用read()读取f，赋值给变量image
        image = f.read()  

        # 2.调用通用物体识别
    # 调用通用物体识别接口并把结果赋值给ending
    ending = client.advancedGeneral(image)

# 报错编码为216202，说明待识别图像大小不合要求,为了解决这个问题，我们可以通过查看返回结果有无参数result来判断是否识别成功
# 3.提取分类结果
    # 判断是否识别成功
    if "result" in ending: 

# ============访问参数"root"一定就能获取分类信息吗？=====================
#不一定，比如，对部分钱币、动漫或者烟酒等识别。(无上层标签)
#为了以防万一，我们用字典中的get方法来解决
# 可用get()函数解决这个问题，get（）用于返回指定键的值，如果键不在字典中返回默认值 None 或者设置的默认值。

         # 从第一个结果中提取出图像分类并赋值给变量value
        # 若没有找到root信息，则分为“未分类“目录

        value = ending['result'][0].get('root', '未分类')

       
# ================'root'返回的信息都包含具体类别的细分====================
# 但是我们不需要这些细分信息，只需要其中的上层标签即可
# 可以使用字符串的内置函数split()。
# 将分隔符作为参数传入到split()函数中，即可把字符串按照指定分隔符切分成多个字符串组成的列表
        # 只取分类结果value的上层标签并赋值给变量label
        label=value.split("-")[0]
        # 使用print()输出变量label
        print(label)

#===============对应分类文件夹还未创建时，创建文件夹==============
 # 字符串拼接变量imgroot、"/"、变量label并将结果赋值给变量targetPath
        targetPath = imgroot + '\\' + label
        
        # 4.对应分类文件夹还未创建时，创建文件夹
        # 如果目标文件夹不存在
        if not os.path.exists(targetPath):
        # 使用os.mkdir()函数创建文件夹
            os.mkdir(targetPath)

# ==========================移动图像到对应文件夹====================
        # 使用shutil.move()函数移动文件，将图像移动到目标文件夹中
        # 将结果赋值给变量newPath
        newPath = shutil.move(filePath, targetPath)
        # 使用格式化输出“已经移动到：{newPath}”
        print(f"已经移动到：{newPath}")