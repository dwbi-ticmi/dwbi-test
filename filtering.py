import csv
import os
import re
import time
import string
import mysql.connector
import numpy as np


def accessDB(command,text) :
	if (command==0):
		DB_createDB(text)
	elif (command==1):
		DB_testConn(text) #tes koneksi database
	elif (command==2):
		DB_createTable(text) #buat tabel
	elif (command==3):
		DB_insertData(text)
	elif (command==4):
		DB_selectData(text)

def DB_createDB(nameDB):
	mydb = mysql.connector.connect(
		host = 'localhost',
		user = 'root',
		password = ''
		)
	curr = mydb.cursor()
	curr.execute("CREATE DATABASE "+nameDB)
	print('DB :: buat '+nameDB+' !!')

def DB_testConn(nameDB):
	mydb = mysql.connector.connect(
		host = 'localhost',
		user = 'root',
		password = '',
		database = nameDB
		)
	curr = mydb.cursor()
	print('DB DATAFEED :: OPEN DB '+nameDB)

def DB_createTable(nameDB):
	mydb = mysql.connector.connect(
		host = 'localhost',
		user = 'root',
		password = '',
		database = 'cobasekarang'
		)
	curr = mydb.cursor()
	nfield = 7 # MEMBUAT TABEL recordType_0 sampai recordType_6
	for i in range (nfield) :
		field = i
		if (field==0) :
			curr.execute("CREATE TABLE recordType_"+str(field)+" (dates INT NOT NULL, timee INT NOT NULL, sequence INT NOT NULL, record_type INT NOT NULL, status  INT NOT NULL, messag VARCHAR (100))")
		elif (field==1) :
			curr.execute("CREATE TABLE recordType_"+str(field)+" (dates INT NOT NULL, timee INT NOT NULL, sequence INT NOT NULL, record_type INT NOT NULL, ord_time INT NOT NULL, ord_comm INT NOT NULL, sec_code VARCHAR(100), board_code VARCHAR(100), broker_code VARCHAR(10), prices INT NOT NULL, volume INT NOT NULL, balance INT NOT NULL, SB VARCHAR(100), ord_num INT NOT NULL, best_bp INT NOT NULL, best_bv INT NOT NULL, best_op INT NOT NULL, best_ov INT NOT NULL, link_order INT NOT NULL)")
		elif (field==2) :
			curr.execute("CREATE TABLE recordType_"+str(field)+" (dates INT NOT NULL, timee INT NOT NULL, sequence INT NOT NULL, record_type INT NOT NULL, status  INT NOT NULL, trade_time INT NOT NULL, trade_comm INT NOT NULL, sec_code VARCHAR(100), board_code VARCHAR(100), trade INT NOT NULL, prices INT NOT NULL, volume INT NOT NULL, buy_code VARCHAR(100), buy_type VARCHAR(100), sell_code VARCHAR(100), sell_type VARCHAR(100), BBP INT NOT NULL, BBV INT NOT NULL, BOP INT NOT NULL, BOV INT NOT NULL, buy_ord_no INT NOT NULL, sell_ord_no INT NOT NULL)")
		elif (field==3) :
			curr.execute("CREATE TABLE recordType_"+str(field)+" (dates INT NOT NULL, timee INT NOT NULL, sequence INT NOT NULL, record_type INT NOT NULL, status  INT NOT NULL, sec_code VARCHAR(100), sec_name VARCHAR(100), sec_status INT NOT NULL, sec_type VARCHAR(100), sub_sector INT NOT NULL, ipo_prices INT NOT NULL, base_price INT NOT NULL, listed_shared INT NOT NULL, trade_list_shared INT NOT NULL, shared_lot INT NOT NULL, remarks VARCHAR(100), sec_remark VARCHAR(100), weight INT NOT NULL)")
		elif (field==4) :
			curr.execute("CREATE TABLE recordType_"+str(field)+" (dates INT NOT NULL, timee INT NOT NULL, sequence INT NOT NULL, record_type INT NOT NULL, broker_code VARCHAR(100), broker_name VARCHAR(100),broker_stat INT NOT NULL)")
		elif (field==5) :  
			curr.execute("CREATE TABLE recordType_"+str(field)+" (dates INT NOT NULL, timee INT NOT NULL, sequence INT NOT NULL, record_type INT NOT NULL, sec_code VARCHAR(100), board_code VARCHAR(100), prev_price INT NOT NULL, high_price INT NOT NULL, low_price INT NOT NULL, close_price INT NOT NULL, change_val INT NOT NULL, trade_vol INT NOT NULL, trade_val INT NOT NULL, trade_freq INT NOT NULL, indi_index INT NOT NULL, ofavail INT NOT NULL, opening_price INT NOT NULL, BBP INT NOT NULL, BBV INT NOT NULL, BOP INT NOT NULL, BV INT NOT NULL, average_pr INT NOT NULL, sec_board_st INT NOT NULL)")
		elif (field==6) :
			curr.execute("CREATE TABLE recordType_"+str(field)+" (dates INT NOT NULL, timee INT NOT NULL, sequence INT NOT NULL, record_type INT NOT NULL, index_code VARCHAR(100), ex_base_val INT NOT NULL, ex_mark_val INT NOT NULL, indexx INT NOT NULL, open INT NOT NULL, high INT NOT NULL, low INT NOT NULL, prev_index INT NOT NULL )")
		print('DB DATAFEED :: tabel recordType_' + str(field) + ' !!')

def DB_insertData(data):
	with open(data, 'rb') as f:
		read= [l.decode('utf8', 'ignore') for l in f.readlines()]
		# print(len(read))

		mydb = mysql.connector.connect(
			host = 'localhost',
			user = 'root',
			password = '',
			database = 'cobasekarang'
		)
		curr = mydb.cursor()

		for x in range (len(read)):
			row = re.split('\|',str(read[x])) # split data berdasarkan pipe
			field=row[4]
			##### NAMA TABEL #####
			if (field=='0') :
				data = (row[1:7]) #0
				sql = """INSERT INTO recordtype_0 VALUES (%s,%s,%s,%s,%s,%s)"""
			elif (field=='1'):
				data = (row[1:20]) #1 
				sql = """INSERT INTO recordtype_1 VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
			elif (field=='2'):
				data = (row[1:23]) #2 
				sql = """INSERT INTO recordtype_2 VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
			elif (field=='3'):
				data = (row[1:19]) #3
				sql = """INSERT INTO recordtype_3 VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
			elif (field=='4'):
				data = (row[1:8]) #4 
				sql = """INSERT INTO recordtype_4 VALUES (%s,%s,%s,%s,%s,%s,%s)"""
			elif (field=='5'):
				data = (row[1:24]) #5
				sql = """INSERT INTO recordtype_5 VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
			elif (field=='6'):
				data = (row[1:13]) #6
				sql = """INSERT INTO recordtype_6 VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
			curr.execute(sql, data)
			mydb.commit()
			print('DB DATAFEED :: data recordType_' + field + ' !!')

def DB_selectData(data):
	
	mydb = mysql.connector.connect(
		host = 'localhost',
		user = 'root',
		password = '',
		database = 'datafeed_idx'
	)
	curr = mydb.cursor()
	sql = """SELECT * FROM recordtype_5"""

def main():
	nameofDB = 'cobasekarang'
	# accessDB(0,nameofDB) #OK CREATE DB (nameofDB = datafeed_idx)
	# accessDB(1,nameofDB) #OK TES KONEKSI DB
	# accessDB(2,nameofDB) #OK BUAT TABEL [recordType_0 : recordType_6], nfield = 7
	filename = 'sekarang.txt' #NAME FILE HARUS SESUAI DENGAN FILE TELNET TXT
	accessDB(3,filename) #OTW DB INSERT DATA FROM FILE TELNET



main()


