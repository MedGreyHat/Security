import socket 
import subprocess
import sys
from datetime import datetime 

remoteServer = raw_input("Eter the target host to scan : ")
remoteServerIP = socket.gethostbyname(remoteServer)
print "-"*60
print "Please wait, scanning target host ", remoteServerIP
print "-"*60

t1 = datetime.now()

try : 
    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        res = sock.connect_ex((remoteServerIP, port))
        if not res :
            print "Port {}: Opened".format(port)
        sock.close()
except KeyboardInterrupt:
    print "You pressed Ctrl + C"        
    sys.exit()

except socket.gaierror: 
    print "Hostname could not be resolved. Exiting"
    sys.exi()
except socket.error: 
    print "Couldn't connect to server"
    sys.exit()

t2 = datetime.now()

total = t2 - t1

print "Scanning Completed in : ",  total 



