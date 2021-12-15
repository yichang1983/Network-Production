from netmiko import ConnectHandler
from getpass import getpass

try:
    ipaddress = input("Enter an IP address: ")
    username = input("username: ")
    device = ConnectHandler(device_type= 'huawei_ssh', ip=ipaddress, username=username, password=getpass())
except Exception as E:  # Exception as E 就是截取全部的錯誤，把它當成E
    print("Issue: ", E)  # 印出 E(錯誤的訊息)

else:
    output1 = device.send_command("display version")
    output2 = device.send_command("display clock")
    output3 = device.send_command("display health")
    output4 = device.send_command("display ip interface brief")
    output5 = device.send_command("display interface description")
    print("display version:\n")    #\n 空下一行的意思
    print(output1)
    print("\n")                    #\n 印出結果後，空一行，感覺才不會跟下一個執行結果擠在一起。
    print("****************************************************************************************************")
    print("display clock:\n")
    print(output2)
    print("\n")                    #\n 印出結果後，空一行，感覺才不會跟下一個執行結果擠在一起。
    print("****************************************************************************************************")
    print("display health:\n")
    print(output3)
    print("\n")                     #\n 印出結果後，空一行，感覺才不會跟下一個執行結果擠在一起。
    print("****************************************************************************************************")
    print("display ip interface brief:\n")
    print(output4)
    print("\n")                     #\n 印出結果後，空一行，感覺才不會跟下一個執行結果擠在一起。
    print("****************************************************************************************************")
    print ("display interface description:\n")
    print(output5)
    print("\n")                     #\n 印出結果後，空一行，感覺才不會跟下一個執行結果擠在一起。
finally:
    print("****************************************************************************************************")
    print("Close")













