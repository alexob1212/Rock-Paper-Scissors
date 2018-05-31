import random

print("Rock...")
print("Paper...")
print("Scissors...")

player1 = input("(enter Player 1's choice): ")

print("Shoot!")

computer = random.randint(0, 2)

# 0 = "Rock"
# 1 = "Paper"
# 2 = "Scissors"

if player1 == "Rock":
	if computer == 1:
		print("Computer wins!")
	elif computer == 2:
		print("Player 1 wins!")

elif player1 == "Paper":
	if computer == 0:
		print("Player 1 wins!")
	elif computer == 2:
		print("Computer wins!")


elif player1 == "Scissors":
	if  computer == 0:
		print("Computer wins!")
	elif computer == 1:
		print("Player 1 wins!")


elif player1 == computer:
	print("Tie!")

else:
	print("Error.")
