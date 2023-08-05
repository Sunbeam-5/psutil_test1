import pandas as pd
import matplotlib.pyplot as plt

# 读取Excel数据
df = pd.read_excel('G:\第二问数据处理_2.xlsx')

# 统计不同年龄段的人数
age_counts = df['年龄段'].value_counts()

# 添加缺失的年龄段并设置人数为0
age_labels = ['0-18岁', '18-45岁', '45-65岁', '65+岁']
age_counts = age_counts.reindex(age_labels, fill_value=0)

# 绘制柱状图
plt.bar(age_labels, age_counts)
plt.xlabel('年龄段')
plt.ylabel('人数')
plt.title('不同年龄段的人数统计')

# 显示图形
plt.show()