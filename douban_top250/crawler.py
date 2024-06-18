import requests
from bs4 import BeautifulSoup


# 定义一个函数来抓取数据
def fetch_movie_data():
    movies = []
    for i in range(10):
        url = f"https://movie.douban.com/top250?start={25*i}&filter="
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        for item in soup.find_all('div', class_='item'):
            rank = item.find('em').text
            title = item.find('span', class_='title').text
            rating = item.find('span', class_='rating_num').text
            quote = item.find('span', class_='inq').text if item.find('span', class_='inq') else ''
            movies.append({'rank': rank, 'title': title, 'rating': rating, 'quote': quote})
    
    return movies