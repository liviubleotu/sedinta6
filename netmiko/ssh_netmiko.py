from netmiko import ConnectHandler
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
    net_connect = ConnectHandler(**router)
    net_connect.enable()
    commands = ["show run int Gig1", "show run int Gig2", "show version | i uptime"]

    for i in commands:
        interface_cli = net_connect.send_command(i)
        print("Output-ul comenzii " + i +" este:")
        print(interface_cli)
