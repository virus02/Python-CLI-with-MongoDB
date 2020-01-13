import argparse 
from pymongo import MongoClient 
from random import randint

try:
	conn = MongoClient()
	print "Database Connected Successfully :)"
except:
	print "Database Connection Failed !!"
#please change the db name(test) to your db name
db = conn.test
#please change collection(mycollection) to your collection name
collection = db.mycollection

def insert(args):
	try:
		rnum = randint(0,999)
		name = raw_input("Enter a name : ")
		age = int(raw_input("Enter an age : "))
		loc = raw_input("Enter a location : ")

		emp_det = {"id":rnum,"name":name,"age":age,"loc":loc}
		rec_id1 = collection.insert_one(emp_det) 

		print "Record Inserted"
	except:
		print "Please enter proper inputs"

def show(args):
	cursor = collection.find()
	if cursor.count() == 0:
		print "There is no record !!"
	else:
		for record in cursor:
			print record
		print "--------------------------"
		
		#finding particular values and selecting fields
		choice = raw_input("Enter F to find all the records which contain a particular value OR S to find perticular field : ")
		
		if (choice.upper() == "F"):
			value = raw_input("Enter a field to check the value : ")
			frecords = collection.find({}, {value:1, "_id":0})
			for frecord in frecords:
				print frecord
		elif (choice.upper() == "S"):
			cur = collection.find()
			field = raw_input("Enter field: ")
			if field == "id" or field == "age":
				try:
					value = int(raw_input("Enter value :  "))
					for rec in cur:
						if rec[field] == value:
							print rec
				except:
					print "There is no such record !!"
			else:
				try:
					value = raw_input("Enter value :  ")
					for rec in cur:
						if rec[field] == value:
							print rec
				except:
					print "There is no such record !!"
		else:
			print "Please enter F or S according to your need"

def remove(args):
	cursor = collection.find()
	count = cursor.count()
	if count != 0:
		try:
			n = int(raw_input("Enter ID : "))
			for rec in cursor:
				if rec['id'] == n:
					collection.remove({"id":n})
					print "Record deleted!!"
					count = count + 1
			if cursor.count() == count:
				print "Could not find the record !!"
		except :
			print "Please enter ID"
	else:
		print "There is no record !!"
	
def deleteAll(args):
	cursor = collection.find().count()
	if cursor != 0:
		collection.remove({})
		print "All records are deleted !!"
	else:
		print "There is no record !!"

parser = argparse.ArgumentParser(description = "Assignment Program")   
parser.add_argument("-i","--insert",help = "Enter your name, age and location") 
parser.add_argument("-s","--show", help="It displays the record") 
parser.add_argument("-r","--remove",help="It deletes the record of perticular ID")
parser.add_argument("-dAll","--deleteAll",help="It deletes all the records")
args = parser.parse_args() 

if args.insert != None:
	insert(args)
if args.show !=None:
	show(args)
if args.remove != None:
	remove(args)
if args.deleteAll != None:
	deleteAll(args)
