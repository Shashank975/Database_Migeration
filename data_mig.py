import pyodbc
import json
from datetime import datetime
from urllib.parse import quote_plus
from pymongo import MongoClient



# This function is used to get table name only from the source database SSMS. 
def table_name():
    server = "LAPTOP-OL5QT5EE\MSSQLSERVER_SC"
    database = "AdventureWorks2019"
    username = "sa"
    password = "Jushank@2021"

    connection = pyodbc.connect(
                'DRIVER={ODBC Driver 17 for SQL Server};'
                'SERVER=' + server + ';'
                'DATABASE=' + database + ';'
                'UID=' + username + ';'
                'PWD=' + password
)

    cursor = connection.cursor()
    cursor.execute("SELECT TABLE_SCHEMA + '.' + TABLE_NAME AS TableName FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE' ORDER BY TABLE_NAME ASC")
    results = cursor.fetchall()
    #Fetch all tables from the database
    table_names = [row[0] for row in results]
    print("This is the Numbers of Rows in the Table :", len(table_names))
    #Get all tables from data source in json format
    json_tables = json.dumps(table_names, indent=4)
    print("This is the Numbers of Rows in the Table in json Formate :", json_tables)
    return table_names


# This function is used to get data from the source database SSMS and get the table name from the function "table_name()".
def get_data_from_source(table_name):
    try:
        server = "LAPTOP-OL5QT5EE\MSSQLSERVER_SC"
        database = "AdventureWorks2019"
        username = "sa"
        password = "Jushank@2021"

        connection = pyodbc.connect(
                    'DRIVER={ODBC Driver 17 for SQL Server};'
                    'SERVER=' + server + ';'
                    'DATABASE=' + database + ';'
                    'UID=' + username + ';'
                    'PWD=' + password
)
        cursor = connection.cursor()
        print("Connection established successfully")


        query = f"SELECT * FROM {table_name}"
        cursor.execute(query)
        columns = [column[0] for column in cursor.description] 
        results = cursor.fetchall()
        print("This is the Numbers of Rows in the Table :",len(results))


        # for row in results:
        #     print(row)
        # return (results)


        # Structuring results into a list of dictionaries
        result_list = []
        for row in results:
            row_dict = {columns[i]: row[i] for i in range(len(columns))}
            result_list.append(row_dict)

        # Converting result to JSON
        json_result = json.dumps(result_list, default=str, indent=4)
        print(f"Data from {table_name}: {json_result}")

        return json_result

    except Exception as e:
        print("Error while connecting to SQL Server", e)


def migerate_to_mongodb():
    try:
        username = quote_plus('shashank')
        password = quote_plus('123@abc')
        uri = f'mongodb+srv://{username}:{password}@advwork.mmbzc.mongodb.net/?retryWrites=true&w=majority&appName=AdvWork'
        client = MongoClient(uri)
        print("Connected successfully")
    except Exception as e:
        print("Error connecting to MongoDB:", e)
        return None


#Call the functions :
if __name__ == "__main__":

    tables = table_name()
    for table in tables:
        print(f"Table Name: {table}")
        data = get_data_from_source(table)
        print(f"Data from {table}: {data}")



