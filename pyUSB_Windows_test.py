

import usb.core
import usb.util

vid = 0x1234  # Change it for your device
pid = 0x000b  # Change it for your device




# handler called when a report is received
def rx_handler(data):
    print('recv: ', data)


def findHIDDevice(mbed_vendor_id, mbed_product_id):
    # Find device
    found = False
    hid_device = usb.core.find(idVendor=mbed_vendor_id, idProduct=mbed_product_id)
    if not hid_device:

        print("No device connected")

    else:
        found = True
        print("device found{0}",hid_device)
        """
        if hid_device.is_kernel_driver_active(2):
            print("kernel driver is active")
        else:
            print("kernel driver is not active")"""
    return found, hid_device    

"""
def getEndpoint(hid_device):
    #extract the defualt endpoint
    found = False
    endpoint = hid_device[0][(0,0)][0]
    if not endpoint:
        print("endpoint extraction failed")
    else :
        enpoint = True
        print("the endpointID{0}",endpoint)
    return found,endpoint
"""

def getEndpoint_In(hid_device):
    found = False
    endpoint_In = hid_device[0][(0,0)][0]
    if not endpoint_In:
        print("endpoint extraction failed")
    else :
        found = True
        print("the endpoint IN: {0}",endpoint_In)
    return found,endpoint_In

def getEndpoint_Out(hid_device):
    found = False
    endpoint_Out = hid_device[0][(0,0)][1]
    if not endpoint_Out:
        print("endpoint extraction failed")
    else :
        found = True
        print("the endpoint OUT: {0}",endpoint_Out)
    return found,endpoint_Out

if __name__ == '__main__':
    # The vendor ID and product ID used in the Mbed program
    mbed_vendor_id = 0x1234
    mbed_product_id = 0x000b

    # Search the Mbed, attach rx handler and send data
    found,mHIDDevice = findHIDDevice(mbed_vendor_id, mbed_product_id)
    if found == True :
       found,mEndpoint_In = getEndpoint_In(mHIDDevice)
       found,mEndpoint_Out = getEndpoint_Out(mHIDDevice)
       #if found == True :
           # now go to an infinite while loop 