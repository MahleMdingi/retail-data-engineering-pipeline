
import pandas as pd

#Extract data from csv file

file_path= "data/raw/retail_sales_dirty.csv"

sales_data = pd.read_csv(file_path)

#Display the first 5 records
print(sales_data.head())

print("\nDataset inforamtion:")
print(sales_data.info())

print("\nDataset dimensions:")
print(sales_data.shape)

print("\nColumn names:")
print(sales_data.columns.tolist())

print("\nMissing values:")
print(sales_data.isnull().sum())

print("\nDuplicate Records:")
print(sales_data.duplicated().sum())

#Remove duplicate records
sales_data = sales_data.drop_duplicates()

print("\nRecords after removing duplicates:")
print(sales_data.shape)

print("\nRows containing missing values:")
print(sales_data[sales_data.isnull().any(axis=1)])

#Count missing values
missing_values  = sales_data.isnull().sum()

print('\nMissing values per column:')
print(missing_values)

print('\nDataTypes:')
print(sales_data.dtypes)

sales_data['UnitPrice'] = pd.to_numeric(
    sales_data['UnitPrice'],
    errors = 'coerce'
)

sales_data['OrderDate'] = pd.to_datetime(
    sales_data["OrderDate"],
    errors='coerce'
)

print('\nUpdated DataType:')
print(sales_data.dtypes)

print('\nMissing Values after conversion:')
print(sales_data.isnull().sum())

#Identify records with invalid prices
invalid_prices = sales_data[sales_data['UnitPrice'].isnull()]

print('\nRecords with invalid prices:')
print(invalid_prices)


#Identify records with invalid prices
valid_prices = sales_data[sales_data['UnitPrice'].notnull()]

print('\nRecords with valid prices:')
print(valid_prices)

#Identify invalid quantites 
invalid_quantites = sales_data[sales_data['Quantity'] <= 0]

print('\nRecords with invalid quantites:')
print(invalid_quantites)


#Identify invalid prices 
invalid_prices = sales_data[sales_data['UnitPrice'] <= 0]

print('\nRecords with invalid prices:')
print(invalid_prices)


# Identify records that fail validation

invalid_records = sales_data[
    (sales_data["Quantity"].isnull()) |
    (sales_data["Quantity"] <= 0) |
    (sales_data["UnitPrice"].isnull()) |
    (sales_data["UnitPrice"] <= 0) |
    (sales_data["CustomerName"].isnull())
]

print("\nQuarantined records:")
print(invalid_records)

# Validation rules

# Rule 1: Quantity must be greater than zero
invalid_quantity = sales_data[
    sales_data["Quantity"].isnull() |
    (sales_data["Quantity"] <= 0)
]

# Rule 2: Unit price must be greater than zero
invalid_price = sales_data[
    sales_data["UnitPrice"].isnull() |
    (sales_data["UnitPrice"] <= 0)
]

# Rule 3: Customer name must not be missing
invalid_customer = sales_data[
    sales_data["CustomerName"].isnull()
]

# Display validation results

print("\nInvalid Quantities:")
print(invalid_quantity)

print("\nInvalid Prices:")
print(invalid_price)

print("\nInvalid Customers:")
print(invalid_customer)

sales_data["Missing_Quantity"] = sales_data["Quantity"].isnull()

sales_data["Invalid_Quantity"] = (
    sales_data["Quantity"].notnull() &
    (sales_data["Quantity"] <= 0)
)

sales_data["Missing_Price"] = sales_data["UnitPrice"].isnull()

sales_data["Invalid_Price"] = (
    sales_data["UnitPrice"].notnull() &
    (sales_data["UnitPrice"] <= 0)
)

sales_data["Missing_Customer"] = sales_data["CustomerName"].isnull()

validation_columns = [
    "Missing_Quantity",
    "Invalid_Quantity",
    "Missing_Price",
    "Invalid_Price",
    "Missing_Customer"
]

sales_data["Has_Validation_Error"] = sales_data[
    validation_columns
].any(axis=1)

print("\nData Quality Report:")

print(
    sales_data[
        ["OrderID"] + validation_columns + ["Has_Validation_Error"]
    ].to_string(index=False)
)


valid_records = sales_data[
    ~sales_data["Has_Validation_Error"]
].copy()

print("\nValid Records:")
print(valid_records)

quarantined_records = sales_data[
    sales_data["Has_Validation_Error"]
].copy()

print("\nQuarantined Records:")
print(quarantined_records)

quality_summary = pd.DataFrame({
    "Validation_Rule": validation_columns,
    "Failed_Records": [
        sales_data[column].sum()
        for column in validation_columns
    ]
})

print("\nData Quality Summary:")
print(quality_summary)

# Save processed datasets

valid_records.to_csv(
    "data/processed/valid_records.csv",
    index=False
)

quarantined_records.to_csv(
    "data/processed/quarantined_records.csv",
    index=False
)

quality_summary.to_csv(
    "data/processed/data_quality_report.csv",
    index=False
)

print("\nData cleaning completed successfully!")
