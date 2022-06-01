import pandas as pd

def read_hired_employees_filter():
    df_hiredate = pd.read_csv("departments.csv", names=['Id', 'Names', 'Hiredate', 'a', 'b'], index_col='Id')

    df_hiredate = df_hiredate.fillna({'a': 0, 'b': 1})

    print(df_hiredate)

def read_departments_filter():
    df_departments = pd.read_csv("departments.csv", names=['Id', 'Departments'], index_col='Id')

def read_jobs_filter():
    df_jobs = pd.read_csv("jobs.csv", names=['Id', 'Jobs'], index_col='Id')

if __name__ == '__main__':
    pass