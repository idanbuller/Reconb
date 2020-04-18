import mysql.connector


mysql_user = str(input(">> Please paste here your MySQL user name: "))
mysql_password = str(input(">> Please paste here your MySQL password: "))

try:
    mydb = mysql.connector.connect(
      host="localhost",
      user=f"{mysql_user}",
      passwd=f"{mysql_password}"
    )
    mycursor = mydb.cursor()
    mycursor.execute("create database IF NOT EXISTS reconb")
    print(">> reconb Scheme created <<")
except mysql.connector.Error as e:
    print(f"MySQL Error: {e}")

finally:
    pass


print("""
[*] Please fill the empty values on keys.py [*]
""")
