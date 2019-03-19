#Manipulating strings.
#Adding them together/ defining methods to print output diffirently

name = str(input("Enter your name: "))
quote = "'you never know till you know, you know?'"
greeting = "Hello {}, would you like to learn some code today?".format(name)

print("Thomas - the wise and all mighty - once said " + quote)

print(greeting)
print(name.upper())
print(name.lower())
print(name.title())
print(name.strip())
