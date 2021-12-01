import socket

from netmiko import ConnectHandler
from sys import argv
from getpass import getpass

manufacturer = argv[1]
ipaddress = argv[2]
username = argv[3]
passw = argv[4]

#python3.6 showcmds.py Juniper 1.1.1.1 user password  (first argu is Juniper, then ip address then username then password)
#when you going to run the file you need to put this "python3.6 showcmds.py Juniper 1.1.1.1 user password" in order to run.

if manufacturer == "cisco":
    device = ConnectHandler(device_type='cisco_ios', ip=ipaddress, username=username, password=passw)
    print("device=", device)
    output1 = device.send_command("show version")
    output2 = device.send_command("show ip int br | e down")
    output3 = device.send_command("show int status")
elif manufacturer == "arista":
    device = ConnectHandler(device_type='cisco_ios', ip=ipaddress, username=username, password=passw)
    output1 = device.send_command("show version")
    output2 = device.send_command("show ip int br | e down")
    output3 = device.send_command("show int status")
elif manufacturer == "huawei":
    device = ConnectHandler(device_type='huawei_ssh', ip=ipaddress, username=username, password=passw)
    output1 = device.send_command("display version")
    output2 = device.send_command("display interfaces")
    output3 = device.send_command("display ?")
elif manufacturer == "juniper":
    device = ConnectHandler(device_type='juniper', ip=ipaddress, username=username, password=passw)
    output1 = device.send_command("show config | display set | match protocol")
    output2 = device.send_command("show version")
    output3 = device.send_command("show interface")
elif manufacturer == "brocade_netiron":
    device = ConnectHandler(device_type='brocade_netiron', ip=ipaddress, username=username, password=passw)
    output1 = device.send_command("show version")
    output2 = device.send_command("show interface brief")
    output3 = device.send_command("show lldp neigh")
elif manufacturer == "brocade":
    device = ConnectHandler(device_type='brocade_nos_ssh', ip=ipaddress, username=username, password=passw)
    output1 = device.send_command("show version")
    output2 = device.send_command("show interface brief")
    output3 = device.send_command("show lldp neigh")
else:
    print("syntax:  python showcmds.py <manufacturer> <device ip address> <username> <password>")
    exit()


print(output1)
print(output2)
print(output3)
device.disconnect()