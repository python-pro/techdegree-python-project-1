#BRR
#MSAW

name = input("What's your name? ")

# TODO: Ask the user by name if they understand Python while loops
understand= input("{}, do you understand while loops in python?\nEnter yes/no  ".format(name))


# TODO: Write a while statement that checks if the user doesn't understand while loops
# TODO: Since the user doesn't understand while loops, let's explain them.
# TODO: Ask the user again, by name, if they understand while loops.

while understand.lower()!='yes':
	print("Well {}, A while loop statement in Python programming language repeatedly executes a target statement as long as a given condition is true.".format(name))
	understand = input("{}, do you understand while loops in python now?\nEnter yes/no  ".format(name))
  
# TODO: Outside the while loop, congratulate the user for understanding while loops
print("Congratulations, {} you've achieved a lot then".format(name))
