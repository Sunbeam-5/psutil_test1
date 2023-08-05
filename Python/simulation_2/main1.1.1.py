import pandas as pd
import os

# 读取Excel文件
df = pd.read_excel('G:\\updated_data.xlsx')

# 获取列名列表
columns = df.columns.tolist()

# 遍历每一列
for column_name in ['大米', '小麦面粉', '杂粮', '薯类', '油炸面食', '猪肉', '牛羊肉', '禽肉', '内脏类', '水产类', '鲜奶', '奶粉', '酸奶', '蛋类', '豆腐', '豆腐丝等', '豆浆', '干豆', '新鲜蔬菜', '海草类', '咸菜', '泡菜', '酸菜', '糕点', '水果', '果汁饮料', '其他饮料']:
    # 获取列名
    column_freq_day = f'食用{column_name}的频率（次数/天）'
    column_freq_week = f'食用{column_name}的频率（次数/周）'
    column_freq_month = f'食用{column_name}的频率（次数/月）'
    column_avg = f'{column_name}平均每次食用量'
    column_eat = f'是否吃{column_name}'

    # 根据“是否吃{column_name}”的值进行处理
    for i in range(len(df)):
        if df[column_eat][i] == 2:
            # 如果不吃，则将“频率”和“平均每次食用量”设为0
            df[column_freq_month][i] = 0
            df[column_avg][i] = 0
        elif df[column_eat][i] == 1:
            # 如果吃，则根据“频率”的单位进行转换
            if pd.notna(df[column_freq_day][i]):
                df[column_freq_month][i] = df[column_freq_day][i] * 30
            elif pd.notna(df[column_freq_week][i]):
                df[column_freq_month][i] = df[column_freq_week][i] * 4
            # 删除“频率”的原始列
            df.drop([column_freq_day, column_freq_week], axis=1, inplace=True)

    # 删除列名
    df.drop(column_eat, axis=1, inplace=True)

# 将转换后的结果保存到G盘
if os.path.exists("G:\\"):
    df.to_excel('G:\\converted_data.xlsx', index=False)
    print("文件保存成功")
else:
    print("G盘不存在")