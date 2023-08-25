import pandas as pd


def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(department, left_on='departmentId', right_on='id', how='left')
    df.rename(columns={'name_x': 'Employee', 'name_y': 'Department', 'salary': 'Salary'}, inplace=True)
    max_salary = df.groupby('Department')['Salary'].transform('max')
    # print(max_salary)
    df = df[df['Salary'] == max_salary]

    # print(df)

    return df[['Department', 'Employee', 'Salary']]
    # return df


if __name__ == '__main__':
    data = [[1, 'Joe', 70000, 1],
            [2, 'Jim', 90000, 1],
            [3, 'Henry', 80000, 2],
            [4, 'Sam', 60000, 2],
            [5, 'Max', 90000, 1]]
    Employee = pd.DataFrame(data, columns=['id', 'name', 'salary', 'departmentId']).astype(
        {'id': 'Int64', 'name': 'object', 'salary': 'Int64', 'departmentId': 'Int64'})

    data = [[1, 'IT'],
            [2, 'Sales']]
    Department = pd.DataFrame(data, columns=['id', 'name']).astype({'id': 'Int64', 'name': 'object'})
    res = department_highest_salary(Employee, Department)
    print(res)
