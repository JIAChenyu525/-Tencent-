import pandas as pd
import matplotlib.pyplot as plt

tencent_stock_data = pd.read_csv("D:/wenjian/tencent_stock_data.csv") # 读取数据
print(tencent_stock_data.head())
print(tencent_stock_data.dtypes) # 查看类型
print(tencent_stock_data.shape) # 查看几行几列

tencent_stock_data.plot() # 混合折线图

tencent_stock_data.plot.scatter(x="date", y="volume tcehy", alpha=0.5) # 日期x与成交量y,透明度为0.5的视图

tencent_stock_data.plot.box() # 箱线图

tencent_stock_data.plot.area(figsize=(12, 4), subplots=True) # 分为多个子图可视化分析👍

fig, axs = plt.subplots(figsize=(12, 4))
tencent_stock_data.plot.area(ax=axs)
axs.set_ylabel("volume tcehy") # 以成交量为参考的可视化图
fig.savefig("路径") # 保存视图

plt.show()