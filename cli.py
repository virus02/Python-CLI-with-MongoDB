import argparse 
from pymongo import MongoClient 

try:
	conn = MongoClient()
	print "Database Connected Successfully :)"
except:
	print "Database Connection Failed !!"

db = conn.test
collection = db.mycollection

def insert(args):
	name = raw_input("Enter a name : ")
	age = int(raw_input("Enter an age : "))
	loc = raw_input("Enter a location : ")

	emp_det = {"name":name,"age":age,"loc":loc}
	rec_id1 = collection.insert_one(emp_det) 

	print "Record Inserted"

def show(args):
	cursor = collection.find()
	if cursor.count() == 0:
		print "There is no record !!"
	else:
		for record in cursor:
			print record

def remove(args):
	cursor = collection.find()
	n = raw_input("Enter name : ")
	for rec in cursor:
		if rec['name'] == n:
			collection.remove({"name":n})
			print "Record deleted!!"
	
def deleteAll(args):
	cursor = collection.find().count()
	if cursor != 0:
		collection.remove({})
		print "All records are deleted !!"
	else:
		print "There is no record !!"

parser = argparse.ArgumentParser(description = "Assignment Program")   
parser.add_argument("-i","--insert") 
parser.add_argument("-s","--show") 
parser.add_argument("-r","--remove")
parser.add_argument("-dAll","--deleteAll")
args = parser.parse_args() 

if args.insert != None:
	insert(args)
if args.show !=None:
	show(args)
if args.remove != None:
	remove(args)
if args.deleteAll != None:
	deleteAll(args)