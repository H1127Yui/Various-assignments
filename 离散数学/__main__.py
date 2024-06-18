from matrux_draw import draw0,draw1
from matrix_input import matrix_input
import numpy as np
import os
import sys




P0 = np.array([
        [0, 1, 0, 1],
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [1, 0, 1, 0]
    ])

P1 = np.array([
        [0, 1, 'e', 3],
        [1, 0, 2, 'e'],
        ['e', 2, 0, 4],
        [3, 'e', 4, 0]
    ])


os.system('cls')
print('欢迎使用邻接矩阵/距离矩阵画图程序\n\n暂不支持有向图的显示\n\n\n\n')
while True:
    user_choice = input("请选择邻接矩阵(0)或者距离矩阵(1):")
    if user_choice == '0' or user_choice == '1':
        break


while True:
    user_choice1 = input("是否直接使用测试矩阵(无需输入)(Y/N):")
    if user_choice1 == 'Y' or user_choice == 'y' or user_choice == 'n' or user_choice == 'N' or user_choice == '0' or user_choice == '1':
        break

if user_choice1 == 'Y' or user_choice1 == 'y' or user_choice1 == '1':
    if user_choice == '0':
        print(P0)
        draw0(P0)
    else:
        print(P1)
        draw1(P1)
else:
    if user_choice == '1':
        print("主要请用'e'来指代∞")
    while True:
        deep = int(input("请输入矩阵深度:"))
        if deep > 0:
            break

    P = matrix_input(deep ,deep)
    if P is int:
        print("错误：无效的输入")
        exit()
    else:
        if user_choice == '0':
            draw0(P)
        else:
            draw1(P)