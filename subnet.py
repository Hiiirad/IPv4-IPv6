def subnet(ip):
    def specialOcted(num):
        if num % 8 == 0:
            return 0
        elif num % 8 == 1:
            return 128
        elif num % 8 == 2:
            return 192
        elif num % 8 == 3:
            return 224
        elif num % 8 == 4:
            return 240
        elif num % 8 == 5:
            return 248
        elif num % 8 == 6:
            return 252
        else:
            return 254

    Subnet = int(ip.split(sep="/")[1])
    remainder = Subnet // 8

    if remainder == 0:
        return str(specialOcted(Subnet))+".0.0.0"
    elif remainder == 1:
        return "255."+str(specialOcted(Subnet))+".0.0"
    elif remainder == 2:
        return "255.255."+str(specialOcted(Subnet))+".0"
    elif remainder == 3:
        return "255.255.255."+str(specialOcted(Subnet))
    elif remainder == 4 and specialOcted(Subnet) == 0:
        return "255.255.255.255"
    elif (remainder == 4 and specialOcted(Subnet) != 0) or 4 < remainder or remainder < 0:
        return "Invalid Subnet!"

test = subnet("10.11.12.13/23")
print(test)
