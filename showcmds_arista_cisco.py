from netmiko import ConnectHandler
from getpass import getpass

ipaddress = input("Enter an IP address: ")
username = input("username: ")
device = ConnectHandler(device_type = 'cisco_ios', ip=ipaddress,  username=username, password=getpass())
output1 = device.send_command("show version")
output2 = device.send_command("show ip int brief")
output3 = device.send_command("show int description")

print(output1)
print(output2)
print(output3)