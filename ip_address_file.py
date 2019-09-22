import os.path
import sys
 
#Checking IP address file and content validity
def ip_address_valid():

    #Prompting user for input
    ip_file = input("\n Enter a valid IP address: ")
 
    #Checking if the file exists
    if os.path.isfile(ip_file) == True:
        print("File is valid")
    
    else:
        print("file is not valid")
        sys.exit()
        
    #Open user selected file for reading (IP addresses file)
    selected_file = open(ip_file, 'r')
    
    #Starting from the beginning of the file
    selected_file.seek(0)
    
    #Reading each line (IP address) in the file
    ip_list = selected_file.readlines()
    
    #Closing the file
    selected_file.close()

    return ip_list

def remove_new_lines(list):
    #Create a new list of clean ip addresses
    clean_ip_addressess = []
    
    #Iterate through the list
    for ip_address in list:
    
        #Remove new lines on each ip address
        clean_ip_address = ip_address.strip("\n")
    
        #Pass the clean ip addresses to a clean_ip_addressess list
        clean_ip_addressess.append(clean_ip_address)
    
    #Return the clean ip addressess list
    return clean_ip_addressess

dirty_list = ["10.10.10.2\n", "10.10.10.3\n", "10.10.10.4\n"]
result = remove_new_lines(dirty_list)
print(result)



    





result = ip_address_valid()
print(result)
