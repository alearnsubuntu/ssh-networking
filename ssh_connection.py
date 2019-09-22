import paramiko
import os.path
import time
import sys
import re

#ask for username and password file path
user_file = input("#Enter user file path and name: ")

#verification of username and password file path
if os.path.isfile(user_file) == True:
    print("Username and Password is valid")
#if the username and password file path is invalid it would return an error message
else:
    print("File {} does not exist. Please check and try again".format(user_file))
#ask for command file path
cmd_file = input("#Enter commands path and name: ")
#verify file as valid
if os.path.isfile(cmd_file) == True:
    print("CMD file is valid")

else:
    print("File {} does not exist. Please check and try again".format(cmd_file))
    sys.exit()
#Establish SSH Connection to arista
def ssh_connection(ip_address):
    #import the global variables
    global user_file
    global cmd_file
    #create SSH connection
    try:
        #open and read the user file
        selected_user_file = open(user_file, "r")
        #starts at the first line
        selected_user_file.seek(0)
        #read user file contents, grab the first line and split on comma
        user_name_password_list = selected_user_file.readlines()[0].split(',')        
        print(user_name_password_list)
        #grab the first item from list as username
        user_name = user_name_password_list[0]
        #grab the second item from list as password
        password = user_name_password_list[1]
        #creating an paramiko ssh client
        session = paramiko.SSHClient()
        #add missing host key policy
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        #connecting to the device through username and password
        session.connect(ip_address, username = user_name, password = password)
        #start shell session
        connection = session.invoke_shell()
        #sending commands to the device through paramiko
        connection.send("enable\n")
        connection.send("terminal length 0\n")
        time.sleep(1)
        #turning on the global configuration mode
        connection.send("\n")
        connection.send("Configure terminal\n")
        time.sleep(1)
        #opening the selected file for reading
        selected_cmd_file = open(cmd_file, "r")
        #open command file for reading
        selected_cmd_file.seek(0)
        #write each line of the file into the device
        for each_line in selected_cmd_file.readlines():
            connection.send(each_line + '\n')
            time.sleep(2)
        #close the user file
        selected_user_file.close()
        #close command file
        selected_cmd_file.close()
        #check the command output for any syntax errors
        router_output = connection.recv(65535)
        
        if re.search(b"% Invalid input", router_output):
            print("* There was at least one IOS syntax error on device {} ".format(ip_address))
            
        else:
            print("\nDone for device {} \n".format(ip_address))
        
        print(str(router_output) + "\n")
        #closing the connection
        session.close()
    #exception handling
    except paramiko.AuthenticationException:
        print("* Invalid username or password")
        print("* Closing program... Bye!")

ssh_connection("10.10.10.2")
    