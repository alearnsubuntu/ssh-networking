import sys
import subprocess
 
#Checking IP reachability
def ip_reach(list):
 
    for ip in list:
        ip = ip.rstrip("\n")
        
        ping_reply = subprocess.call('ping %s -c 2' % (ip), shell = True, stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL)
               
        if ping_reply == 0:
            print("\n* {} is reachable :)\n".format(ip))
            continue
        
        else:
            print('\n* {} not reachable :( Check connectivity and try again.'.format(ip))
            sys.exit()
        
list = ["8.8.8.8", "10.10.10.1"]
ip_reach(list)