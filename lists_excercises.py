#Challanges regarding lists.
#'lists.py' as practice field.

guests = ['Mikel', 'Oliver', 'Nikki', 'Liam']

#personal invites
print(guests[0] + ":" + "\n I would love to have you at my birthday party!")
print(guests[1] + ":" + "\n I'd be sad if you didn't come to my Birthday")
print(guests[2] + ":" + "\n Awe bra! Pull through fo sho. Let's JOOOOL")
print(guests[3] + ":" + "\n it wouldn't be a party without you.\n")

#remove guest from list and state this.
popped_guests = guests.pop(2)

print(popped_guests + " could sadly not make it.")

print(guests)

#Add more guests
guests.insert(0, 'Andrew')
guests.insert(2, 'Herr Jeschke')
guests.append('Melanie')
print("\n I added more guests!")
#Sort guests alphabetically
print(sorted(guests))
print("\n Sadly, I can now only invite two people to the party... ")

#Removing/ notifying people they have been kicked
print(guests.pop(0) + ", apologies, you didn't make the cut...")
print(guests.pop(0) + ", apologies, you didn't make the cut...")
print(guests.pop(0) + ", apologies, you didn't make the cut...")
print(guests.pop(0) + ", apologies, you didn't make the cut...")
print(guests)

#Del last people from list leaving it empty
del guests[0]
del guests[0]
print(guests)

