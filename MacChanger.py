#!/usr/bin/python3

import re
import subprocess
import optparse

def search_mac_address(_mac_address):
    return re.search(r'([0-9a-fA-F]{2}[:-]){5}([0-9a-fA-F]{2})', str(_mac_address)).group(0)

def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac_address", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info")
    elif not options.new_mac_address:
        parser.error("[-] Please specify a new MAC address, use --help for more info")
    return options

def get_mac_addrs(_interface):
    ifconfig_result = subprocess.check_output(["ifconfig", _interface])
    mac_addrs = search_mac_address(ifconfig_result)

    if mac_addrs:
        return mac_addrs
    else:
        print("[-] Could not read MAC Address")

def set_new_mac_address(_interface, _new_mac_address):
    print("[+] Changing MAC address for " + _interface + " to " + _new_mac_address)
    subprocess.call("ifconfig " + _interface + " down", shell=True)
    subprocess.call("ifconfig " + _interface + " hw ether " + _new_mac_address, shell=True)
    subprocess.call("ifconfig " + _interface + " up", shell=True)

options = get_args()
current_mac_address = get_mac_addrs(options.interface)
print("Current MAC Address for interface " + options.interface + " is: " + current_mac_address)

set_new_mac_address(options.interface, options.new_mac_address)

new_mac_address = get_mac_addrs(options.interface)
if new_mac_address == options.new_mac_address:
    print("[+] MAC address was a sucessfully changed to " + new_mac_address)
else:
    print("[-] MAC address did not get changed")
