#!/usr/bin/python
# -*- coding: utf-8 -*-

import jenkins
import datetime
import sqlite3 as lite
import sys
import json

configs = json.load(open('jenkins_config.json'))

j_server = jenkins.Jenkins(
	configs['server'], 
	username=configs['username'], 
	password=configs['password']
	)

jobs = j_server.get_jobs()
now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
db_connection = None

try:
	db_connection = lite.connect('challenge.db')

	with db_connection:
		cursor = db_connection.cursor()
		cursor.execute('CREATE TABLE if not exists JOBS(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, status TEXT, timestamp DATETIME)')

		rows = []
		for job in jobs:
			name = job['name']
			item = (name, job['color'], unicode(now))
			cursor.execute('INSERT INTO JOBS (name, status, timestamp) VALUES (?, ?, ?)', item)
			print('Job inserted: %s' % name)

except lite.Error, e:
	print "Error %s: " % e.args[0]
	sys.exit(1)

finally:
	if db_connection:
		db_connection.close()
