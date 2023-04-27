#Dq is a Cisco Genie library that provides various helper functions to ease the parsing of nested Python dictionaries.
#Normally if we wanted to pull out the state for the neighbour 1.1.1.1 we would need to perform a query much like the below (painful right?).
#ospf_neighbors['vrf']['default']['address_family']['ipv4']['instance']['1']['areas']['0.0.0.0']['interfaces']['Ethernet1/1']['neighbors']['1.1.1.1']['state'] => full
#With Dq, we can simply perform the following:
#$ pip3 install "pyats[library]"
#>>> from genie.utils import Dq
#>>> Dq(ospf_neighbors).contains('1.1.1.1').get_values('state', 0)
#'full'
# https://pubhub.devnetcloud.com/media/genie-docs/docs/userguide/utils/index.html

from pyats.topology import loader
from pprint import pprint
from genie.utils import Dq
 
# Load the testbed file
tb = loader.load('/home/devasc/labs/devnet-src/liviu/sedinta6/genie/testbed.yml')
 
# Assign the CSR device to a variable
csr = tb.devices['CSR1kv']
 
# Connect to the CSR device
csr.connect()


# Issue 'show version' command and parse the output
parsed_output = csr.parse('show version')
#print (parsed_output)
# Store the standard IOS version in a variable for future use
standard_os = '16.12.02'
# Look for the 'xe_version' key and see if it contains the proper IOS version
ios_check = Dq(parsed_output).contains(standard_os).get_values('xe_version')
xe_version = parsed_output['version']['version']
#print (xe_version)


if ios_check:
    print(f"IOS Check passed! Same version:{standard_os} and existing: {xe_version}")
else:
    print (f"IOS Check failed! Existing version is: {xe_version}")
 
# Disconnect from the CSR device
csr.disconnect()
