# This module is used to load the data in the MySQL Database
import csv
import mysql.connector as con
import streamlit as st

my_sql_config = st.secrests["mysql"]

def InsertTrainData():
    mn = con.connect(host = my_sql_config["host"],
                user = my_sql_config["user"],
                database = my_sql_config["database"],
                password = my_sql_config["password"])

    cur = mn.cursor()
    # This is used to iterate through all the data in the csv file and inser them in the database
    try:
        with open(r"C:\Users\Naman\OneDrive\Desktop\Railway management\Assets\Train_details.csv") as csv_data:
            csv_reader = csv.reader(csv_data, delimiter=",")
            for row in csv_reader:
                cur.execute(
                    'INSERT INTO train_info VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', row)
    except FileNotFoundError:
        print("Please check whether the file is in the Assets Folder or not and try changing the Location in InsertData.py")
    finally:
        mn.commit()  # after doing anything in the database we need to commit it to save the changes made to the database
        cur.close()
        mn.close()