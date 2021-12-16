from netmiko import ConnectHandler
from getpass import getpass


ipaddress = input("Enter an IP address: ")
arista = {
'device_type': 'cisco_ios',
'ip': ipaddress,
'username': 'yichang.chen',
'password': 'Ready2Go@@',
}

# juniper = {
# 'device_type': 'juniper',
# 'ip': ipaddress,
# 'username': 'yichang.chen',
# 'password': 'Ready2Go@@',
# }

huawei = {
'device_type': 'huawei_ssh',
'ip': ipaddress,
'username': 'yichang.chen',
'password': 'Ready2Go@@',
}


all_devices = [arista, huawei]

for a_device in all_devices:
    net_connect = ConnectHandler(**a_device)
    output = net_connect.send_command("show version")
    output1 = net_connect.send_command("display version")
    print(f"\n\n--------- Device {a_device['device_type']} ---------")
    print(output)
    print(output1)
    print("--------- End ---------")
