places = ['South Africa', 'Hawaai', 'Los Angeles', 'Japan']
numAttending = len(places)
attendingMessage = "There are {} places you'd like to visit!".format(numAttending)

print("unordered:")
print(places)
print("\n")

#Temporarily sort items
print("ordered (not final):")
print(sorted(places))
print("\n")

#Reverse/ re-reverse list
print("reversed")
places.reverse()
print(places)
print("\n")

print("original order")
places.reverse()
print(places)
print("\n")

places.sort()
print(places)
print("\n")

#Reversed perma sort list.
places.sort(reverse = True)
print(places)
print("\n")

print(attendingMessage)







