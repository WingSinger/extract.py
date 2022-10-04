import os, sys, time
from subprocess import getoutput

# Changing to the directory where, 
# all wifi connections are preserved.

os.chdir("/etc/NetworkManager/system-connections")
allConnections = {}
AnyPasswordinTheFile = False

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
            AnyPassword = True
            if AnyPasswordinTheFile:
                allConnections[currentSSID] = SSIDpassword


print("username\t \tpassword")
print("-------------------------------------")
for key, value in zip(allConnections.keys(), allConnections.values()):
    print(f"{key} \t\t{value}", end = '\n')
