import csv
import re
import mysql.connector
import pyodbc 
import numpy
import string
import mysql.connector


def newdatabase():
	mydb = mysql.connector.connect(
		host = 'localhost',
		user = 'root',
		password = ''
		)
	curr = mydb.cursor()
	curr.execute("CREATE DATABASE datafeed")
	print('DB : datafeed !!')

def connection():
	mydb = mysql.connector.connect(
		host = 'localhost',
		user = 'root',
		password = '',
		database = 'datafeed'
		)
	print('go :: database datafeed')

	curr = mydb.cursor()
	curr.execute("CREATE TABLE recordType_1 (dates INT NOT NULL, timee INT NOT NULL, sequence INT NOT NULL, record_type INT NOT NULL, status  INT NOT NULL, messag VARCHAR (10))")

def index(nfield):
	for x in range (nfield) :
		field=x;
		if (field==0) :
			data = 'dates, timee, sequence, record_type, status, messag'
		elif (field==1):
			data = 'date,time,stockcode,open,high,low,close,vol,val,freq'
		elif (field==2):
			data = 'date,time,stockcode,open,high,low,close,vol,val,freq'
		elif (field==3):
			data = 'date,time,stockcode,open,high,low,close,vol,val,freq'
		elif (field==4):
			data = 'date,time,stockcode,open,high,low,close,vol,val,freq'
		elif (field==5):
			data = 'date,time,stockcode,open,high,low,close,vol,val,freq'
		elif (field==6):
			data = 'date,time,stockcode,open,high,low,close,vol,val,freq'

		filecsv = open('record_type'+ str(field) +'.csv','a')
		filecsv.write(data + '\n')
		filecsv.close()
		print('file field ' + str(field) + ': terbuat!')

def loadData(filename):
	with open(filename, 'rb') as f:
		read= [l.decode('utf8', 'ignore') for l in f.readlines()]

		for x in range (len(read)):
			row = re.split('\|',str(read[x]))
			field=row[4]
			##### NAMA TABEL #####
			if (field=='0') :
				# index = 'date,time,stockcode,open,high,low,close,vol,val,freq'
				data = (row[1:7]) #0 

			elif (field=='1'):
				# index = 'date,time,stockcode,open,high,low,close,vol,val,freq'
				data = (row[1:20]) #1 

			elif (field=='2'):
				# index = 'date,time,stockcode,open,high,low,close,vol,val,freq'
				data = (row[1:23]) #2 

			elif (field=='3'):
				# index = 'date,time,stockcode,open,high,low,close,vol,val,freq'
				data = (row[1:18]) #3

			elif (field=='4'):
				# index = 'date,time,stockcode,open,high,low,close,vol,val,freq'
				data = (row[1:8]) #4 

			elif (field=='5'):
				# index = 'date,time,stockcode,open,high,low,close,vol,val,freq'
				data = (row[1:24]) #5

			elif (field=='6'):
				# index = 'date,time,stockcode,open,high,low,close,vol,val,freq'
				data = (row[1:13]) #6

			string =','.join(str(x) for x in data)
			filecsv = open('record_type' + field + '.csv','a')
			print('success read line ',x)
			filecsv.write(string + '\n')
			filecsv.close()
			
	print('success ..')

# newdatabase()
# connection()
# index(7)
# loadData('next.txt')




# (
# 				dates INT NOT NULL, 
# 				timess INT NOT NULL, 
# 				stockcode VARCHAR(12), 
# 				open INT NOT NULL,
# 				high INT NOT NULL, 
# 				low INT NOT NULL, 
# 				close INT NOT NULL, 
# 				volume INT NOT NULL,
# 				value INT NOT NULL, 
# 				freq INT NOT NULL)")