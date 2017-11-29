import jenkins

server = jenkins.Jenkins('http://localhost:8080', username='ruben', password='cenas')
user = server.get_whoami()
version = 1 #server.get_version()
print('Hello %s from Jenkins %s' %(user['fullName'], version))

info = server.get_queue_info()
print(info)

jobs = server.get_jobs()
print(server.jobs_count())
for j in jobs:
	print(j)

