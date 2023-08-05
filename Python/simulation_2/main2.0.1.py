import pandas as pd

# 食品列表
food_list = ['大米', '小麦面粉', '杂粮', '薯类', '油炸面食', '猪肉', '牛羊肉', '禽肉', '内脏类', '水产类',
             '鲜奶', '奶粉', '酸奶', '蛋类', '豆腐', '豆腐丝等', '豆浆', '干豆', '新鲜蔬菜', '海草类',
             '咸菜', '泡菜', '酸菜', '糕点', '水果', '果汁饮料', '其他饮料']

for column_name in food_list:
    # 读取两个Excel文件
    df1 = pd.read_excel('C:\\Users\\19855\\Desktop\\附件2 慢性病及相关因素流调数据 更改1.xlsx')
    df2 = pd.read_excel('G:\\数据处理.xlsx')

    # 只保留需要的列
    df1 = df1[['ID', '出生年', '性别', '文化程度', '婚姻状况', '职业']]
    df2 = df2[['ID', f'是否吃{column_name}', f'食用{column_name}的频率（次数/月）', f'{column_name}平均每次食用量']]

    # 按照 'ID' 列合并两个 DataFrames
    df = pd.merge(df1, df2, on='ID')

    # 去掉有缺失值的数据
    df = df.dropna()

    # 将出生日期转化为年龄
    df['年龄'] = 2023 - df['出生年']

    # 将年龄分为4段
    bins = [0, 18, 45, 65, df['年龄'].max()]
    labels = [1, 2, 3, 4]
    df['年龄段'] = pd.cut(df['年龄'], bins=bins, labels=labels)

    # 统计每个年龄段吃每种食品的人数
    food_counts = df[df[f'是否吃{column_name}'] == '是'].groupby('年龄段')['ID'].count()
    print(f'{column_name}吃的人数：\n{food_counts}')

    # 保存到新的Excel文件
    df.to_excel(f'G:\\{column_name}数据处理.xlsx', index=False)