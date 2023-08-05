import numpy as np
import pandas as pd

def fill_missing_values(data, column_name):
    # 根据其他列填充缺失值
    data[f'是否吃{column_name}'] = data[f'是否吃{column_name}'].fillna(1)
    data[[f'食用{column_name}的频率（次数/天）', f'食用{column_name}的频率（次数/周）', f'食用{column_name}的频率（次数/月）', f'{column_name}平均每次食用量']] = data[[f'食用{column_name}的频率（次数/天）', f'食用{column_name}的频率（次数/周）', f'食用{column_name}的频率（次数/月）', f'{column_name}平均每次食用量']].fillna(0)
    return data

# 读取 Excel 文件
data = pd.read_excel(r'C:\Users\19855\Desktop\附件2 慢性病及相关因素流调数据 更改1.xlsx')

# 处理所有类似的列
columns_to_fill = ['大米', '小麦面粉', '杂粮', '薯类', '油炸面食', '猪肉', '牛羊肉', '禽肉', '内脏类', '水产类', '鲜奶', '奶粉', '酸奶', '蛋类', '豆腐', '豆腐丝等', '豆浆', '干豆', '新鲜蔬菜', '海草类', '咸菜', '泡菜', '酸菜', '糕点', '水果', '果汁饮料', '其他饮料']
for column in columns_to_fill:
    data = fill_missing_values(data, column)

# 针对每种食品的数据进行处理
for column_name in columns_to_fill:
    # 针对"是否吃{column_name}"为2的情况
    data.loc[data[f'是否吃{column_name}'] == 2, f'食用{column_name}的频率（次数/月）'] = 0
    data.loc[data[f'是否吃{column_name}'] == 2, f'{column_name}平均每次食用量'] = 0

    # 如果"{column_name}的频率（次数/天）"、"{column_name}的频率（次数/周）"、"{column_name}的频率（次数/月）"或"{column_name}平均每次食用量"这几个列中任意存在非空值，则将"是否吃{column_name}"列的值设为1，否则设为2
    if data[[f'食用{column_name}的频率（次数/天）', f'食用{column_name}的频率（次数/周）', f'食用{column_name}的频率（次数/月）',f'{column_name}平均每次食用量']].notnull().any().any():
        data.loc[data[[f'食用{column_name}的频率（次数/天）', f'食用{column_name}的频率（次数/周）',f'食用{column_name}的频率（次数/月）', f'{column_name}平均每次食用量']].notnull().any(axis=1), f'是否吃{column_name}'] = 1
        data.loc[~data[[f'食用{column_name}的频率（次数/天）', f'食用{column_name}的频率（次数/周）',f'食用{column_name}的频率（次数/月）', f'{column_name}平均每次食用量']].notnull().any(axis=1), f'是否吃{column_name}'] = 2
    else:
        data[f'是否吃{column_name}'] = 2

    # 针对"是否吃{column_name}"为1的情况
    data.loc[data[f'是否吃{column_name}'] == 1, f'{column_name}平均每次食用量'] = data.loc[data[f'是否吃{column_name}'] == 1, f'{column_name}平均每次食用量'].fillna(data[f'{column_name}平均每次食用量'].median())

# 保留所需的列
columns_to_keep = ['ID'] + [f'是否吃{column_name}' for column_name in columns_to_fill] + [f'食用{column_name}的频率（次数/月）' for column_name in columns_to_fill] + [f'{column_name}平均每次食用量' for column_name in columns_to_fill]
data = data.filter(columns_to_keep)

# 将结果保存到 Excel 文件中
data.to_excel(r'C:\Users\19855\Desktop\处理后的数据.xlsx', index=False)