import pymongo
import logging

from flask import Flask,request, jsonify

app1 = Flask(__name__)

#5 . All the above questions you have to answer for mongo db as well .
# 5.1 . Write a program to insert a record in Mongodb table and fetch the records via api
@app1.route('/insertRecordMD',methods=['GET','POST'])
def insert_rec():
    logging.basicConfig(filename='taskMD_insert.log', level=logging.INFO,
                        format='%(levelname)s %(asctime)s %(name)s %(message)s')

    ''' this function will insert the record into Mongodb database'''
    # connecting to Mongodb server
    client = pymongo.MongoClient(
        "mongodb+srv://Poonam:Class123@cluster0.8t5cuou.mongodb.net/?retryWrites=true&w=majority")

    db = client.test
    try:

        if(request.method == 'POST'):
            database=client['Inventory']
            collection = database['Table1']
            d = request.json['data']
            logging.info("Records in table before insert command")
            records = jsonify(str(collection.find({})))
            logging.info(records)
            collection.insert_one(d)
            logging.info("Records in table after insert command")
            records = jsonify(str(collection.find({})))
            logging.info(records)
            return records
    except Exception as e:
        logging.error(e)
        logging.exception(e)
        print(e)



#5.2.  Write a program to update a record and fetch the records via api
@app1.route('/updateRecordMD',methods=['GET','POST'])
def update_rec():
    logging.basicConfig(filename='taskMD_update.log', level=logging.INFO,
                        format='%(levelname)s %(asctime)s %(name)s %(message)s')

    ''' this function will update the record into Mongodb database'''
    # connecting to Mongodb server
    client = pymongo.MongoClient(
        "mongodb+srv://Poonam:Class123@cluster0.8t5cuou.mongodb.net/?retryWrites=true&w=majority")

    db = client.test
    try:
        if(request.method == 'POST'):
            database = client['Inventory']
            collection = database['Table1']
            filters = request.json['filter']
            newvalues = request.json['newvalue']
            logging.info("Records in table before update command")
            records = jsonify(str(collection.find({})))
            logging.info(records)
            collection.update_one(filters, newvalues)
            logging.info("Records in table after update command")
            records = jsonify(str(collection.find({})))
            logging.info(records)
            return records
    except Exception as e:
        logging.error(e)
        logging.exception(e)
        print(e)


#5.3 . Write a program to delete a record and fetch the records via api
@app1.route('/deleteRecordMD',methods=['GET','POST'])
def delete_rec():
    logging.basicConfig(filename='taskMD_delete.log', level=logging.INFO,
                        format='%(levelname)s %(asctime)s %(name)s %(message)s')

    ''' this function will delete the record into Mongodb database'''
    # connecting to Mongodb server
    client = pymongo.MongoClient(
        "mongodb+srv://Poonam:Class123@cluster0.8t5cuou.mongodb.net/?retryWrites=true&w=majority")

    db = client.test
    try:
        if(request.method == 'POST'):
            database = client['Inventory']
            collection = database['Table1']
            data = request.json['data']
            logging.info("Records in table before update command")
            records = jsonify(str(collection.find({})))
            logging.info(records)
            collection.delete_one(data)
            logging.info("Records in table after update command")
            records = jsonify(str(collection.find({})))
            logging.info(records)
            return records

    except Exception as e:
        logging.error(e)
        logging.exception(e)
        print(e)

if __name__=='__main__':
    app1.run()




