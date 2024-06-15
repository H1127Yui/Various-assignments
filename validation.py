import os

def check_files_in_directory(directory):
    # 检查目录是否存在
    if not os.path.exists(directory):
        #print(f"目录 {directory} 不存在")
        return False
    
    # 检查目录是否为空
    if not os.listdir(directory):
        #print(f"目录 {directory} 为空")
        return False
    
    # 检查目录内是否有文件
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path):
            #print(f"目录 {directory} 内有文件")
            return True
    
    #print(f"目录 {directory} 内没有文件")
    return False
