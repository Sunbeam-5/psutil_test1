import pandas as pd

#读取两个Excel文件
df1 = pd.read_excel('C:\\Users\\19855\\Desktop\\附件2 慢性病及相关因素流调数据 更改1.xlsx')
df2 = pd.read_excel('G:\\数据处理.xlsx')

#只保留需要的列
df1 = df1[['ID', '出生年', '性别', '文化程度', '婚姻状况', '职业']]
df2 = df2[['ID', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 'D13', 'D14', 'D15', 'D16',
'D17', 'D18', 'D19', 'D20', 'D21', 'D22', 'D23', 'D24', 'D25', 'D26', 'D27', 'D28', 'D29',
'D30', 'D31', 'D32', 'D33', 'D34', 'D35', 'D36', 'D37']]

#按照 'ID' 列合并两个 DataFrames
merged_df = pd.merge(df1, df2, on='ID')

#去掉有缺失值的数据
merged_df = merged_df.dropna(subset=['职业', '婚姻状况'])

#将出生日期转化为年龄
merged_df['年龄'] = 2023 - merged_df['出生年']

#将年龄分为4段
bins = [0, 18, 45, 65, merged_df['年龄'].max()]
labels = [1, 2, 3, 4]
merged_df['年龄段'] = pd.cut(merged_df['年龄'], bins=bins, labels=labels)

#统计各年龄段的人数
age_counts = merged_df['年龄段'].value_counts()

#输出各年龄段的人数
print("0-18岁居民有:", age_counts[1])
print("18-45岁居民有:", age_counts[2])
print("45-65岁居民有:", age_counts[3])
print("65+岁居民有:", age_counts[4])

#保存到新的Excel文件
merged_df.to_excel('G:\第二问数据处理_1.xlsx', index=False)