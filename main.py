import pymongo
# need to procide mongodb localhost
client=pymongo.MongoClient("mongodb://localhost:27017")
#this code will make database in mongodb
# database name
dataBase=client['Sagar']

#collection Name
collection=dataBase['Ml_dep']

#sampledata
d={'companyname':'Sagar_Ai',
   'product':'AI',
   'course':'ML_deployment'}

# insert above rows
rec=collection.insert_one(d)

#lets veryfy all records present indatabase
all_record=collection.find()

# print all record
for idx, record in enumerate(all_record):
    print(f"{idx}: {record}")