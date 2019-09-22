import sys

def ip_addr_valid(list):

    for ip in list:
        ip = ip.rstrip("\n")
        octet_list = ip.split('.')
        
        networkAddress1 = int(octet_list[0])
        networkAddress2 = int(octet_list[1])
        hostAddress1 = int(octet_list[2])
        hostAddress2 = int(octet_list[3])
        
        if (len(octet_list) == 4) and (1 <= networkAddress1 <= 223) and (networkAddress1 != 127) and (networkAddress1 != 169 or networkAddress2 !=254) and (0 <= networkAddress2) <= 255 and 0 <= hostAddress1 <= 255 and 0 <= hostAddress2 <= 255):
            continue
        else:
            print('\n* There was an invalid IP address in the file: {} :(\n'.format(ip))
            sys.exit()