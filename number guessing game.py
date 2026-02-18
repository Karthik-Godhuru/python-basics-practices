import random
secret=random.randint(1,10)
for attempt in range(3):
	guess=int(input("enter the guess number bro: "))
	if secret==guess:
		print("you win bro")
		break
	elif secret>guess:
		pritnt("you are very close")
	else:
		print("you are so far")
else:
	print("game over bro")