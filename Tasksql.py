#import pymongo
import logging
import mysql.connector as conn

from flask import Flask,request

app1 = Flask(__name__)


#logging.basicConfig(filename='task_20_08_22.log', level=logging.DEBUG, format='%(levelname)s %(asctime)s %(name)s %(message)s')

# 1 . Write a program to insert a record in sql table and fetch the records via api
@app1.route('/insertRecord',methods=['GET','POST'])
def insert_rec():
    logging.basicConfig(filename='task_insert.log', level=logging.INFO,
                        format='%(levelname)s %(asctime)s %(name)s %(message)s')

    ''' this function will insert the record into sql database'''
    # connecting to sql server
    mydb = conn.connect(host='localhost', user='root', passwd='Class123')
    cursor = mydb.cursor()
    try:

        if(request.method == 'POST'):
            cmd = request.json['command']
            cmd1=request.json['to_view_table']
            logging.info("Records in table before insert command")
            cursor.execute(cmd1)
            logging.info(cursor.fetchall())
            cursor.execute(cmd)
            mydb.commit()
            logging.info("Records in table after insert command")
            cursor.execute(cmd1)
            records=cursor.fetchall()
            logging.info(records)
            return records
    except Exception as e:
        logging.error(e)
        logging.exception(e)
        print(e)
    finally:
        mydb.close()


#2.  Write a program to update a record and fetch the records via api
@app1.route('/updateRecord',methods=['GET','POST'])
def update_rec():
    logging.basicConfig(filename='task_update.log', level=logging.INFO,
                        format='%(levelname)s %(asctime)s %(name)s %(message)s')

    ''' this function will update the record into sql database'''
    # connecting to sql server
    mydb = conn.connect(host='localhost', user='root', passwd='Class123')
    cursor = mydb.cursor()
    try:
        if(request.method == 'POST'):
            cmd = request.json['command']
            cmd1=request.json['to_view_table']
            logging.info("Records in table before update command")
            cursor.execute(cmd1)
            logging.info(cursor.fetchall())
            cursor.execute(cmd)
            mydb.commit()
            logging.info("Records in table after update command")
            cursor.execute(cmd1)
            records=cursor.fetchall()
            logging.info(records)

            return records
    except Exception as e:
        logging.error(e)
        logging.exception(e)
        print(e)
    finally:
        mydb.close()

#3 . Write a program to delete a record and fetch the records via api
@app1.route('/deleteRecord',methods=['GET','POST'])
def delete_rec():
    logging.basicConfig(filename='task_delete.log', level=logging.INFO,
                        format='%(levelname)s %(asctime)s %(name)s %(message)s')

    ''' this function will delete the record into sql database'''
    # connecting to sql server
    mydb = conn.connect(host='localhost', user='root', passwd='Class123')
    cursor = mydb.cursor()
    try:
        if(request.method == 'POST'):
            cmd = request.json['command']
            cmd1=request.json['to_view_table']
            logging.info("Records in table before delete command")
            cursor.execute(cmd1)
            logging.info(cursor.fetchall())
            cursor.execute(cmd)
            mydb.commit()
            logging.info("Records in table after delete command")
            cursor.execute(cmd1)
            records=cursor.fetchall()
            logging.info(records)

            return records
    except Exception as e:
        logging.error(e)
        logging.exception(e)
        print(e)
    finally:
        mydb.close()




if __name__=='__main__':
    app1.run()


#5 . All the above questions you have to answer for mongo db as well .

