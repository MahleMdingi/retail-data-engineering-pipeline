
import pandas as pd
import pyodbc

#1. Extract the cleaned data
valid_records = pd.read_csv('data/processed/valid_records.csv')

print(f"Records ready to load: {len(valid_records)}")

# 2. Connect to SQL Server
connection_string = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=RetailDB;"
    "Trusted_Connection=yes;"
    "Encrypt=yes;"
    "TrustServerCertificate=yes;"
)

connection = pyodbc.connect(connection_string)
cursor = connection.cursor()

# 3. Prepare the SQL INSERT statement
insert_query = """
    INSERT INTO dbo.RetailSales_Staging
    (
        OrderID,
        CustomerName,
        Product,
        Category,
        Quantity,
        UnitPrice,
        OrderDate
    )
    VALUES (?, ?, ?, ?, ?, ?, ?)
"""

# 4. Insert the records
for _, row in valid_records.iterrows():

    cursor.execute(
        insert_query,
        int(row["OrderID"]),
        row["CustomerName"],
        row["Product"],
        row["Category"],
        int(row["Quantity"]),
        float(row["UnitPrice"]),
        row["OrderDate"]
    )

# 5. Commit the transaction
connection.commit()

print("Data successfully loaded into SQL Server!")

# 6. Close the connection
cursor.close()
connection.close()
