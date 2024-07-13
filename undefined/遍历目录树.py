import os


def print_directory_structure(root_dir, prefix='', level=0):
    try:
        items = os.listdir(root_dir)
    except PermissionError:
        print(f"{prefix}├── [Permission Denied]")
        return

    items = [item for item in items if not item.startswith('.')]  # 忽略隐藏文件
    items.sort()

    for i, item in enumerate(items):
        path = os.path.join(root_dir, item)
        if i == len(items) - 1:
            new_prefix = prefix + '└── '
            next_prefix = prefix + '    '
        else:
            new_prefix = prefix + '├── '
            next_prefix = prefix + '│   '

        if os.path.isdir(path):
            print(f"{new_prefix}{item}")
            print_directory_structure(path, next_prefix, level + 1)
        else:
            print(f"{new_prefix}{item}")


# 获取当前目录
current_dir = os.getcwd()
print_directory_structure(current_dir)
