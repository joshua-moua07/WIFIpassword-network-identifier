#wifi password program
#search windows for known wifi passwords
#display the passwords alongside the network name
#import subprocess module

import subprocess #import the subprocess module

check_net = subprocess.run("netsh wlan show profile", capture_output=True, text=True) #variable to input command to Windows Terminal, shows us Network IDs 
#.run command = runs a command from Windows / capture_output = capture and store what the command prints, text = make the output readable as strings
output = check_net.stdout.splitlines() #Split the output into lines we can work with
#.stdout shows what the command printed and stores the command in Python so we can use it
net_list = [] #create a list to store network IDs
pw_list = [] #create a list to store key's
for user_profile in output: #for loop to loop through the output from the first command
    if "All User Profile" in user_profile: #if statement that goes through the output, finds the corresponding text
        networks = user_profile.split(":") #split the corresponding text based on where the colon is
        net_list.append(networks[-1]) #append the right side (-1) to our list, which is our Network IDs

for netID in net_list: #for loop to loop through the network IDs 
    PW_NET = subprocess.run(f"netsh wlan show profile name={netID} key=clear", capture_output=True, text=True) #loop through the network IDs and input them into the command
    key_output = PW_NET.stdout.splitlines() #take the output and split them into lines
    for lines in key_output: #for loop that loops through the output
        if "Key Content" in lines: #if statement that searches through the lines for the corresponding text
            keys = lines.split(":") #split the lines at the text
            pw_list.append(keys[-1]) #append the keys on the right side (-1) to our password list

print(net_list,"\n", pw_list) #print the network IDs and passwords on separate lines




        

