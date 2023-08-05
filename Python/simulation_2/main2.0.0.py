import pandas as pd

# 1. 读取两个Excel文件并合并
df1 = pd.read_excel('C:\\Users\\19855\\Desktop\\附件2 慢性病及相关因素流调数据 更改1.xlsx')
df2 = pd.read_excel('G:\\updated_data_processed.xlsx')

df = pd.merge(df1, df2, on='ID')  # 假设'D'是两个表中的共同列

# 2. 去掉有缺失值的数据
df = df.dropna(subset=['出生年', '性别', '文化程度', '婚姻状况', '职业'])

# 3. 将出生日期转化为年龄
df['年龄'] = 2023 - df['出生年']

# 4. 将年龄分为4段
bins = [0, 18, 45, 65, df['年龄'].max()]
labels = [1, 2, 3, 4]
df['年龄段'] = pd.cut(df['年龄'], bins=bins, labels=labels)

# 5. 统计每个年龄段的人数
age_counts = df['年龄段'].value_counts().sort_index()
print(age_counts)

# 保存到新的Excel文件
df.to_excel('G:\\第二问数据处理.xlsx', index=False)