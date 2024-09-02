import pandas as pd


# select * from cinema where description != 'boring' and id % 2 = 1 order by rating desc;
def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    return cinema[(cinema['description']!='boring') & (cinema['id']%2==1)].sort_values('rating', ascending=False)

if __name__ == '__main__':
    data = [[1, 'War', 'great 3D', 8.9], [2, 'Science', 'fiction', 8.5], [3, 'irish', 'boring', 6.2],
            [4, 'Ice song', 'Fantacy', 8.6], [5, 'House card', 'Interesting', 9.1]]
    cinema = pd.DataFrame(data, columns=['id', 'movie', 'description', 'rating']).astype(
        {'id': 'Int64', 'movie': 'object', 'description': 'object', 'rating': 'Float64'})

    res = not_boring_movies(cinema)
    print(res)
