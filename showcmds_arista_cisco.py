from netmiko import ConnectHandler
from getpass import getpass

try:
    ipaddress = input("Enter an IP address: ")
    username = input("username: ")
    device = ConnectHandler(device_type = 'cisco_ios', ip=ipaddress,  username=username, password=getpass())
except Exception as E:  # Exception as E 就是截取全部的錯誤，把它當成E
    print("Issue: ", E)  # 印出 E(錯誤的訊息)

else:
    output1 = device.send_command("show version")
    output2 = device.send_command("show clock")
    output3 = device.send_command("show environment all")
    output4 = device.send_command("show ip int brief")
    output5 = device.send_command("show int description")
    print("show version:\n")    #\n 空下一行的意思
    print(output1)
    print("****************************************************************************************************")
    print("show clock:\n")
    print(output2)
    print("****************************************************************************************************")
    print("show environment all:\n")
    print(output3)
    print("****************************************************************************************************")
    print("show ip int brief:\n")
    print(output4)
    print("****************************************************************************************************")
    print ("show int description:\n")
    print(output5)
finally:
    print("****************************************************************************************************")
    print("Close")