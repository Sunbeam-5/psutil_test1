import pandas as pd

# 读取Excel文件
df = pd.read_excel('G:\\updated_data.xlsx')

# 食品列表
food_list = ['大米', '小麦面粉', '杂粮', '薯类', '油炸面食', '猪肉', '牛羊肉', '禽肉', '内脏类', '水产类',
             '鲜奶', '奶粉', '酸奶', '蛋类', '豆腐', '豆腐丝等', '豆浆', '干豆', '新鲜蔬菜', '海草类',
             '咸菜', '泡菜', '酸菜', '糕点', '水果', '果汁饮料', '其他饮料']

# 循环处理每种食品的数据
for column_name in food_list:
    # 针对"是否吃{column_name}"为2的情况
    df.loc[df[f'是否吃{column_name}'] == 2, f'食用{column_name}的频率（次数/月）'] = 0
    df.loc[df[f'是否吃{column_name}'] == 2, f'{column_name}平均每次食用量'] = 0

    # # 针对"是否吃{column_name}"为1的情况     食用{column_name}的频率（次数/月）
    # df.loc[df[f'是否吃{column_name}'] == 1, f'食用{column_name}的频率（次数/月）'] = df.loc[df[f'是否吃{column_name}'] == 1, f'食用{column_name}的频率（次数/天）'] * 30
    # df.loc[df[f'是否吃{column_name}'] == 1, f'食用{column_name}的频率（次数/月）'] = df.loc[df[f'是否吃{column_name}'] == 1, f'食用{column_name}的频率（次数/周）'] * 4

    # # 针对"是否吃{column_name}"为1的情况     食用{column_name}的频率（次数/月）
    # if df[f'食用{column_name}的频率（次数/月）'].isnull().any():
    #     df.loc[df[f'是否吃{column_name}'] == 1, f'食用{column_name}的频率（次数/月）'] = df.loc[df[f'是否吃{column_name}'] == 1, f'食用{column_name}的频率（次数/天）'] * 30
    #     df.loc[df[f'是否吃{column_name}'] == 1, f'食用{column_name}的频率（次数/月）'] = df.loc[df[f'是否吃{column_name}'] == 1, f'食用{column_name}的频率（次数/周）'] * 4

    # 针对"是否吃{column_name}"为1的情况     食用{column_name}的频率（次数/月）
    if df[f'食用{column_name}的频率（次数/月）'].isnull().any():
        df.loc[df[f'是否吃{column_name}'] == 1 & df[f'食用{column_name}的频率（次数/月）'].isnull(), f'食用{column_name}的频率（次数/月）'] = df.loc[df[f'是否吃{column_name}'] == 1 & df[f'食用{column_name}的频率（次数/月）'].isnull(), f'食用{column_name}的频率（次数/天）'] * 30
        df.loc[df[f'是否吃{column_name}'] == 1 & df[f'食用{column_name}的频率（次数/月）'].isnull(), f'食用{column_name}的频率（次数/月）'] = df.loc[df[f'是否吃{column_name}'] == 1 & df[f'食用{column_name}的频率（次数/月）'].isnull(), f'食用{column_name}的频率（次数/周）'] * 4
# # 删除不需要的列
# columns_to_drop = [f'食用{food}的频率（次数/天）' for food in food_list] + [f'食用{food}的频率（次数/周）' for food in food_list]
# df = df.drop(columns=columns_to_drop)

# 保留所需的列
columns_to_keep = ['ID']
for column_name in food_list:
    columns_to_keep += [f'是否吃{column_name}', f'食用{column_name}的频率（次数/月）', f'{column_name}平均每次食用量']
df = df[columns_to_keep]

# 保存到新的Excel文件
df.to_excel('G:\\第一问处理数据.xlsx', index=False)