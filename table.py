import matplotlib.pyplot as plt
def draw(df):
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    #提取 'rank' 和 'rating' 列
    rank = df['rank']
    ratings = df['rating']

    # 创建图形
    plt.figure(figsize=(12, 8))

    # 绘制条形图
    plt.barh(rank, ratings, color='skyblue')

    # 添加标题和标签
    plt.title('豆瓣电影 Top 250 评分', fontsize=16)
    plt.xlabel('评分', fontsize=14)
    #plt.ylabel('电影标题', fontsize=14)

    # 反转 y 轴，使排名最高的电影在顶部
    plt.gca().invert_yaxis()

    # 显示图形
    plt.show()