import pandas as pd


# select p.product_name, year, price from sales s left join product p on s.product_id = p.product_id;
def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    df = sales.merge(product, on='product_id')
    df = df[['product_name', 'year', 'price']]
    return df


if __name__ == '__main__':
    data = [[1, 100, 2008, 10, 5000], [2, 100, 2009, 12, 5000], [7, 200, 2011, 15, 9000]]
    sales = pd.DataFrame(data, columns=['sale_id', 'product_id', 'year', 'quantity', 'price']).astype(
        {'sale_id': 'Int64', 'product_id': 'Int64', 'year': 'Int64', 'quantity': 'Int64', 'price': 'Int64'})
    data = [[100, 'Nokia'], [200, 'Apple'], [300, 'Samsung']]
    product = pd.DataFrame(data, columns=['product_id', 'product_name']).astype(
        {'product_id': 'Int64', 'product_name': 'object'})

    res = sales_analysis(sales, product)
    print(res)
