'''
select u.user_id as buyer_id, u.join_date, count(o.order_id) as orders_in_2019
from Users u
left join (select * from Orders where order_date <= '2019-12-31' and order_date >= '2019-01-01') o
on u.user_id = o.buyer_id
group by u.user_id;
'''

import pandas as pd


def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    orders = orders[(orders['order_date'] <= '2019-12-31') & (orders['order_date'] >= '2019-01-01')]
    df = users.merge(orders, how='left', left_on='user_id', right_on='buyer_id')
    df = df.groupby(['user_id', 'join_date']).agg(orders_in_2019=('order_id', 'count')).rename_axis(['buyer_id', 'join_date'])
    return df.reset_index()


if __name__ == '__main__':
    data = [[1, '2018-01-01', 'Lenovo'], [2, '2018-02-09', 'Samsung'], [3, '2018-01-19', 'LG'], [4, '2018-05-21', 'HP']]
    users = pd.DataFrame(data, columns=['user_id', 'join_date', 'favorite_brand']).astype(
        {'user_id': 'Int64', 'join_date': 'datetime64[ns]', 'favorite_brand': 'object'})
    data = [[1, '2019-08-01', 4, 1, 2], [2, '2018-08-02', 2, 1, 3], [3, '2019-08-03', 3, 2, 3],
            [4, '2018-08-04', 1, 4, 2], [5, '2018-08-04', 1, 3, 4], [6, '2019-08-05', 2, 2, 4]]
    orders = pd.DataFrame(data, columns=['order_id', 'order_date', 'item_id', 'buyer_id', 'seller_id']).astype(
        {'order_id': 'Int64', 'order_date': 'datetime64[ns]', 'item_id': 'Int64', 'buyer_id': 'Int64',
         'seller_id': 'Int64'})
    data = [[1, 'Samsung'], [2, 'Lenovo'], [3, 'LG'], [4, 'HP']]
    items = pd.DataFrame(data, columns=['item_id', 'item_brand']).astype({'item_id': 'Int64', 'item_brand': 'object'})

    print(market_analysis(users, orders, items))
