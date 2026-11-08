import pyodbc 

#Database connection config
connection_string = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=RetailDB;"
    "Trusted_Connection=yes;"
    "Encrypt=yes;"
    "TrustServerCertificate=yes;"
)

try:
    #Establish DB Connection
    connection = pyodbc.connect(connection_string)

    print('Successfully connected to SQL Server')

    #Create a cursor
    cursor = connection.cursor()

    # Execute SQL query
    cursor.execute("""
            SELECT
            @@SERVERNAME AS ServerName,
            DB_NAME() AS DatabaseName
    """)

    #Retrieve query result
    result = cursor.fetchone()

    print(f'Server:{result.ServerName}')
    print(f'Database: {result.DatabaseName}')

except pyodbc.Error as error:
    print('Database connection failed:')
    print(error)

finally:
    if 'connection' in locals():
        connection.close()
        print('Database connection closed.')
