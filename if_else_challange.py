#This is the current working solution to the problem: Python If_Else on https://www.hackerrank.com/challenges/py-if-else/problem

number = int(input())
odd_even = number % 2

if odd_even != 0:
    print("Weird")
elif odd_even == 0 and number in range(2, 6):
    print("Not Weird")
elif odd_even == 0 and number in range(6, 21):
    print("Weird")
elif odd_even == 0 and number > 20:
    print("Not Weird")
else:
    print("Ayt fokol happened!")

