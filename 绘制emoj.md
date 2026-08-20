# turtle
## 导入turtle模块
+ 方法1:
`import turtle`：导入turtle模块。
+ 方法2:
`from turtle import *`：从turtle模块中导入所有的函数(后续可以直接用函数)
# 利用turtle绘制爱心
1. 绘制左边线
2. 绘制左半圆
3. 绘制右半圆
4. 绘制右边线
5. 填充颜色
6. 填充表白文字
## pensize()
+ 一个函数，作用是设置画笔粗细
## pencolor()
+ 一个函数，作用是设置画笔颜色。
### 颜色设置
+ pencolor()的颜色设置很灵活。
+ 参数可以用三种模式填写，比如：
  + RGB颜色值：(255,192,203)
  + 16进制颜色码：#FFC0CB
  + 英文代码："pink"
+ 呈现的结果都是粉色，其他色彩设置可以参考网站： [颜色设置参考网站](https://www.sioe.cn/yingyong/yanse-rgb-16/)
## left()
+ 一个函数，作用是将画笔方向向左转。
## right()
+ 一个函数，作用是将画笔方向向右转。
+ 设置的参数表示向右转的角度。
## forward()
+ 一个函数，作用是向画笔方向前进。
+ 设置的参数表示前进的步数。
## circle()
+ 一个函数，作用是画圆。
+ circle(radius,extent=None,steps=None)
  + 例如：circle(50,-180)表示绘制一个半径为50，圆心角为-180的半圆。
## fillcolor()设置填充颜色
+ 例如：fillcolor("pink")是指将填充颜色设置为粉色。

### begin_fill ()函数设置颜色填充的起点
### end_fill()函数设置颜色填充的终点

## 利用write()绘制文字
+ 填写文字的步骤是：
1.设置画笔颜色
2.将画笔移动到爱心的中心位置
3.写下表白的话

## goto()
+ 一个函数，作用是移动到指定坐标位置。
+ `goto(x,y)`参数需要填写移动到的具体坐标位置。
  + 例如`goto(0,80)`就是移动到x=0，y=80的位置

## write()
+ 一个函数，作用是填写文字。
+ `write()`函数可以设置参数。
  + 例如：`write("LOVE YOU",align = "center",font=("Arial",20,"bold"))`
  + 表示：书写的内容是"LOVE YOU "，文字内容居中，字体为"Arial"，字体大小20，粗细为"bold"粗。
<img width="1730" height="1245" alt="屏幕截图_20-8-2026_16832_np baicizhan com" src="https://github.com/user-attachments/assets/55879874-24df-4735-835d-eaf2e07b658e" />

# 抬起和隐藏画笔
## penup()
+ 一个函数，作用是抬起画笔。
## hideturtle()
+ 一个函数，作用是隐藏海龟画笔。

# 绘制爱心
```python
# 从turtle中导入所有函数
from turtle import *

# 绘制心形
# 使用pensize()函数将画笔粗细设置为5
pensize(5)
# 使用pencolor()函数设置颜色
# 画笔颜色为"red"
pencolor("red")
# 使用fillcolor()函数设置填充颜色
# 填充颜色为"pink"
fillcolor("pink")
# 使用begin_fill()函数准备开始填充图形
begin_fill()
# 使用left()函数向左转135度
left(135)
# 使用forward()函数向前进100步
forward(100)
# 使用right()函数右转180度
right(180)
# 使用circle()函数画半圆，半径为50，角度-180度
circle(50,-180)
# 使用left()函数向左转90度
left(90)
# 使用circle()函数画半圆，半径为50，角度-180度
circle(50,-180)
# 使用right()函数右转180度
right(180)
# 使用forward()函数向前进100步
forward(100)
# 使用end_fill()函数填充完成
end_fill()

# 填充文字
# 使用penup()函数抬起画笔
penup()
# 使用pencolor()函数设置画笔颜色为黑色
pencolor("black")
# 使用goto()函数将画笔移动到坐标(0,80)的位置
goto(0,80)
# 使用hideturtle()函数隐藏画笔
hideturtle()
# 设定write()函数输入内容为"LOVE YOU"，居中对齐，字体为"Arial"和大小为20粗细为"bold"
write("LOVE YOU",align = "center",font=("Arial",20,"bold"))
```


# 画脸
## 脸部画笔初始化：定义函数，设置初始位置
+ 首先，定义一个draw_face()函数绘制脸部
+ 进入函数的主体部分后，第一步需要将小乌龟放置到我们期待的位置：(-120,0)
+ 为了避免留下小乌龟从初始位置移动到(-120,0)的轨迹，我们可以：
+ 🐢penup()抬起小乌龟
+ 🐢goto()把小乌龟移动到目标位置
+ 🐢再使用pendown()放下小乌龟
```python
# 定义draw_face()函数绘制脸部
def draw_face():
    # 抬起画笔
    penup()
    # 移动到坐标点为(-120,0)的地方
    goto(-120,0)
    # 落笔
    pendown()
    # 将画笔颜色设置为黑色"black"
    pencolor("black")
    # 将画笔粗细设置为4
    pensize(4)
 # 调整海龟朝向-90度方向
    seth(-90)
 # 开始填充颜色
    begin_fill()
    # 画圆，圆的半径为130，圆心角为360度
    circle(130,360)
    # 填充颜色为"gold"
    fillcolor("gold")
    # 停止填充颜色
    end_fill()

```

### 使用`seth()`函数，设置画笔朝向-90度的方向开始绘制。

+ 两种调整角度的方法
1.相对角度
  + 以海龟的朝向为基准进行转向。
  + 例如：left(),right()

2.绝对角度
+ 以坐标轴方向为基准调整角度。
  + 例如：seth()
<img width="1727" height="769" alt="屏幕截图_20-8-2026_162831_np baicizhan com" src="https://github.com/user-attachments/assets/ca63c8ba-2e63-4bd5-8e5d-c9d7dd0f723c" />

## 绘制嘴巴
+ 绘制嘴巴可以分为以下几步：

1.画笔移动到坐标点(-80,-10)的位置。
2.朝向-90度的方向
3.绘制一个半径为90的半圆。

```python
# 定义draw_mouth() 函数绘制嘴巴   
def draw_mouth():
    # 抬起画笔
    penup()
    # 移动到坐标点为(-80,-10)的位置
    goto(-80,-10)
    # 落笔
    pendown()
    # 调整海龟朝向-90度方向
    seth(-90)
    # 绘制一个半径为90，圆心角为180的半圆
    circle(90,180)
```

```python
# 导入turtle中的全部函数
from turtle import *
# 定义draw_face()函数绘制脸部
def draw_face():
    # 抬起画笔
    penup()
    # 移动到坐标点为(-120,0)的地方
    goto(-120,0)
    # 落笔
    pendown()
    # 将画笔颜色设置为黑色"black"
    pencolor("black")
    # 将画笔粗细设置为4
    pensize(4)
    # 调整海龟朝向-90度方向
    seth(-90)
    # 开始填充颜色
    begin_fill()
    # 画圆，圆的半径为130，圆心角为360度
    circle(130,360)
    # 填充颜色为"gold"
    fillcolor("gold")
    # 停止填充颜色
    end_fill()
# 定义draw_mouth() 函数绘制嘴巴   
def draw_mouth():
    # 抬起画笔
    penup()
    # 移动到坐标点为(-80,-10)的位置
    goto(-80,-10)
    # 落笔
    pendown()
    # 调整海龟朝向-90度方向
    seth(-90)
    # 绘制一个半径为90，圆心角为180的半圆
    circle(90,180)
# 调用draw_face()函数绘制脸   
draw_face()
# 调用draw_mouth()函数绘制嘴巴
draw_mouth()
```

## 绘制眼白
+ 思考一下，眼白可以怎么绘制呢？
1.从嘴角位置向上直走60步
2.将海龟角度设置为155度
3.将画笔颜色设置为白色，粗度为20
4.绘制一个半径为100，圆心角为45度的圆弧

<img width="1920" height="1918" alt="7-P15" src="https://github.com/user-attachments/assets/798fcc0a-1887-47f2-b868-74f2f38a2dc1" />

```python
# 定义eyes_white()函数绘制眼白   
def eyes_white():
    # 抬起画笔
    penup()
    # 往前直走60步
    forward(60)
    # 将角度调整为155度
    seth(155)
    # 落笔
    pendown()
    # 设置画笔粗细为20
    pensize(20)
    # 设置画笔颜色为"white"
    pencolor("white")
    # 绘制一个半径为100，圆心角为45的弧形
    circle(100,45)
    # 抬笔
    penup()
 ```
### 绘制眼白—part2
1. 抬起画笔，朝向180度的方向（正左）移动40步
2. 角度调整为155度
3. 绘制一个半径为100，圆心角为45度的圆弧
<img width="769" height="290" alt="7-P17" src="https://github.com/user-attachments/assets/077c02ff-417a-42d9-87cb-50ec7f29437e" />

```python
 # 朝向180度方向
    seth(180)
    # 向前走40步
    forward(40)
    # 将角度调整为155度
    seth(155)
    # 落笔
    pendown()
    # 绘制一个半径为100，圆心角为45度的圆弧
    circle(100,45)
    # 抬笔
    penup()
```

## 绘制黑眼珠
1.画笔朝向0度方向，向前移动6步
2.设置画笔粗细为15，颜色为黑色
3.画一个半径为5的圆
4.向前移动110步，再绘制一个半径为5的圆
<img width="2332" height="2251" alt="移动6步" src="https://github.com/user-attachments/assets/0c4222df-e376-417a-9276-361a66869e35" />
```python
# 导入turtle中的全部函数
from turtle import *
# 定义draw_face()函数绘制脸部
def draw_face():
    # 抬起画笔
    penup()
    # 移动到坐标点为(-120,0)的地方
    goto(-120,0)
    # 落笔
    pendown()
    # 将画笔颜色设置为黑色"black"
    pencolor("black")
    # 将画笔粗细设置为4
    pensize(4)
    # 调整海龟朝向-90度方向
    seth(-90)
    # 开始填充颜色
    begin_fill()
    # 画圆，圆的半径为130，圆心角为360度
    circle(130,360)
    # 填充颜色为"gold"
    fillcolor("gold")
    # 停止填充颜色
    end_fill()
# 定义draw_mouth() 函数绘制嘴巴   
def draw_mouth():
    # 抬起画笔
    penup()
    # 移动到坐标点为(-80,-10)的位置
    goto(-80,-10)
    # 落笔
    pendown()
    # 调整海龟朝向-90度方向
    seth(-90)
    # 绘制一个半径为90，圆心角为180的半圆
    circle(90,180)

# 定义eys_white()函数绘制眼白   
def eyes_white():
    # 使用penup()函数抬起画笔
    penup()
    # 使用forward()函数往前直走60步
    forward(60)
    # 使用seth()函数将角度调整为155度
    seth(155)
    # 使用pendown()函数落笔
    pendown()
    # 使用pensize()函数设置画笔粗细为20
    pensize(20)
    # 使用pencolor()函数设置画笔颜色为"white"
    pencolor("white")
    # 使用circle()函数绘制一个半径为100，圆心角为45的弧形
    circle(100,45)
    # 使用penup()函数抬笔
    penup()
    # 使用seth()函数朝向180度方向
    seth(180)
    # 使用forward()函数向前走40步
    forward(40)
    # 使用seth()函数将角度调整为155度
    seth(155)
    # 使用pendown()函数落笔
    pendown()
    # 使用circle()函数绘制一个半径为100，圆心角为45度的圆弧
    circle(100,45)
    # 使用penup()函数抬笔
    penup()

#  定义一个eyes_black()函数绘制黑眼珠
def eyes_black():
    # 使用seth()函数将角度设置为0
    seth(0)
    # 使用forward()函数前进6步
    forward(6)
    # 使用pendown()函数落笔
    pendown()
    # 使用pensize()函数设置画笔粗细为15
    pensize(15)
    # 使用pencolor()函数设置画笔颜色为"black"
    pencolor("black")
    # 使用circle()函数绘制一个半径为5，圆心角为360度
    circle(5,360)
    # 使用penup()函数抬笔
    penup()
    # 使用forward()函数前进110步
    forward(110)
    # 使用pendown()函数落笔
    pendown()
    # 使用circle()函数绘制一个半径为5的圆
    circle(5,360)
    # 使用hideturtle()函数隐藏画笔
    hideturtle()
    
# 调用draw_face()函数画脸
draw_face()
# 调用draw_mouth()函数画嘴巴
draw_mouth()
# 调用eyes_white()函数画白眼珠
eyes_white()
# 调用eyes_black()函数画黑眼珠
eyes_black()

```

# 运动控制
<img width="1114" height="692" alt="画笔运动命令-f" src="https://github.com/user-attachments/assets/e076d555-5775-4f29-a4f3-86bcb547fb54" />
# 画笔控制
<img width="1114" height="936" alt="画笔控制命令-f" src="https://github.com/user-attachments/assets/df1224a4-4363-4558-bf18-4293ec757014" />
# 全局控制命令
<img width="2068" height="1080" alt="0652f52d42562a141bb7c70964bc659d" src="https://github.com/user-attachments/assets/cce64feb-3eae-4351-829b-c563f9e0a233" />




