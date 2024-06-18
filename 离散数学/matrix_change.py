'''
import numpy as np

def reachability_to_adjacency(reachability_matrix):#可达矩阵转换邻接矩阵
    n = len(reachability_matrix)
    adjacency_matrix = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if reachability_matrix[i][j] == 1 and i != j:
                is_direct = True
                for k in range(n):
                    if k != i and k != j and reachability_matrix[i][k] == 1 and reachability_matrix[k][j] == 1:
                        is_direct = False
                        break
                if is_direct:
                    adjacency_matrix[i][j] = 1
    
    return adjacency_matrix



def distance_to_adjacency(distance_matrix):#距离矩阵转换为邻接矩阵
    # 获取矩阵的维度
    n = distance_matrix.shape[0]
    
    # 初始化邻接矩阵
    adjacency_matrix = np.zeros((n, n), dtype=int)
    
    # 遍历距离矩阵，将非零元素转换为1
    for i in range(n):
        for j in range(n):
            if distance_matrix[i][j] != 0:
                adjacency_matrix[i][j] = 1
    
    return adjacency_matrix

# 示例距离矩阵
P2 = np.array([
    [0, 2, 0, 4],
    [2, 0, 3, 0],
    [0, 3, 0, 1],
    [4, 0, 1, 0]
])


# 示例可达矩阵
P1 = np.array([
    [1, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 1, 1],
    [0, 0, 1, 1]
])

# 测试邻接矩阵
P = np.array([
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0]
])'''