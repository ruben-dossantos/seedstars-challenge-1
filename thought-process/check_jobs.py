import jenkins
import datetime

server = jenkins.Jenkins('http://localhost:8080', username='ruben', password='cenas')

jobs = server.get_jobs()
now = datetime.datetime.now()
for job in jobs:
	name = job['name']
	color = job['color']
	print('name=%s, color=%s, date=%s' %(name, color, now))

