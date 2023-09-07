import os

path = r"G:\相册"  # 指定路径

# 循环创建文件夹
for year in range(2016, 2018):
    for month in range(1, 13):
        folder_name = f"{year}年{month}月"
        folder_path = os.path.join(path, folder_name)
        os.makedirs(folder_path, exist_ok=True)