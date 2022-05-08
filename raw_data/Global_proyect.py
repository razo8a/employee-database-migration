import csv


def read_departaments():
    with open('departments.csv', newline='') as f:
        reader_dep = csv.reader(f)
        for row in reader_dep:
            print(row)

def read_hired_employees():
    with open('hired_employees.csv', newline='') as f:
        reader_dep = csv.reader(f)
        for row in reader_dep:
            print(row)

def read_jobs():
    with open('jobs.csv', newline='') as f:
        reader_dep = csv.reader(f)
        for row in reader_dep:
            print(row)

def load_csv_to_postgres():
    pass


if __name__ == '__main__':
    read_hired_employees()
    #read_departaments()
    #read_jobs()



