def average_rating(df):
    return df['rating'].mean()


def top_rated_movies(df):
    top_rated_movies = df[df['rating'] == df['rating'].max()]
    
    return top_rated_movies