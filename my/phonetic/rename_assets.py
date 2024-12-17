import os
import re

def rename_assets(html_file, assets_folder, prefix="resource_"):
    # 获取资源文件夹中的文件列表
    files = sorted(os.listdir(assets_folder))
    rename_map = {}

    # 重命名资源文件
    for index, file_name in enumerate(files):
        old_path = os.path.join(assets_folder, file_name)
        if os.path.isfile(old_path):
            extension = os.path.splitext(file_name)[1]
            new_name = f"{prefix}{index + 1}{extension}"
            new_path = os.path.join(assets_folder, new_name)
            os.rename(old_path, new_path)
            rename_map[file_name] = new_name

    # 读取 HTML 文件并更新引用
    with open(html_file, "r", encoding="utf-8") as file:
        html_content = file.read()

    for old_name, new_name in rename_map.items():
        # 替换 HTML 中的文件引用
        html_content = re.sub(rf'(["\'/]){re.escape(old_name)}(["\'/])', rf'\1{new_name}\2', html_content)

    # 写回更新后的 HTML 文件
    with open(html_file, "w", encoding="utf-8") as file:
        file.write(html_content)

    print("资源重命名并更新 HTML 文件完成！")

# 使用示例
html_file_path = "index.html"  # HTML 文件的路径
assets_folder_path = "assets"  # 资源文件夹的路径
rename_assets(html_file_path, assets_folder_path)
