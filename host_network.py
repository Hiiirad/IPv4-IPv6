from math import log2
import re

def numHost(ip):
    if re.search(string=ip, pattern=r"\s"):
        netmask = ip.split(sep=" ")[1].split(sep=".")
        if netmask[0] != "255":
            num = 256 - int(netmask[0])
            host = 32 - int(log2(num))
            return 2 ** host - 2
        elif netmask[1] != "255":
            num = 256 - int(netmask[1])
            host = 32 - int(log2(num)) - 8
            return 2 ** host - 2
        elif netmask[2] != "255":
            num = 256 - int(netmask[2])
            host = 32 - int(log2(num)) - 16
            return 2 ** host - 2
        elif netmask[3] != "255":
            num = 256 - int(netmask[3])
            host = 32 - int(log2(num)) - 24
            return 2 ** host - 2
    else:
        Subnet = int(ip.split(sep="/")[1])
        host = 32 - Subnet
        return 2 ** host - 2

test = numHost("10.11.12.13/30")
print(test)
test1 = numHost("10.11.12.13 255.255.255.240")
print(test1)
