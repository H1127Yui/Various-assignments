import crawler #爬虫
import table #可视化
import validation #检查目录下是否有文件
import analysis #数据分析
import pandas as pd




def update():
    movies_data = crawler.fetch_movie_data()
    df = pd.DataFrame(movies_data)
    df.to_csv('./data/douban_top250.csv', index=False)

if __name__ == '__main__':
    # 抓取数据并存储到本地
    if validation.check_files_in_directory('./data') == True:
        print("数据库已存在，是否更新(Y/N)")
        while True:
            flat=input()
            if flat =='Y' or 'y':
                update()
                break
            elif flat =='N' or 'n' :
                break
            else:
                print("请正确输入(Y/N)")
    else:
        print("数据库不存在，正在爬取中，请稍等……")
        update()

    df = pd.read_csv('./data/douban_top250.csv')#读取数据

   
    print("平均得分", analysis.average_rating(df))
    print(f"最高评分的电影:")
    print(analysis.top_rated_movies(df))


    table.draw(df)