import tkinter as tk
from tkinter import messagebox
import numpy as np

# 全局变量用于存储矩阵 P_np
P_np_global = None
flag = 1

def is_valid(c: str) -> bool:
    # 判断 c 是否是一个 0-9 的数字
    if c.isdigit():
        return True
    # 判断 c 是否是字符 "e"
    elif c == 'e':
        return True
    elif c == '':
        return True
    # 如果 c 不是数字也不是字符 "e"，则返回 False
    return False

def create_ui(root, rows, cols):
    matrix_entries = []
    entry_width = 5  # 每个输入框的宽度
    entry_height = 2  # 每个输入框的高度
    padx = 5  # 水平间距
    pady = 5  # 垂直间距
    
    for i in range(rows):
        row_entries = []
        for j in range(cols):
            entry = tk.Entry(root, width=entry_width, justify='center')
            entry.grid(row=i, column=j, padx=padx, pady=pady)
            row_entries.append(entry)
        matrix_entries.append(row_entries)
    
    submit_button = tk.Button(root, text="提交", command=lambda: submit(matrix_entries, rows, cols))
   
    submit_button.grid(row=rows, column=0, columnspan=cols, pady=10)
    
    # 计算窗口大小
    window_width = cols * (entry_width * 10 + padx) + padx
    window_height = rows * (entry_height * 10 + pady) + pady + 50  # 额外加上按钮的高度
    
    root.geometry(f"{window_width}x{window_height}")

def submit(matrix_entries, rows, cols):
    global P_np_global
    P = []
    for i in range(rows):
        row = []
        for j in range(cols):
            value = matrix_entries[i][j].get()
            if not is_valid(value):
                P_np_global = 0
                messagebox.showinfo("错误", "出现了非法输入请关闭此窗口继续")
                return
            if not value:
                row.append(0)
            else:
                row.append(value)
        P.append(row)
    
    P_np = np.array(P)
    P_np_global = P_np  # 将 P_np 赋值给全局变量
    messagebox.showinfo("成功", "矩阵已成功输入，请关闭此窗口继续")

def matrix_input(rows=3, cols=3):
    root = tk.Tk()
    root.title("矩阵输入")
    root.option_add('*Font', '宋体 12')  # 设置字体

    create_ui(root, rows, cols)
    root.mainloop()
    
    #print("获取的矩阵 P_np 为：")
    #print(P_np_global)
    return P_np_global


if __name__ == "__main__":
    matrix_input(4,4)