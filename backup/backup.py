import csv
import re
import mysql.connector
import pyodbc 
import numpy
import string


def loadData(filename,field):
	with open(filename, 'rb') as f:
		read= [l.decode('utf8', 'ignore') for l in f.readlines()]

		# ##### NAMA TABEL #####
		# if (field==0) :
		# 	data = 'date,time,stockcode,open,high,low,close,vol,val,freq'
		# elif (field==1):
		# 	data = 'date,time,stockcode,open,high,low,close,vol,val,freq'
		# elif (field==2):
		# 	data = 'date,time,stockcode,open,high,low,close,vol,val,freq'
		# elif (field==3):
		# 	data = 'date,time,stockcode,open,high,low,close,vol,val,freq'
		# elif (field==4):
		# 	data = 'date,time,stockcode,open,high,low,close,vol,val,freq'
		# elif (field==5):
		# 	data = 'date,time,stockcode,open,high,low,close,vol,val,freq'
		# elif (field==6):
		# 	data = 'date,time,stockcode,open,high,low,close,vol,val,freq'

	
		# filecsv = open('record_type'+ field +'.csv','a')
		# filecsv.write(data + '\n')
		# filecsv.close()


		for x in range (len(read)):
			row = re.split('\|',str(read[x]))
			# row[5]=re.sub('\s','',row[5])
			if (row[4]=='0'):
				data = (row[1:7]) #0 
			elif (row[4]=='1'):
				data = (row[1:19]) #1 
			elif (row[4]=='2'):
				data = (row[1:22]) #2 
			elif (row[4]=='3'):
				data = (row[1:18]) #3 
			elif (row[4]=='4'):
				data = (row[1:8]) #4 
			elif (row[4]=='5'):
				data = (row[1:24]) #5
			elif (row[4]=='6'):
				data = (row[1:13]) #6 
			
			string =','.join(str(x) for x in data)
			filecsv = open('record_type' + field + '.csv','a')
			print('success read line ',x)
			filecsv.write(string + '\n')
			filecsv.close()
			
	print('success ..')



loadData('next.txt','5')
# build_db()
# createtable()
# dosqlServer()