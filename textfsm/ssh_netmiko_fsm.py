from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint


router_devnet = {"device_type": "cisco_ios",
          "ip": "sandbox-iosxe-latest-1.cisco.com",
          "username" : "admin",
          "port" : "22",
          "password": "C1sco12345",
          }

router_local = {"device_type": "cisco_ios",
          "ip": "192.168.0.47",
          "username" : "student",
          "port" : "22",
          "password": "cisco",
          }


lista_rutere = [router_local,router_devnet]
for router in lista_rutere:
    commands = ["show ip interface brief", "show version"]
    for commands in commands:    
        with ConnectHandler(**router) as net_connect:
        # Use TextFSM to retrieve structured data
            output = net_connect.send_command(commands, use_textfsm=True)
            print()
            pprint(output)
            print()





