from pyats.topology import loader
from pprint import pprint

# Load the testbed file
tb = loader.load('/home/devasc/labs/devnet-src/liviu/sedinta6/genie/testbed.yml')

# Assign the CSR device to a variable
csr = tb.devices['CSR1kv']

# Connect to the CSR device
csr.connect()
# Issue 'show version' command and print the output
csr.execute('show version')
csr.execute('show ip ospf neighbor')


# Disconnect from the CSR device
csr.disconnect()
