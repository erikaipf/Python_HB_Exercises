def add(num1, num2):
	return num1 + num2

def substract(num1, num2):
	return num1 - num2

def multiply(num1, num2):
	return num1 * num2

def divide(num1, num2):
	return num1 / num2

def modulo(num1, num2):
	return num1 % num2

def power(num1, num2):
	return num1 ** num2

def square(num1):
	return num1*num1

# print add(4,5)

# print substract(5,4)

# print multiply(10,2)

# print divide(30,4.0)

# print modulo(31,2)

# print power(3,3)

# print square(9)

print add(4,5) + substract(9,6)
print add( add(4,5) , substract(9,6) )

print divide(12,2)-60
print substract(divide(12,2),60)

print add(add(1,2),3)

print square(add(1,2))

print divide(modulo(3,4),multiply(9,9))
print multiply(7,add(3,8))
print substract(add(1,2),multiply(3,add(4,5)))

print power(3,add(2,3)) 