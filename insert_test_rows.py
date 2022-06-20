import psycopg2
from config_db import config
import datetime


def dummy_table():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create table if not exists
        print('Create dummy table employee')
        with conn:
            with conn.cursor() as cur:
                cur.execute("""
                CREATE TABLE IF NOT EXISTS employee (
                    employee_id  serial PRIMARY KEY,
                    first_name VARCHAR (50) NOT NULL,
                    last_name VARCHAR (50) NOT NULL,
                    email VARCHAR (255) UNIQUE NOT NULL,
                    created_on TIMESTAMP NOT NULL
                );
                """)

        # insert dummy data to table
        print('Insert sample data to table employee')
        with conn:
            with conn.cursor() as cur:
                insert_sql = f"""
                INSERT INTO employee(employee_id, first_name, last_name, email, created_on) VALUES
                (1, 'Carlos', 'Razo', 'carlos.razo@data.com', '{datetime.datetime.now()}'), 
                (2, 'Omar', 'Aguayo', 'omar.aguayo@data.com', '{datetime.datetime.now()}'), 
                (3, 'Jonathan', 'Ponce', 'jonathan.ponce@data.com', '{datetime.datetime.now()}');
                """
                cur.execute(insert_sql)

        # query dummy table
        print('Query sample data from dummy table employee')
        with conn:
            with conn.cursor() as cur:
                query_sql = 'SELECT * FROM employee;'
                cur.execute(query_sql)
                for row in cur.fetchall():
                    print(row)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    dummy_table()
