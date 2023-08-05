import numpy as np
import pandas as pd

# 读取Excel文件
data = pd.read_excel(r'C:\Users\19855\Desktop\附件2 慢性病及相关因素流调数据 更改1.xlsx')

# 食品列表
food_list = ['大米', '小麦面粉', '杂粮', '薯类', '油炸面食', '猪肉', '牛羊肉', '禽肉', '内脏类', '水产类',
             '鲜奶', '奶粉', '酸奶', '蛋类', '豆腐', '豆腐丝等', '豆浆', '干豆', '新鲜蔬菜', '海草类',
             '咸菜', '泡菜', '酸菜', '糕点', '水果', '果汁饮料', '其他饮料']

# 循环处理每种食品的数据
for food in food_list:
    # 针对"是否吃{food}"为2的情况
    data.loc[data[f'是否吃{food}'] == 2, [f'食用{food}的频率（次数/月）', f'{food}平均每次食用量']] = 0

    # 针对"是否吃{food}"为1的情况
    freq_cols = [f'食用{food}的频率（次数/{freq})' for freq in ['天', '周', '月']]
    data.loc[data[f'是否吃{food}'] == 1, freq_cols] = data.loc[data[f'是否吃{food}'] == 1, freq_cols].fillna(0)

    # 根据日、周频率计算月频率
    data[f'食用{food}的频率（次数/月）'] = data[f'食用{food}的频率（次数/天）'] * 30 + data[f'食用{food}的频率（次数/周）'] * 4



# 保留所需的列
columns_to_keep = ['ID'] + [(f'是否吃{food}', f'食用{food}的频率（次数/月）', f'{food}平均每次食用量') for food in food_list]
data = data[columns_to_keep]

# 保存到新的 Excel 文件
data.to_excel('G:\\第一问最终数据.xlsx', index=False)