###############################-----------------Main Code-------------------#########################
# import pyodbc
# import json
# from datetime import datetime
# from urllib.parse import quote_plus
# from pymongo import MongoClient


# # This function is used to get table name only from the source database SSMS. 
# def table_name():
#     server = "LAPTOP-OL5QT5EE\MSSQLSERVER_SC"
#     database = "AdventureWorks2019"
#     username = "sa"
#     password = "Jushank@2021"

#     connection = pyodbc.connect(
#                 'DRIVER={ODBC Driver 17 for SQL Server};'
#                 'SERVER=' + server + ';'
#                 'DATABASE=' + database + ';'
#                 'UID=' + username + ';'
#                 'PWD=' + password
# )

#     cursor = connection.cursor()
#     cursor.execute("SELECT TABLE_SCHEMA + '.' + TABLE_NAME AS TableName FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE' ORDER BY TABLE_NAME ASC")
#     results = cursor.fetchall()
#     #Fetch all tables from the database
#     table_names = [row[0] for row in results]
#     print("This is the Numbers of Rows in the Table :", len(table_names))
#     #Get all tables from data source in json format
#     json_tables = json.dumps(table_names, indent=4)
#     print("This is the Numbers of Rows in the Table in json Formate :", json_tables)
#     return table_names


# # This function is used to get data from the source database SSMS and get the table name from the function "table_name()".
# def get_data_from_source(table_name):
#     try:
#         server = "LAPTOP-OL5QT5EE\MSSQLSERVER_SC"
#         database = "AdventureWorks2019"
#         username = "sa"
#         password = "Jushank@2021"

#         connection = pyodbc.connect(
#                     'DRIVER={ODBC Driver 17 for SQL Server};'
#                     'SERVER=' + server + ';'
#                     'DATABASE=' + database + ';'
#                     'UID=' + username + ';'
#                     'PWD=' + password
# )
#         cursor = connection.cursor()
#         print("Connection established successfully")

#         query = f"SELECT * FROM {table_name}"
#         cursor.execute(query)
#         columns = [column[0] for column in cursor.description] 
#         results = cursor.fetchall()
#         print("This is the Numbers of Rows in the Table :",len(results))

#         # Structuring results into a list of dictionaries
#         result_list = []
#         for row in results:
#             row_dict = {columns[i]: row[i] for i in range(len(columns))}
#             result_list.append(row_dict)

#         # Converting result to JSON
#         json_result = json.dumps(result_list, default=str, indent=4)
#         print(f"Data from {table_name}: {json_result}")

#         return result_list  # Returning the result as a list of dictionaries for MongoDB insertion

#     except Exception as e:
#         print(f"Error while processing table {table_name}: {e}")
#         return None


# def migrate_to_mongodb():
#     try:
#         username = quote_plus('shashank')
#         password = quote_plus('123@abc')
#         uri = f'mongodb+srv://{username}:{password}@advwork.mmbzc.mongodb.net/?retryWrites=true&w=majority&appName=AdvWork'
#         client = MongoClient(uri)
#         print("Connected successfully")
#         db = client["AdventureWorks"]  # Using AdventureWorks database
#     except Exception as e:
#         print("Error connecting to MongoDB:", e)
#         return None

#     # List to track tables that failed migration
#     failed_tables = []

#     # Get the list of tables from SQL Server
#     tables = table_name()

#     # Loop through all tables and migrate them to MongoDB
#     for table in tables:
#         print(f"Processing table: {table}")
#         data = get_data_from_source(table)

#         if data is not None:
#             # Insert data into MongoDB collection with the same name as the table
#             try:
#                 collection = db[table]  # Create or get collection in MongoDB
#                 collection.insert_many(data)  # Insert the data into MongoDB
#                 print(f"Data from {table} migrated successfully.")
#             except Exception as e:
#                 print(f"Error inserting data from {table} into MongoDB: {e}")
#                 failed_tables.append(table)  # Track the table name if migration fails
#         else:
#             failed_tables.append(table)  # Track the table name if getting data fails

#     # Print failed tables
#     if failed_tables:
#         print("\nTables that failed during migration:")
#         for failed_table in failed_tables:
#             print(failed_table)
#     else:
#         print("\nAll tables migrated successfully!")


# # Call the migration function
# if __name__ == "__main__":
#     migrate_to_mongodb()


