#IPV4 address range calculator.
#Author: Nolan Raymond

import ipaddress

print("Please enter network address in CIDR notation (ex: 10.0.2.0/29)")
addr = input("Enter your address here: ")
range = ipaddress.ip_network(addr)
for x in range.hosts():
        print(x)
