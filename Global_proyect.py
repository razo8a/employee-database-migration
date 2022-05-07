import csv

def read_departaments():
    with open('raw_data/departments.csv', newline='') as f:
        reader_dep = csv.reader(f, delimiter=' ', quotechar='|')
        for row in reader_dep:
            print(', '.join(row))
    print(reader_dep)

def read_hird_employees():
    pass

def read_jods():
    pass


if __name__ == '__main__':
    pass



