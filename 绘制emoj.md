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
