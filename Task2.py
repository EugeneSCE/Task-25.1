import mysql.connector


def dbConection():
  return mysql.connector.connect(
    host="localhost",
    user="temp_user",
    password="Q!password"
  )

def createSchema(mycursor):
  mycursor.execute("DROP DATABASE IF EXISTS task2_db")
  mycursor.execute("CREATE DATABASE task2_db")

  mycursor.execute("USE task2_db")
  mycursor.execute(
    "CREATE TABLE DEPARTMENT (ID INT NOT NULL AUTO_INCREMENT, NAME VARCHAR(255), LOCATION VARCHAR(255), PRIMARY KEY (ID))")
  mycursor.execute(
    "CREATE TABLE EMPLOYEE (ID INT NOT NULL AUTO_INCREMENT, NAME VARCHAR(255), SALARY INT, DEPT_ID INT, PRIMARY KEY (ID), FOREIGN KEY (DEPT_ID) REFERENCES DEPARTMENT(ID) ON DELETE CASCADE )")


def closeAndDeleteDB(mydb, mycursor):
  mycursor.execute("DROP DATABASE task2_db")
  mydb.close()

def insertData(mydb,mycursor ,table_name,data_arr):
  if table_name == "DEPARTMENT":
    sql = "INSERT INTO " + table_name + " (NAME, LOCATION) VALUES (%s, %s)"
    for data in data_arr:
      mycursor.execute(sql, data)
    mydb.commit()

  elif table_name == "EMPLOYEE":
    sql = "INSERT INTO " + table_name + " (NAME, SALARY, DEPT_ID) VALUES (%s, %s, %s)"
    for data in data_arr:
      mycursor.execute(sql, data)
    mydb.commit()
  return


def createData(mydb, mycursor):
  department_data = (
    ["Executive", "Sydney"],
    ["Production", "Sydney"],
    ["Resources", "Cape Town"],
    ["Technical", "Texas"],
    ["Management", "Paris"],
  )

  employee_data = (
    ["Candice", 4685, 1],
    ["Julia", 2559, 2],
    ["Bob", 4405, 4],
    ["Scarlet", 2350, 1],
    ["Ileana", 1151, 4]
  )
  createSchema(mycursor)
  insertData(mydb, mycursor, "DEPARTMENT", department_data)
  insertData(mydb, mycursor, "EMPLOYEE", employee_data)


def query(mydb,mycursor):

  mycursor.execute("USE task2_db")
  query = "SELECT D.NAME, COUNT(E.ID) FROM DEPARTMENT D  LEFT JOIN Employee E ON D.ID = E.DEPT_ID GROUP BY D.ID ORDER BY COUNT(E.ID) DESC, D.NAME"
  mycursor.execute(query)
  return mycursor.fetchall()


if __name__ == '__main__':
  mydb = dbConection()
  mycursor = mydb.cursor()
  createData(mydb, mycursor)
  print(query(mydb, mycursor))
  closeAndDeleteDB(mydb, mycursor)