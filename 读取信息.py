import pandas as pd


s=pd.Series([1,2,3,4,5],index=["a","b","c","d","e"])
print(s)
print(s.index)
#NumPy和数组
import numpy as np
#二维数组
arr=np.array([[1,2,3],[4,5,6]])
print(arr)

#Series
info=pd.Series([1,2,3],index=["a","b","c"])
print(info)

#DataFrame 数据框
##定义一个字典和列表
data2={"rank":[1,2,3],"GDP":[1000,2000,3000]}
city=["北京","上海","广州"]
df=pd.DataFrame(data2,index=city)