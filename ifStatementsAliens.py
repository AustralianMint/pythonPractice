alien_color = input(str("Enter a color: ")).lower()
savior_mssg = "You spared everybody's lives!"

if alien_color == "red":
    print("This is the RED ship! \nPOINTS: 5")
elif alien_color == "yellow":
    print("This was the YELLOW ship!\nPOINTS: 10")
elif alien_color == "green":
    print("This was the GREEN ship!\nPOINTS: 15")
else:
    print(savior_mssg.center(50, '~'))
