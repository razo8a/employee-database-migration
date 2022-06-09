import csv


def read_departaments():
    with open('raw_data/departments.csv', newline='') as f:
        reader_dep = csv.reader(f)
        for row in reader_dep:
            print(row)

def read_hired_employees():
    with open('raw_data/hired_employees.csv', newline='') as f:
        reader_dep = csv.reader(f)
        for row in reader_dep:
            print(row)

def read_jobs():
    with open('raw_data/jobs.csv', newline='') as f:
        reader_dep = csv.reader(f)
        for row in reader_dep:
            print(row)

def load_csv_to_postgres():
    pass


if __name__ == '__main__':
    read_departaments()
    read_jobs()
    read_hired_employees()



