import pandas as pd

# 读取Excel文件
df = pd.read_excel("G:/updated_data.xlsx")

# 对每个食品进行处理
for column_name in ['大米', '小麦面粉', '杂粮', '薯类', '油炸面食', '猪肉', '牛羊肉', '禽肉', '内脏类', '水产类', '鲜奶', '奶粉', '酸奶', '蛋类', '豆腐',
                    '豆腐丝等', '豆浆', '干豆', '新鲜蔬菜', '海草类', '咸菜', '泡菜', '酸菜', '糕点', '水果', '果汁饮料', '其他饮料']:

    # 如果“是否吃{column_name}”的值为“2”
    if (df[f'是否吃{column_name}'] == 2).any():
        # 使用条件索引选择“是否吃{column_name}”列中的值为 2 的行，并将“食用{column_name}的频率（次数/月）”和“{column_name}平均每次食用量”两列的值设置为 0
        df.loc[df[f'是否吃{column_name}'] == 2, ['食用{column_name}的频率（次数/月）', f'{column_name}平均每次食用量']] = 0

    # 如果“是否吃{column_name}”的值为“1”
    elif df[f'是否吃{column_name}'].any() == 1:
        column_freq_day = f'食用{column_name}的频率（次数/天）'
        column_freq_week = f'食用{column_name}的频率（次数/周）'
        column_freq_month = f'食用{column_name}的频率（次数/月）'
        column_avg = f'{column_name}平均每次食用量'

        for i in range(len(df)):
            if pd.notna(df[column_freq_day][i]):
                df.loc[i, column_freq_month] = df.loc[i, column_freq_day] * 30
            elif pd.notna(df[column_freq_week][i]):
                df.loc[i, column_freq_month] = df.loc[i, column_freq_week] * 4

    # 如果“是否吃{column_name}”的值为其他
    else:
        pass

# 将结果保存到Excel文件
df.drop([f'食用{column_name}的频率（次数/天）', f'食用{column_name}的频率（次数/周）'], axis=1, inplace=True)
df.to_excel("G:/output_data.xlsx", index=False)