#For Loop practice.
#The value of the list gets saved in the first 'name' you specify in the loop.

counter = 1
magicians = ['thomas', 'shrek', 'donkey']
compliment = ", that was a great trick!"

for person in magicians:
	print("{}st ".format(counter)+ "\t" + person.title() + compliment)
	counter += 1
print("\n\t Thank you all for attending!")
