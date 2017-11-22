#!/usr/bin/python
import sys
import commands
from datetime import *
import time

import MySQLdb
import _mysql_exceptions

DB_HOST = "greengrass.co4tctnwmzmy.us-west-2.rds.amazonaws.com"
DB_PORT = 3306
DB_USERNAME = "root"
DB_PASSWORD = "PdXnW947JGYVWxDbXbn2BMpNWihHmcSr"
DB_DATABASE = "greengrass"

try:
	db = MySQLdb.connect(DB_HOST, DB_USERNAME, DB_PASSWORD, DB_DATABASE)
except _mysql_exceptions.OperationalError as e:
	print "Connection fails"
	print e
else:
	sql = "select * from data ORDER BY id desc limit 1"
	print sql
	cursor = db.cursor()
	try:
		cursor.execute(sql)
		db.commit()
	except:
		print "query sql fails"
		db.rollback()
	else:
		row = cursor.fetchone()
		print row
		rows = str(row)
		rows = rows.strip('\n')
		rows = rows.split(",")

		temp = rows[1]
		temp = temp.split("L")
		temp = int(temp[0]) / 10.0
		print temp
		dts = str(row)
		dts = dts.strip('\n')
		dts = dts.split("(")
		dts = dts[2]
		dts = dts.split(")")
		dts = dts[0]
		dts = dts.split(",")
		year = dts[0]
		month = dts[1].split(" ")
		month = month[1]
		day = dts[2].split(" ")
		day = day[1]
		hour = dts[3].split(" ")
		hour = hour[1]
		minute = dts[4].split(" ")
		minute = minute[1]
		second = dts[4].split(" ")
		second = second[1]
		dt = year + "-" + month + "-" + day + " " + hour + ":" + minute + ":" + second
		print dt
	finally:
		db.close()
