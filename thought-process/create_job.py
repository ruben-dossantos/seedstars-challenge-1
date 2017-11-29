import jenkins

server = jenkins.Jenkins('http://localhost:8080', username='ruben', password='cenas')

server.create_job('empty', jenkins.EMPTY_CONFIG_XML)
