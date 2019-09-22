from ip_address_file import ip_address_file
from ip_address_evaluate import ip_address_evaluate
from ip_address_reachability import ip_address_reachability
from ssh_connection import ssh_connection
from create_threads import create_threads

ip_address = ip_address_file() #saving ip address into a variable

try:
    ip_address_evaluate(ip_address)

except KeyboardInterrupt:
    Print ("Program aborted by user. Exiting...")
    sys.exit()
    
try:
    ip_address_reachability(ip_address)
        
except KeyboardInterrupt:
    Print ("Program aborted by user. Exiting...")
    sys.exit()
    
create_threads(ip_address, ssh_connection)

#end of program
