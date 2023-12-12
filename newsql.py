import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os,shutil
def dbs():
    db = os.listdir("D:/DSQL")
    for db_nm in db:
        print(db_nm)
def crt_dbs():
    if ((os.path.exists("D:/DSQL/"+qr[qr.find("database")+9:])==True)):
        return print("{0} database exists.".format(qr[qr.find("database")+9:]))
    else:
        os.mkdir("D:/DSQL/"+qr[qr.find("database")+9:]) #os.mkdir("parent directory"+ "new folder name.
                                                    #folder name coming from slicing the query
        return print("{0} database created.".format(qr[qr.find("database")+9:]))
def use_dbs(): 
    if ((os.path.exists("D:/DSQL/"+qr[qr.find("use")+4:])==True)):#os.path.exists checks wether file exist or not. 
        return print("Entered in {0} database.".format(qr[qr.find("use")+4:]))
    else:
        return print("{0} database doesn't exists.".format(qr[qr.find("use")+4:]))
def flush_dbs():
    if ((os.path.exists("D:/DSQL/"+qr[qr.find("database")+9:])==True)):
        shutil.rmtree("D:/DSQL/"+qr[qr.find("database")+9:], ignore_errors=True)
        return print("{0} database flushed.".format(qr[qr.find("database")+9:]))
    else:
        return print("{0} database doesn't exists.".format(qr[qr.find("database")+9:]))
def crt_table():
    tbl_nm =  qr[qr.find("table")+6:qr.find("(")]   #gives out table name.
    clm_nm=  (qr[qr.index("[")+1:qr.index("]")]).split(",") #gives out column name
    #qr = qr.replace(qr[qr.index("["):qr.index("]")+1])    
    tbl = pd.DataFrame(columns= clm_nm)
    tbl.to_csv("D:/DSQL/"+tbl_nm+".csv",index = False)
    return print("Table " + tbl_nm+" created.")
def dt_tbl():
    






# use dictionaries  for storing fucntion and then use loop to check over its keys and use its value.





while True:
    qr = input(">>> ")
    if ("create database" in qr.lower()) :
        crt_dbs()
    elif ("use " in qr.lower()):
        use_dbs()
    elif ("flush" in qr.lower()):
        flush_dbs()
    elif ("create table" in qr.lower()) :
        crt_table()
    elif ("show databases" in qr.lower()):
        dbs()
    
    
    
