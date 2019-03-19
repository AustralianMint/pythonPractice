#Working with calling list items

games = ["Far Cry 4", "Division", "age of empires 2  "]

print(games[0].title() + " is my favorite game!")
print(games[1].title() + " is my favorite game!")
print(games[2].strip() + " is my favorite game!")

#insert @ end
games.append("Diblo 3")
print(games)

#insert anywhere
games.insert(0, "hopscotch")
games.insert(1, "tag")
print(games)

#delet item
del games[2]
print(games)

#pop last item of list into new var
popped_game = games.pop(1)
print("Your latest purchase was: " + popped_game)

print(games.reverse())



