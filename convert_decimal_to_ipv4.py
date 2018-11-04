def convert(number):
    number = int(number)
    first_octed = number // 256**3
    # print(first_octed)
    second_octed = (number % 256**3) // 256**2 
    # print(second_octed)
    third_octed = ((number % 256**3) % 256**2) // 256
    # print(third_octed)
    fourth_octed = ((number % 256**3) % 256**2) % 256
    # print(fourth_octed)
    return str(first_octed)+"."+str(second_octed)+"."+str(third_octed)+"."+str(fourth_octed)

test = convert(176482051)
print(test)
