from flask import Flask , Request
from pymongo import MongoClient
app = Flask (__name__)

#setting some db documents ssssss

client = MongoClient('mongodb://localhost:27017/')
db = client['demo']
collection = db['data']


@app.route ('/add_data', methods = ["POST"])
def momgo():
    data = request.json
    collection.insert_one(data)
    return 'data added to the mongo db'



if __name__ == '__main__':
    app.run ()