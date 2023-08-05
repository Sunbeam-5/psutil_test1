import pandas as pd
import numpy as np

def fill_missing_values(data, column_name):
    # 根据其他列填充缺失值
    data.loc[data[[f'食用{column_name}的频率（次数/天）', f'食用{column_name}的频率（次数/周）', f'食用{column_name}的频率（次数/月）', f'{column_name}平均每次食用量']].isnull().all(axis=1), f'是否{column_name}'] = 2
    data.loc[data[f'是否吃{column_name}'].isnull(), f'是否吃{column_name}'] = 1
    return data

# 读取Excel文件
data = pd.read_excel(r'C:\Users\19855\AppData\Roaming\spsspro\spsspro\jupyter\notebook\影响城市居民身体健康的因素分析\附件2 慢性病及相关因素流调数据 (1).xlsx')

# 处理所有类似的列
columns_to_fill = ['大米', '小麦面粉', '杂粮', '薯类', '油炸面食', '猪肉','牛羊肉','禽肉','内脏类','水产类','鲜奶','奶粉','酸奶','蛋类','豆腐','豆腐丝等','豆浆','干豆','新鲜蔬菜','海草类','咸菜','泡菜','酸菜','糕点','水果','果汁饮料','其他饮料']
for column in columns_to_fill:
    data = fill_missing_values(data, column)

# 直接修改源文件
data.to_excel(r'C:\Users\19855\AppData\Roaming\spsspro\spsspro'
              r'\jupyter\notebook\影响城市居民身体健康的因素分析\附件2 慢性病及相关因素流调数据 (1).xlsx', index=False)