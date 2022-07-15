import pandas as pd
from sqlalchemy import create_engine
from fastavro import writer, reader, parse_schema


def main():
    # Create the SQL engine object
    alchemyEngine = create_engine('postgresql+psycopg2://omaraguayo:IslaCartagena@localhost/employees')

    # Connect to Postgres Database
    ps_conn = alchemyEngine.connect()

    # Query all rows in employee table
    sql_query = """
    SELECT * FROM employee;
    """
    df = pd.read_sql(sql_query, ps_conn)

    # Close the connection to database
    ps_conn.close()

    schema = {
        'doc': 'Data_base1',
        'name': 'Employee',
        'namespace': 'in',
        'type': 'record',
        'fields': [
            {'name': 'employee_id', 'type': 'int'},
            {'name': 'first_name', 'type': 'string'},
            {'name': 'last_name', 'type': 'string'},
            {'name': 'email', 'type': 'string'},
            {'name': 'crated_on', 'type': ["null", "int"]}
        ]
    }
    _parse_schema = parse_schema(schema)

    # covert pd.DataFrame to records - list of dictionaries
    records = df.to_dict('records')

    # Write to Avro file
    with open('backup.avro', 'wb') as out:
        writer(out, _parse_schema, records)


if __name__ == '__main__':
    main()
