name = str(input("Please enter your name: "))
understanding = str(input("Ok {}, Do you understand While Loops? (yes/ no)".format(name)))
explanation = """In most computer programming languages, a while loop is a control flow statement that allows code to be executed repeatedly based on a given Boolean condition.
The while loop can be thought of as a repeating if statement."""

while understanding == "no":
    print("ok {}".format(name), explanation)
    understanding = str(input("Do you understand loops now? (yes/ no)"))

if understanding == "yes":
    print("Great, {}! I'm glad you understand!".format(name))
    
    
    
