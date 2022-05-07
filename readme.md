# Employee database migration 

This project is big data migration to a new database system. 
The code will read CSV files and send then to a postgres database.
We will also use REST APIs to insert new batches of data.
A cron job will automatically backout tge database in AVRO files.
Backout files will be stored in a Google Drive for security reasons.
Finally, there will be an API to restore AVRO backout files back to 
the postgres database.

## Techologies Used 

- Python 
- Postgres 
- Rest API 
- Cron job 


