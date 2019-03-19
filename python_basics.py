#def suggest(product_idea):
#    if len(product_idea) < 3:
#        raise ValueError("The entered name is too short... ")
#    return product_idea + "inator"

def editor(name_of_person):
    try:
        name = str(input("Enter a name: "))
    except ValueError:
        print("The entered title is too short")
    print(name + "inator")

editor("thomas")
