#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con = None

try:
	con = lite.connect('test.db')
	
	with con:
		cur = con.cursor()
		cur.execute('SELECT SQLITE_VERSION()')

		data = cur.fetchone()

		print "SQLite version: %s" % data

		cur.execute("CREATE TABLE if not exists JOBS(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, status TEXT, timestamp DATETIME)")
		cur.execute("INSERT INTO JOBS (name, status, timestamp) VALUES('Test', 'blue', '2017-11-29 16:16:22')")
	
except lite.Error, e:
	print "Error %s:" % e.args[0]
	sys.exit(1)

finally:
	if con:
		con.close()
