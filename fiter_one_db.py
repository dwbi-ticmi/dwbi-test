import csv
import os
import re
import time
import string
import mysql.connector
import numpy as np

def DB_createTable():
	mydb = mysql.connector.connect(
		host = 'localhost',
		user = 'root',
		password = '',
		database = 'nest'
		)
	curr = mydb.cursor()
	curr.execute("CREATE TABLE recordType (dates INT NOT NULL, timee INT NOT NULL, sequence INT NOT NULL, record_type INT NOT NULL, sec_code VARCHAR(100), board_code VARCHAR(100), prev_price INT NOT NULL, high_price INT NOT NULL, low_price INT NOT NULL, close_price INT NOT NULL, change_val INT NOT NULL, trade_vol INT NOT NULL, trade_val INT NOT NULL, trade_freq INT NOT NULL, indi_index INT NOT NULL, ofavail INT NOT NULL, opening_price INT NOT NULL, BBP INT NOT NULL, BBV INT NOT NULL, BOP INT NOT NULL, BV INT NOT NULL, average_pr INT NOT NULL, sec_board_st INT NOT NULL)")
    print('DB DATAFEED :: tabel recordType !!')

# def DB_insertData(data):
# 	with open(data, 'rb') as f:
# 		read= [l.decode('utf8', 'ignore') for l in f.readlines()]
# 		# print(len(read))

# 		mydb = mysql.connector.connect(
# 			host = 'localhost',
# 			user = 'root',
# 			password = '',
# 			database = 'datafeed_idx'
# 		)
# 		curr = mydb.cursor()

# 		for x in range (len(read)):
# 			row = re.split('\|',str(read[x])) # split data berdasarkan pipe
# 			field=row[4]
# 			##### NAMA TABEL #####
# 			if (field=='0') :
# 				data = (row[1:7]) #0
# 				sql = """INSERT INTO recordtype_0 VALUES (%s,%s,%s,%s,%s,%s)"""
# 			elif (field=='1'):
# 				data = (row[1:20]) #1 
# 				sql = """INSERT INTO recordtype_1 VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
# 			elif (field=='2'):
# 				data = (row[1:23]) #2 
# 				sql = """INSERT INTO recordtype_2 VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
# 			elif (field=='3'):
# 				data = (row[1:19]) #3
# 				sql = """INSERT INTO recordtype_3 VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
# 			elif (field=='4'):
# 				data = (row[1:8]) #4 
# 				sql = """INSERT INTO recordtype_4 VALUES (%s,%s,%s,%s,%s,%s,%s)"""
# 			elif (field=='5'):
# 				data = (row[1:24]) #5
# 				sql = """INSERT INTO recordtype_5 VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
# 			elif (field=='6'):
# 				data = (row[1:13]) #6
# 				sql = """INSERT INTO recordtype_6 VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
# 			# curr.execute(sql, data)
# 			# mydb.commit()
# 			print('DB DATAFEED :: data recordType_' + field + ' !!')


DB_createTable()