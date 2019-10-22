## @package database
# 
# This module is used to interface the database. So any access to the database will happen here

import MySQLdb

db_user = "feeder"
db_pwd = "feeder"
db_name = "showcase_db"


## This function is used when updating the database so no output is expected
#
# @param query The query that will be run on the database
def updateDB(query):
    db = MySQLdb.connect(host="localhost", user=db_user, passwd=db_pwd, db=db_name)
    cur = db.cursor()
    try:
        cur.execute(query)
        db.commit()
        #print("Database updated. Query:%s" % query)
    except:
        db.rollback()
        print("Database update error occured. Rolling back db")
    db.close()



## This function is used to select only one row from the database
#
# @param query The query that will select the row
# @return The selected row
def selectOne(query):
    db = MySQLdb.connect(host="localhost", user=db_user, passwd=db_pwd, db=db_name)
    cur = db.cursor()
    try:
        cur.execute(query)
        data = cur.fetchone()
    except Exception as e:
        print("Unable to fetch data: " + str(e) )
        data = ""
    db.close()
    return data

## This function is used to select many rows from the database
#
# @param query The query that will select the database
# @return The selected rows
def selectMany(query):
    db = MySQLdb.connect(host="localhost", user=db_user, passwd=db_pwd, db=db_name)
    cur = db.cursor()
    try:
        cur.execute(query)
        data = cur.fetchall()
    except Exception as e:
        print("Unable to fetch data: " + str(e) )
        data = ""
    db.close()
    return data


