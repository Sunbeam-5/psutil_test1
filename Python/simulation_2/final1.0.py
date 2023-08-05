import numpy as np
import pandas as pd

def fill_missing_values(data, column_name):
    # 根据其他列填充缺失值
    data.loc[data[[f'食用{column_name}的频率（次数/天）', f'食用{column_name}的频率（次数/周）', f'食用{column_name}的频率（次数/月）', f'{column_name}平均每次食用量']].isnull().all(axis=1), f'是否{column_name}'] = 2
    data.loc[data[f'是否吃{column_name}'].isnull(), f'是否吃{column_name}'] = 1
    return data

# 读取Excel文件
data = pd.read_excel(r'C:\Users\19855\Desktop\附件2 慢性病及相关因素流调数据 更改1.xlsx')

# 处理所有类似的列
columns_to_fill = ['大米', '小麦面粉', '杂粮', '薯类', '油炸面食', '猪肉','牛羊肉','禽肉','内脏类','水产类','鲜奶','奶粉','酸奶','蛋类','豆腐','豆腐丝等','豆浆','干豆','新鲜蔬菜','海草类','咸菜','泡菜','酸菜','糕点','水果','果汁饮料','其他饮料']
for column in columns_to_fill:
    data = fill_missing_values(data, column)

# 读取 Excel 文件
df = pd.read_excel(r'C:\Users\19855\Desktop\附件2 慢性病及相关因素流调数据 更改1.xlsx')

# 食品列表
food_list = ['大米', '小麦面粉', '杂粮', '薯类', '油炸面食', '猪肉', '牛羊肉', '禽肉', '内脏类', '水产类',
             '鲜奶', '奶粉', '酸奶', '蛋类', '豆腐', '豆腐丝等', '豆浆', '干豆', '新鲜蔬菜', '海草类',
             '咸菜', '泡菜', '酸菜', '糕点', '水果', '果汁饮料', '其他饮料']

# 循环处理每种食品的数据
for column_name in food_list:
    # 针对"是否吃{column_name}"为2的情况
    df.loc[df[f'是否吃{column_name}'] == 2, f'食用{column_name}的频率（次数/月）'] = 0
    df.loc[df[f'是否吃{column_name}'] == 2, f'{column_name}平均每次食用量'] = 0

    # 如果"{column_name}的频率（次数/天）"、"{column_name}的频率（次数/周）"、"{column_name}的频率（次数/月）"或"{column_name}平均每次食用量"这几个列中任意存在非空值，则将"是否吃{column_name}"列的值设为1，否则设为2
    if df[[f'食用{column_name}的频率（次数/天）', f'食用{column_name}的频率（次数/周）', f'食用{column_name}的频率（次数/月）',f'{column_name}平均每次食用量']].notnull().any().any():
        df['是否吃' + column_name] = np.where(df[[f'食用{column_name}的频率（次数/天）', f'食用{column_name}的频率（次数/周）',f'食用{column_name}的频率（次数/月）', f'{column_name}平均每次食用量']].notnull().any(axis=1), 1, 2)

    # 针对"是否吃{column_name}"为1的情况
    if df[f'食用{column_name}的频率（次数/月）'].isnull().any():
        df.loc[df[f'是否吃{column_name}'] == 1 & df[f'食用{column_name}的频率（次数/月）'].isnull(), f'食用{column_name}的频率（次数/月）'] = df.loc[df[f'是否吃{column_name}'] == 1 & df[f'食用{column_name}的频率（次数/月）'].isnull(), f'食用{column_name}的频率（次数/天）'] * 30
        df.loc[df[f'是否吃{column_name}'] == 1 & df[f'食用{column_name}的频率（次数/月）'].isnull(), f'食用{column_name}的频率（次数/月）'] = df.loc[df[f'是否吃{column_name}'] == 1 & df[f'食用{column_name}的频率（次数/月）'].isnull(), f'食用{column_name}的频率（次数/周）'] * 4

# 保留所需的列
columns_to_keep = ['ID']
for column_name in food_list:
    columns_to_keep += [f'是否吃{column_name}', f'食用{column_name}的频率（次数/月）', f'{column_name}平均每次食用量']
df = df[columns_to_keep]



# 保存到新的 Excel 文件
df.to_excel('G:\\第一问最终数据.xlsx', index=False)