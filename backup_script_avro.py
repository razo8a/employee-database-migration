import pandas as pd
from sqlalchemy import create_engine
from fastavro import writer, reader, parse_schema


def main():
    # Create the SQL engine object
    alchemyEngine = create_engine('postgresql+psycopg2://carlos_razo:@localhost/mydatabase')

    # Connect to Postgres Database
    ps_conn = alchemyEngine.connect()

    # Query all rows in employee table
    sql_query = """
    SELECT * FROM employee;
    """
    df = pd.read_sql(sql_query, ps_conn)

    # Close the connection to database
    ps_conn.close()


if __name__ == '__main__':
    main()
