import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def into_char(num):#将数字序列号转换为大写字母
    return chr(num + 65)

def draw0(P):# 定义邻接矩阵
    

    # 创建一个空的图
    G = nx.Graph()

    # 添加顶点
    n = len(P)
    for i in range(n):
        G.add_node(into_char(i))

    # 添加边
    for i in range(n):
        for j in range(n):
            if int(P[i][j]) != 0:
                G.add_edge(into_char(i), into_char(j))

    # 绘制图
    pos = nx.spring_layout(G)  # 选择布局方式
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold')
    plt.show()

def draw1(adj_matrix = [
        [0, 1, 'e', 3],
        [1, 0, 2, 'e'],
        ['e', 2, 0, 4],
        [3, 'e', 4, 0]
    ]):# 示例距离矩阵
    

    # 创建一个空的图
    G = nx.Graph()

    # 添加顶点
    n = len(adj_matrix)
    for i in range(n):
        G.add_node(into_char(i))

    # 添加边
    for i in range(n):
        for j in range(i + 1, n):
            if adj_matrix[i][j] != 'e':
                G.add_edge(into_char(i), into_char(j), weight=adj_matrix[i][j])

    # 绘制图
    pos = nx.spring_layout(G)  # 选择布局方式
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold')
    plt.show()





if __name__ == "__main__":
    draw1(np.array([
        [0, 1, 'e', 3],
        [1, 0, 2, 'e'],
        ['e', 2, 0, 4],
        [3, 'e', 4, 0]
    ]))