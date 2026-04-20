import random
num=random.randint(1,9)
chances=0
while chances < 5:
	chances=chances+1
	guess=input()
	if guess == str(num):
		print("YOU WON")
		break
if not chances < 5:
	print("You lose, "+"the number was "+str(num))