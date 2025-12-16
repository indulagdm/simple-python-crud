from db import collection


#Create
def createUser(name,password):
    collection.insert_one({
        "name":name,
        "password":password
    })


#Get all
def getUserAll():
    return list(collection.find())


