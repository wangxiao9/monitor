# __author:EstherWang
# time:01/03/2021
from time import sleep

import pexpect
import paramiko


# def ssh_command(user, host, password, command):
#     ssh_new_key = 'Are you sure you want to continue connecting'
#     child = pexpect.popen_spawn.PopenSpawn('ssh -l %s %s %s' % (user, host, command))
#     i = child.expect([pexpect.TIMEOUT, ssh_new_key, 'password: '])
#     if i == 0:
#         print('ERROR!')
#         print ('SSH could not login. Here is what SSH said:')
#         print (child.before, child.after)
#         return None
#     if i == 1:
#         child.sendline('yes')
#         child.expect('password: ')
#         i = child.expect([pexpect.TIMEOUT, 'password: '])
#         if i == 0:
#             print('ERROR!')
#             print('SSH could not login. Here is what SSH said:')
#             print(child.before, child.after)
#             return None
#     child.sendline(password)
#     return child

def loginLinux(username, ip, password, command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, 22, username=username, password=password, timeout=20)
    if command == 'top':
        stdin, stdout, stderr = client.exec_command(command)
        sleep(2)
        client.exec_command('q')
    else:
        stdin, stdout, stderr = client.exec_command(command)
    results = stdout.readlines()

    print(results)

if __name__ == '__main__':
    loginLinux("root", "47.102.113.194", "!Newhire17", "top -d 3 -b -n 2 | grep 27292")
    # loginLinux("root", "10.68.40.35", "dong", 'top -n 2| grep 742')