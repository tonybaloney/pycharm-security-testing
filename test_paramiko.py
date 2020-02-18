import paramiko

client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.client.AutoAddPolicy)

client.exec_command('banana')
client.exec_command('banana {0}'.format("x"))