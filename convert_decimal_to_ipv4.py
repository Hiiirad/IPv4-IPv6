
number = int(input("Please put your number here: "))
# number = 176482051
first_octed = number // 256**3 # khareje ghesmat
# print(first_octed)
second_octed = (number % 256**3) // 256**2 
# print(second_octed)
third_octed = ((number % 256**3) % 256**2) // 256
# print(third_octed)
fourth_octed = ((number % 256**3) % 256**2) % 256
# print(fourth_octed)
print(str(first_octed)+"."+str(second_octed)+"."+str(third_octed)+"."+str(fourth_octed))
