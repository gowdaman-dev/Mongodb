import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

#NOTE-AFTER INSERTING RECORDS DO BELOW

x = mycol.find_one()#To extract first record

print(x)

#to extract all records
for x in mycol.find():
  print(x)

#extract particular fields
for x in mycol.find():
  print(x)

#extract excluding address from table
for x in mycol.find({},{ "address": 0 }):
  print(x)

#> than s
  myquery = { "address": { "$gt": "S" } }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)

#sort
mydoc = mycol.find().sort("name")

for x in mydoc:
  print(x)

#sort descending
mydoc = mycol.find().sort("name", -1)

for x in mydoc:
  print(x)

#delete one
myquery = { "address": "Mountain 21" }

mycol.delete_one(myquery)

#delete many
myquery = { "address": {"$regex": "^S"} }

x = mycol.delete_many(myquery)

print(x.deleted_count, " documents deleted.")

#deleting all records
x = mycol.delete_many({})

print(x.deleted_count, " documents deleted.")

#delete table
mycol.drop()

#UPDATE ONE

myquery = { "address": "Valley 345" }
newvalues = { "$set": { "address": "Canyon 123" } }

mycol.update_one(myquery, newvalues)

#print "customers" after the update:
for x in mycol.find():
  print(x)

#UPDATE MANY
myquery = { "address": { "$regex": "^S" } }
newvalues = { "$set": { "name": "Minnie" } }

x = mycol.update_many(myquery, newvalues)

print(x.modified_count, "documents updated.")

#LIMIT

myresult = mycol.find().limit(5)

#print the result:
for x in myresult:
  print(x)

  
  

  






  

