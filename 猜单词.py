# TODO 导入time模块
import time
# 用字典的形式存储单词，字典的键为中文，值为英文
wordList = {"苹果":"apple", "香蕉":"banana","西瓜":"watermelon"}

# 输出"背单词小游戏"
print("背单词小游戏")

# TODO 使用time.sleep()函数设置停顿2秒
time.sleep(2)
# 计数器归零
count = 0

# 遍历字典wordList
for i in wordList:
    # TODO 使用input()函数接收用户输入的英文并存储在变量word中
    # TODO 文案为
    word=input(f"请输入{i}的英文：")
    # TODO 判断word和字典wordList[i]相等
    if word==wordList[i]:
        # TODO 计数器加1
        count+=1
        # TODO 判断如果计数器不等于3
        if count!=3:
            # TODO 输出
            print("你真棒，继续冲")
        # 其他情况    
        else:
            # TODO 输出
            print("全部答对")
    # 如果word和字典wordList[i]不相等，也就是其他情况        
    else:
        # TODO 输出
        print("再来一次")
        # TODO 跳出循环
        break
