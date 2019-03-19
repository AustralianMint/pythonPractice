import sys

MASTER_PASSWORD = "opensesame"

password = input("plz enter the super secret password: ")
attempt_counter = 1

while password != MASTER_PASSWORD:
    password = input("Incorrect password. Plz try again: ")
    attempt_counter += 1
    if attempt_counter > 3:
        sys.exit("Waayyyy to many incorrect password attemtps... ")
        
print("Correct password! ")
