import pyodbc 

drivers = pyodbc.drivers()

print('Installed ODBC Drivers:')

for driver in drivers:
    print(driver)
