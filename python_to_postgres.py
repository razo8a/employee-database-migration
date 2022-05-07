# Conection python to postgres
import psycopg2


hostname = 'localhost'
database = 'demo'
username = 'postgres'
pwd = 'admin'
port_id = 5432

conn = psycopg2.connect(
            host=hostname,
            dbname=database,
            user=username,
            password=pwd,
            port=port_id)
conn.close()

