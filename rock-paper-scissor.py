print("Rock...")
print("Paper...")
print("Scissors...")

player1 = input("(enter Player 1's choice): ")
player2 = input("(enter Player 2's choice): ")

print("Shoot!")

if player1 == "Rock" and player2 == "Paper":
	print("Player 2 wins!")
elif player1 == "Rock" and player2 == "Scissors":
	print("Player 1 wins!")

elif player1 == "Paper" and player2 == "Rock":
	print("Player 1 wins!")
elif player1 == "Paper" and player2 == "Scissors":
	print("Player 2 wins!")

elif player1 == "Scissors" and player2 == "Rock":
	print("Player 2 wins!")
elif player1 == "Scissors" and player2 == "Paper":
	print("Player 1 wins!")

else:
	print("Draw!")
