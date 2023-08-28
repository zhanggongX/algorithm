import pandas as pd


def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    df = world[(world['area'] >= 3000000) | (world['population'] >= 25000000)]
    print(df[['name', 'population', 'area']])


if __name__ == '__main__':
    data = [["Afghanistan", 'Asia', 652230, 25500100, 20343000000],
            ["Albania", 'Europe', 28748, 2831741, 12960000000],
            ["Algeria", 'Africa', 2381741, 37100000, 188681000000],
            ["Andorra", 'Europe', 468, 78115, 3712000000],
            ["Angola", 'Africa', 1246700, 20609294, 100990000000]]
    world_pd = pd.DataFrame(data, columns=['name', 'continent', 'area', 'population', 'gdp'])
    print(world_pd)
    big_countries(world_pd)
