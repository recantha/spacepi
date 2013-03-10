import bluetooth

target_name = "Nintendo RVL-CNT-01"
target_address = None

devices = bluetooth.discover_devices()

for bdaddr in devices:
	if target_name == bluetooth.lookup_name(bdaddr):
		target_address = bdaddr
		break

if target_address is not None:
	print "Found BT device with address ", target_address
else:
	print "Could not find target bluetootk device nearby"


