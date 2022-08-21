import sys
from parse import *
import mysql.connector
from mysql.connector import errorcode
import csv

mysql_con = None

def db_connect():
  try:
    conn = mysql.connector.connect(host = 'kurly-db.cxt53rg7mbem.ap-northeast-2.rds.amazonaws.com',port = 3306,database = 'kurlyDB',user = 'root',password = 'zjfflxnejans')
    print("Connection established")
  except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Something is wrong with the user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("Database does not exist")
    else:
      print(err)
  else:
    cursor = conn.cursor(prepared=True)
  return conn

def admCD_insert(filename,cursor):
    ### only use when admCD is empty ###
    f = open(filename,'r',encoding='utf-8')
    csvReader = csv.reader(f)
    count = 0
    for row in csvReader:
      if count==0:
        count=1;
      else:
        if row[3]=="":
          print("no secondary adrr")
        else:
          sql = "insert into admCD values (\"" + row[1] + "\",\"" + row[2] + "\",\"" + row[3] + "\")"
          cursor.execute(sql)

if __name__ == '__main__':
  conn = db_connect()
  cursor = conn.cursor(buffered=True)

  tst_sql = "select * from address where address_category = 38"
  cursor.execute(tst_sql)

  #admCD_insert("C:\\Users\\idp3060a\\asset\\admCD.csv",cursor)
  #conn.commit()

  res = cursor.fetchall()
  for addr in res:
    print(addr[2].split(' '))

