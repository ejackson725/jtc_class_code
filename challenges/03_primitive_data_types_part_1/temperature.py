# 03_primitive_data_types_part_1 
#covert 100 degees fahrenheit tp celcius
x = 100
celsius_100 = (x-32)*(5/9)


print(celsius_100)

print(type(celsius_100))

#Convert a temperature of 0 degrees fahrenheit to celcius
#save this to a variable called celsius_0, and print out the value
print("question2")

x = 0
celsius_0 = (x-32)*(5/9)
print(celsius_0)
print(type(celsius_0))


#Convert a temperature of 34.2 degrees fahrenheit to celsius
#did it in all in one print statment withouth saving any variables
print("question3")
print((34.2-32)*(5/9))


#convert a temperature of 5 degrees celsius to fahrenheit
print("question4")
print(5*(9/5)+32)

#I determine what was hotter 30.2 degrees celsius or 85.1 fahrenheit
print("question5")
print(30.2*(9/5)+32)

a = 86.36
b = 85.1
if a > b:
	print("a is hotter than b")

