TICKET_PRICE = 10
tickets_remaining = 100

print("There are {} Tickets remaining!".format(tickets_remaining))

name = (input("What is your name? "))

ticket_demand = int(input("{}, How many tickets would you like? ".format(name)))

total_price = TICKET_PRICE * ticket_demand

confirmation = str(input("Would you like to purchase '{}' tickets for: ${} (yes/ no)".format(ticket_demand, total_price)))


if confirmation == "yes":
    print("Your tickets have been purchased!")
else: 
    print("Alright well fuk u m8")
