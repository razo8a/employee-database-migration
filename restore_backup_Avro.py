import pandas as pd
from fastavro import reader, parse_schema


def main():
    # 1. List to store records
    avro_records = []

    # 2. Read the Avro file
    with open('backup.avro', 'rb') as fo:
        avro_reader = reader(fo)
        for record in avro_reader:
            avro_records.append(record)

    # 3. Convert to pd.DataFrame
    df_avro = pd.DataFrame(avro_records)

    # Print the first couple of rows
    print(df_avro.head)


if __name__ == '__main__':
    main()