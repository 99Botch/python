import socket
import subprocess
import sys
from datetime import datetime

subprocess.call('clear', shell=True)

remoteServerIP = input('Enter a server\'s IP: ')

print('-' * 30)
print('LAUNCH SCAN OF ' + remoteServerIP)
print('-' * 30)

t1 = datetime.now()

try:
    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print('Port {}: Open'.format(port))
        sock.close()
except KeyboardInterrupt:
    print('Scan Interrupted')
    sys.exit()
except socket.error:
    print('Could not connect to server')
    sys.exit()

t2 = datetime.now()

watcher = t2 - t1
print('Scan completed in {}'.format(watcher ))