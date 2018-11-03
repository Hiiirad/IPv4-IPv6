import re

# Checking IPv4 and IPv6 ranges
# https://www.iana.org/assignments/iana-ipv4-special-registry/iana-ipv4-special-registry.xhtml


def detection(domain):
    domain = str(domain)
    if re.search(string=domain, pattern=r"^([0-9]|[1-8][0-9]|9[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-8][0-9]|9[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-8][0-9]|9[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-8][0-9]|9[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"):
        if re.search(string=domain, pattern=r"^0\.([0-9]|[1-8][0-9]|9[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-8][0-9]|9[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-8][0-9]|9[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"):
            return "Your IP is in 0.0.0.0/8 which is This host on this network"
        elif re.search(string=domain, pattern=r"^10\.([0-9]|[1-8][0-9]|9[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-8][0-9]|9[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-8][0-9]|9[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"):
            return "Your IP is in 10.0.0.0/8 which is Private-Use"
        elif re.search(string=domain, pattern=r"^100\.(6[4-9]|[7-9][0-9]|1[01][0-9]|12[0-7])\.([0-9]|[1-8][0-9]|9[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-8][0-9]|9[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"):
            return "Your IP is in 100.64.0.0/10 which is Shared Address Space"
        elif re.search(string=domain, pattern=r"^127\.([0-9]|[1-8][0-9]|9[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-8][0-9]|9[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-8][0-9]|9[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"):
            return "Your IP is in 127.0.0.0/8 which is Loopback"
        elif re.search(string=domain, pattern=r"^169\.254\.([0-9]|[1-8][0-9]|9[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-8][0-9]|9[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"):
            return "Your IP is in 169.254.0.0/16 which is Link Local"
        elif re.search(string=domain, pattern=r"^172\.(1[6-9]|2[0-9]|3[01])\.([0-9]|[1-8][0-9]|9[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-8][0-9]|9[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"):
            return "Your IP is in 172.16.0.0/12 which is Private-Use"
        elif re.search(string=domain, pattern=r"^192\.0\.0\.([0-9]|[1-8][0-9]|9[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"):
            return "Your IP is in 192.0.0.0/24 which is IETF Protocol Assignments"
        elif re.search(string=domain, pattern=r"^192\.0\.0\.8$"):
            return "Your IP is in 192.0.0.8/32 which is IPv4 Dummy Address"
        elif re.search(string=domain, pattern=r"^192\.0\.0\.9$"):
            return "Your IP is in 192.0.0.9/32 which is Port Control Protocol Anycast"
        elif re.search(string=domain, pattern=r"^192\.0\.0\.10$"):
            return "Your IP is in 192.0.0.10/32 which is Traversal Using Relays around NAT Anycast"
        elif re.search(string=domain, pattern=r"^192\.0\.0\.(17[01])$"):
            return "Your IP is in 192.0.0.170/32 and 192.0.0.171/32 which is NAT64/DNS64 Discovery"
        elif re.search(string=domain, pattern=r"^192\.0\.2\.([0-9]|[1-8][0-9]|9[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"):
            return "Your IP is in 192.0.2.0/24 which is Documentation (TEST-NET-1)"
        elif re.search(string=domain, pattern=r"^192\.31\.196\.([0-9]|[1-8][0-9]|9[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"):
            return "Your IP is in 192.31.196.0/24 which is AS112-v4"
        elif re.search(string=domain, pattern=r"^192\.52\.193\.([0-9]|[1-8][0-9]|9[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"):
            return "Your IP is in 192.52.193.0/24 which is AMT"
        elif re.search(string=domain, pattern=r"^192\.88\.99\.([0-9]|[1-8][0-9]|9[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"):
            return "Your IP is in 192.88.99.0/24 which is Deprecated (6to4 Relay Anycast)"
        elif re.search(string=domain, pattern=r"^192\.168\.([0-9]|[1-8][0-9]|9[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-8][0-9]|9[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"):
            return "Your IP is in 192.168.0.0/16 which is Private-Use"
        elif re.search(string=domain, pattern=r"^192\.175\.48\.([0-9]|[1-8][0-9]|9[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"):
            return "Your IP is in 192.175.48.0/24 which is Direct Delegation AS112 Service"
        elif re.search(string=domain, pattern=r"^198\.(1[89])\.([0-9]|[1-8][0-9]|9[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-8][0-9]|9[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"):
            return "Your IP is in 198.18.0.0/15 which is Benchmarking"
        elif re.search(string=domain, pattern=r"^198\.51\.100\.([0-9]|[1-8][0-9]|9[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"):
            return "Your IP is in 198.51.100.0/24 which is Documentation (TEST-NET-2)"
        elif re.search(string=domain, pattern=r"^203\.0\.113\.([0-9]|[1-8][0-9]|9[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"):
            return "Your IP is in 203.0.113.0/24 which is Documentation (TEST-NET-3)"
        elif re.search(string=domain, pattern=r"^(24[0-9]|25[0-5])\.([0-9]|[1-8][0-9]|9[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-8][0-9]|9[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-8][0-9]|9[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-4])$"):
            return "Your IP is in 240.0.0.0/4 which is Reserved"
        elif re.search(string=domain, pattern=r"^255\.255\.255\.255$"):
            return "Your IP is in 255.255.255.255/32 which is Limited Broadcast"
    elif re.search(string=domain, pattern=r"^\s*((([0-9A-Fa-f]{1,4}:){7}([0-9A-Fa-f]{1,4}|:))|(([0-9A-Fa-f]{1,4}:){6}(:[0-9A-Fa-f]{1,4}|((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){5}(((:[0-9A-Fa-f]{1,4}){1,2})|:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){4}(((:[0-9A-Fa-f]{1,4}){1,3})|((:[0-9A-Fa-f]{1,4})?:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){3}(((:[0-9A-Fa-f]{1,4}){1,4})|((:[0-9A-Fa-f]{1,4}){0,2}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){2}(((:[0-9A-Fa-f]{1,4}){1,5})|((:[0-9A-Fa-f]{1,4}){0,3}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){1}(((:[0-9A-Fa-f]{1,4}){1,6})|((:[0-9A-Fa-f]{1,4}){0,4}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(:(((:[0-9A-Fa-f]{1,4}){1,7})|((:[0-9A-Fa-f]{1,4}){0,5}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:)))(%.+)?\s*$"):
        if re.search(string=domain, pattern=r"^(F[D|C])", flags=re.IGNORECASE):
            return "Your IP is Private IPv6"
        else:
            return "Your IP is Public IPv6"
    else:
        return "Check your domain again!"


test = detection("127.0.0.1")
print(test)
