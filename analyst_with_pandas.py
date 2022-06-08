import pandas as pd

def read_hired_employees_filter():
    df_hiredate = pd.read_csv("hird_employees.csv", names=['Id', 'Names', 'Hiredate', 'a', 'b'], index_col='Id')

    df_hiredate = df_hiredate.fillna({'a': 0, 'b': 0})

    return df_hiredate

def read_departments_filter():
    df_departments = pd.read_csv("departments.csv", names=['Id', 'Departments'], index_col='Id')

    return df_departments

def read_jobs_filter():
    df_jobs = pd.read_csv("jobs.csv", names=['Id', 'Jobs'], index_col='Id')

    return read_jobs_filter()


if __name__ == '__main__':
    read_hired_employees_filter()
    read_departments_filter()
    read_jobs_filter()
