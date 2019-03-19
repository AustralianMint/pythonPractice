string = "Hey there, I am a string!"
rstr = "I love geeksforgeeks"
name = input("Enter your name: ")
# Printing the original string
print ("The original string is : \n", rstr, "\n")

# Printing the right aligned string
# with "-" padding
print ("The right aligned string is : ")
print (rstr.rjust(40, '-'))
print(string.center(40, '~'))
print(name.center(40, '*'))

#printing lenght of string.
print(len(string))

## The specified padding has to be longer than the given stringself.
## Otherwise it won't show.
