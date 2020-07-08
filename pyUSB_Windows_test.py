

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

def send_test_message(endpoint):
       # def write(self, data, timeout = None):
        r"""Write data to the endpoint.

        The parameter data contains the data to be sent to the endpoint and
        timeout is the time limit of the operation. The transfer type and
        endpoint address are automatically inferred.

        The method returns the number of bytes written.

        For details, see the Device.write() method.
        """
        """
        USB_MSG_GET_DEVICE_INFO = 0x03,           // 3
        USB_MSG_GET_DEVICE_INFO_REPLY,     // 4   """
        
        out_msg = [3,0]
        outData = bytearray(out_msg)
        write_length = endpoint.write(outData)
        print("endpoint write length: {0}", write_length)
        
def send_test_message2(hid_device, endpoint):
       # def write(self, data, timeout = None):
        r"""Write data to the endpoint.

        The parameter data contains the data to be sent to the endpoint and
        timeout is the time limit of the operation. The transfer type and
        endpoint address are automatically inferred.

        The method returns the number of bytes written.

        For details, see the Device.write() method.
        """
        """
        USB_MSG_GET_DEVICE_INFO = 0x03,           // 3
        USB_MSG_GET_DEVICE_INFO_REPLY,     // 4   """
        
        out_msg = [3,0]
        outData = bytearray(out_msg)
        print("outData: {0}", "30")  
        write_length = hid_device.write(endpoint ,data= outData)
        print("endpoint write length: {0}", write_length)        

if __name__ == '__main__':
    # The vendor ID and product ID used in the Mbed program
    mbed_vendor_id = 0x1234
    mbed_product_id = 0x000b

    # Search the Mbed, attach rx handler and send data
    found,mHIDDevice = findHIDDevice(mbed_vendor_id, mbed_product_id)
    if found == True :
       found,mEndpoint_In = getEndpoint_In(mHIDDevice)
       found,mEndpoint_Out = getEndpoint_Out(mHIDDevice)
       
       #mHIDDevice.write()
       #mEndpoint_Out.Wr
       #send_test_message(mEndpoint_Out)
       send_test_message2(mHIDDevice,mEndpoint_Out)
       #if found == True :
           # now go to an infinite while loop 