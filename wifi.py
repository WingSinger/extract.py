import os, sys, time
from subprocess import getoutput

# Changing to the directory where, 
# all wifi connections are preserved.

os.chdir("/etc/NetworkManager/system-connections")
AnyPasswordinTheFile = False
allConnections = {}
totalConnections = 0

print("username\t \tpassword")
print("-------------------------------------")

for _file in os.listdir():
    # Reading files, which contains info regarding to connections.
    with open(_file, 'r') as fp:
        lines = fp.readlines()
        fp.close()

    # some files does not contain passwords, but have a ssid, we're 
    # going to skip those files, and extract info from only those
    # files which have the 'psk=<password>' keyword.

    for line in lines:
        if 'ssid' in line:
            currentSSID = line.split("=")[1]
            currentSSID = currentSSID.replace('\n', '')

        if 'psk=' in line:
            SSIDpassword = line.split("=")[1]
            SSIDpassword = SSIDpassword.replace('\n', '')
            AnyPasswordinTheFile = True

            if AnyPasswordinTheFile:
                # If there is any password in the file.
                # add  it to the dictionary.
                allConnections[currentSSID] = SSIDpassword


for key, value in zip(allConnections.keys(), allConnections.values()):
    print(f"{key} \t\t{value}", end = '\n')
    time.sleep(0.1)

print(f"\nTotal {len(allConnections)} connections resolved from the computer")
