import json
import napalm  

driver = napalm.get_network_driver('ios')
router = driver('192.168.0.47','student','cisco')
router.open()


ios_output = router.get_facts()
print (json.dumps(ios_output, indent = 4))


ios_output = router.get_interfaces()
print (json.dumps(ios_output, sort_keys=True, indent = 4))

ios_output = router.get_interfaces_counters()
print (json.dumps(ios_output, sort_keys=True, indent = 4))

ios_output = router.get_bgp_neighbors()
print (json.dumps(ios_output, sort_keys=True, indent = 4))

ios_output = router.get_bgp_config()
print (json.dumps(ios_output, sort_keys=True, indent = 4))



