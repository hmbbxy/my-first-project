# 将 PPT 中的结构按照层级关系来排列是这样的：
+ 幻灯片页 -> 形状 -> 文本框 -> 段落 -> 样式块
<img width="1560" height="1200" alt="P10" src="https://github.com/user-attachments/assets/eeeaefe5-532e-4f39-abb7-7779a10cac6b" />

+  由于 PPT 有多级结构，想要得到所有的文字内容，那就要从头开始层层读取。
1.  第一步，读取文件；
2.  第二步，读取指定幻灯片页；
3.  第三步，读取指定形状；
4.  第四步，读取文本框内的文本内容。

# 读取指定.pptx文件
+ 使用了 `Presentation()` 函数，可以读取指定路径中的 .pptx 文件，返回一个 Presentation 对象
```python
from pptx import Presentation
path = "/Users/yequ.pptx"
pptxFile = Presentation(path)
print(pptxFile)
```

# 读取幻灯片页
+ 读取 .pptx 文件后，我们可以访问 Presentation 中的 .slides 属性，获取幻灯片页序列。
+ 幻灯片页序列中包含所有幻灯片页对象，可以使用索引定位到单个幻灯片页对象；
+ 获取PPT第一张幻灯片页对象：
`slide = pptxFile.slides[0]`
+ 也可以使用 for 循环读取所有幻灯片页对象。

```python
# 使用from...import从pptx模块中导入Presentation
from pptx import Presentation

# 将.pptx文件路径赋值给变量path
path = "/Users/xiaohe/statistics.pptx"

# 读取path并赋值给变量pptxFile
pptxFile = Presentation(path)

# TODO for循环遍历pptxFile中.slides属性，并赋值给slide
for slide in pptxFile.slides:
    # TODO print()输出slide
    print(slide)
```

# 读取形状
+ 可以访问幻灯片页对象中的 .shapes 属性，获取形状序列。

```python
# 使用from...import从pptx模块中导入Presentation
from pptx import Presentation

# 将.pptx文件路径赋值给变量path
path = "/Users/xiaohe/statistics.pptx"

# 读取path并赋值给变量pptxFile
pptxFile = Presentation(path)

# for循环遍历pptxFile中.slides属性，并赋值给slide
for slide in pptxFile.slides:
    # for循环遍历slide中.shapes属性，赋值给变量shape
    for shape in slide.shapes:
        # print()输出shape
        print(shape)
```

+ 思考一下，是不是每个形状中都有文本框呢？
+ 形状可以按照是否含有文本分为两类，一类是含有文本框的形状，另一类是纯图片的形状。
+ 所以，我们要将纯图片的形状排除，再从文本框中提取文字内容。

# 读取文本框
+ 判断文本框
+ 访问形状对象中的 .has_text_frame 属性，判断形状中是否存在文本框，返回布尔数。
  + 与 if 语句相结合，如果形状中存在文本框，就执行接下来的操作。
```python
if shape.has_text_frame == True:   
    texts = shape.text_frame
```

+ 注意，由于一个形状只有一个文本框，.text_frame 属性获取的是单个文本框对象

```python
# 使用from...import从pptx模块中导入Presentation
from pptx import Presentation

# 将.pptx文件路径赋值给变量path
path = "/Users/xiaohe/statistics.pptx"

# 读取path并赋值给变量pptxFile
pptxFile = Presentation(path)

# for循环遍历pptxFile中的.slides属性，赋值给slide
for slide in pptxFile.slides:
    # for循环遍历slide中.shapes属性，赋值给变量shape
    for shape in slide.shapes:
        # 判断形状中是否有文本框
        if shape.has_text_frame == True:
            # 读取形状中的文本框，并赋值给变量textFrame
            textFrame = shape.text_frame
            # print()输出textFrame.text
            print(textFrame.text)
```

+ 在这里，我们需要知道一个小规则，就是写入 Word 文档的内容样式要保持一致。
+ 也就是说，一段文本内容为一个样式块，就可以写入 Word 文档。如果一段文本内容包含多个样式块，写入 Word 文档时，就可能发生报错。
+ 所以要以*样式块*为最小单位提取文本内容，再把每个样式块写入 Word 文档中

# 读取段落
+ 刚才我们获取了文本框对象，再往下一层读取，需要访问 .paragraphs 属性，返回文本框中的段落序列
```python
# 使用from...import从pptx模块中导入Presentation
from pptx import Presentation

# 将.pptx文件路径赋值给变量path
path = "/Users/xiaohe/statistics.pptx"

# 读取path并赋值给变量pptxFile
pptxFile = Presentation(path)

# for循环遍历pptxFile中的.slides属性，赋值给slide
for slide in pptxFile.slides:

    # for循环遍历slide中.shapes属性，赋值给变量shape
    for shape in slide.shapes:
        # 判断形状中是否有文本框
        if shape.has_text_frame == True:
            # 读取形状中的文本框，并赋值给变量textFrame
            textFrame = shape.text_frame
        
            # for循环遍历文本框内的所有段落
            # 赋值给变量paragraph
            for paragraph in textFrame.paragraphs:
                # print()输出paragraph
                print(paragraph)
```

# 读取样式块的文本内容
+ 获取了所有段落对象后，接下来就访问段落对象的 .runs 属性，就可以获得段落中的样式块序列。
```python
# 使用from...import从pptx模块中导入Presentation
from pptx import Presentation

# 将.pptx文件路径赋值给变量path
path = "/Users/xiaohe/statistics.pptx"

# 读取path并赋值给变量pptxFile
pptxFile = Presentation(path)

# for循环遍历pptxFile中的.slides属性，赋值给slide
for slide in pptxFile.slides:

    # for循环遍历slide中.shapes属性，赋值给变量shape
    for shape in slide.shapes:
        # 判断形状中是否有文本框
        if shape.has_text_frame == True:
            # 读取形状中的文本框，并赋值给变量textFrame
            textFrame = shape.text_frame
        
            # for循环遍历文本框内的所有段落
            # 赋值给变量paragraph
            for paragraph in textFrame.paragraphs:
                # for循环遍历段落中的所有样式块
                # 赋值给变量run
                for run in paragraph.runs:
                    # 读取样式块中的文本内容，并赋值给变量texts
                    texts = run.text
                    # print()输出texts
                    print(texts)
```
