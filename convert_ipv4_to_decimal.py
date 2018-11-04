def convert(ip):
    ip = str(ip)
    list_of_octed = ip.split(sep=".")
    power = 4
    total = 0
    for i in list_of_octed:
        power -= 1
        total += int(i)*(256**power)
    return total

test = convert("10.132.231.3")
print(test)
