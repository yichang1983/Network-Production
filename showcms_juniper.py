from netmiko import ConnectHandler
from getpass import getpass

try:
    ipaddress = input("Enter an IP address: ")
    username = input("username: ")
    device = ConnectHandler(device_type='juniper', ip=ipaddress,  username=username, password=getpass())
except Exception as E:                  #Exception as E 就是截取全部的錯誤，把它當成E
    print("Error =", E)                 #印出 E(錯誤的訊息)

else:
    output1 = device.send_command("show version | match model")
    output2 = device.send_command("show system uptime")
    output3 = device.send_command("show chassis hardware")
    output4 = device.send_command("show chassis routing-engine")
    output5 = device.send_command("show interfaces descriptions")
    print("show version | match model\n")    #\n 空下一行的意思
    print(output1)
    print("****************************************************************************************************")
    print("show system uptime\n")
    print(output2)
    print("****************************************************************************************************")
    print("show chassis hardware\n")
    print(output3)
    print("****************************************************************************************************")
    print("show chassis routing-engine\n")
    print(output4)
    print("****************************************************************************************************")
    print("show ip int brief\n")
    print(output5)
finally:
    print("close")














