import os
import sys

import usb.core
import usb.util

vid = 0x1234  # Change it for your device
pid = 0x000b  # Change it for your device


from time import sleep
import random


# handler called when a report is received
def rx_handler(data):
    print('recv: ', data)


def findHIDDevice(mbed_vendor_id, mbed_product_id):
    # Find device
    hid_device = usb.core.find(idVendor=mbed_vendor_id, idProduct=mbed_product_id)
    if not hid_device:

        print("No device connected")

    else:
        print("device found")
        if hid_device.is_kernel_driver_active(2):
            print("kernel driver is active")
        else:
            print("kernel driver is not active")


if __name__ == '__main__':
    # The vendor ID and product ID used in the Mbed program
    mbed_vendor_id = 0x1234
    mbed_product_id = 0x000b

    # Search the Mbed, attach rx handler and send data
    findHIDDevice(mbed_vendor_id, mbed_product_id)
