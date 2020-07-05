import hid

vid = 0x1234	# Change it for your device
pid = 0x000b	# Change it for your device

"""
def readData(data):
    #print(data)
    print("Raw data: {0}".format(data))
    return None

# VID and PID customization changes here...
filter = hid.HidDeviceFilter(vendor_id = 0x1234, product_id = 0x000b)
hid_device = filter.get_devices()
device = hid_device[0]
device.open()
print(hid_device)

device.set_raw_data_handler(readData)
"""

device = hid.Device()
device.open(vid,pid)
print('Connected to ADU{}\n'.format(pid))
