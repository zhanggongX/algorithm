import pandas as pd


def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    return users[users["mail"].str.match(r"^[a-zA-Z][a-zA-Z0-9_.-]*\@leetcode\.com$")]


if __name__ == '__main__':
    data = [[1, 'Winston', 'winston@leetcode.com'], [2, 'Jonathan', 'jonathanisgreat'],
            [3, 'Annabelle', 'bella-@leetcode.com'], [4, 'Sally', 'sally.come@leetcode.com'],
            [5, 'Marwan', 'quarz#2020@leetcode.com'], [6, 'David', 'david69@gmail.com'],
            [7, 'Shapiro', '.shapo@leetcode.com']]
    Users = pd.DataFrame(data, columns=['user_id', 'name', 'mail']).astype(
        {'user_id': 'int64', 'name': 'object', 'mail': 'object'})

    res = valid_emails(Users)
    print(res)
