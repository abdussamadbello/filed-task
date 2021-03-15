import json
from bson.errors import BSONError
from bson.objectid import ObjectId
from bson import json_util
from pymongo.collection import ReturnDocument
from pymongo.errors import PyMongoError
from database import db

def getAll(audio_type):
    try:
        result = db[audio_type].find()
        result=json.dumps(list(result),default=json_util.default)
        return result
    except PyMongoError as e:
        raise (e)

def getById(audio_type, id):
        try:
            result = db[audio_type].find({"_id": ObjectId(id)})
            result=json.dumps(list(result),default=json_util.default)
            return result
        except (PyMongoError,BSONError) as e:
            raise (e)

def create_file(audio_type, audio_file):
    data=dict(audio_file)
    try:
        coll_names=db.list_collection_names()
        if audio_type not in coll_names:
            result = db.create_collection(audio_type).insert_one(data)
            return str(result.inserted_id)
        else:
            result=db[audio_type].insert_one(data)
            return str(result.inserted_id)
    except Exception as e:
        raise (e)

def update_file(audio_type, audio_file, id):
    data=dict(audio_file)
    try:
       result= db[audio_type].find_one_and_update(
            {"_id": ObjectId(id)},
            {"$set": data},
            return_document=ReturnDocument.AFTER,
            )
       result= json.dumps(result,default=json_util.default)
       return result

    except (PyMongoError,BSONError) as e:
        raise (e)

def deleteById(audio_type, id):
    try:
      result = db[audio_type].find_one_and_delete(
            {"_id": ObjectId(id)}
        )
      result= json.dumps(result,default=json_util.default)
      return result
    except (PyMongoError,BSONError) as e:
        raise (e)
