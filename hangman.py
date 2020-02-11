from random import *


#function to input a word to play with

def input_word():
	chosen_word = input("Enter a word between 3 and 7 letters...\n")
	if len(chosen_word) < 3 or len(chosen_word) > 7:
		print("Not a valid word...\n")
		input_word()
	else:
		print("The word you have chosen is {0} charachters long".format(len(chosen_word)))
		return chosen_word
  
def game(word):
	board = []
	for i in word:
		board.append("_")
	print(board)
	#return board
	guesses_remaining = 10
	while guesses_remaining > 0:
		guessed_letters = []
		letter = input("Guess a letter!\n")
		print("Guessed Letter: {0}".format(guessed_letters))
		if len(letter) > 1 or len(letter) < 1:
			print("Invalid Guess! Try Again!")
		elif letter in guessed_letters:
			print("You already guessed that letter")
		else:
			guessed_letters.append(letter)
			for i in range(len(word)):
				if word[i] == letter:
					print("You guessed a letter correctly")
					board[i] = word[i]
			for i in board:
				check = ""
				new_check = check + i
				check = new_check
				if check == word:
					print("You Win!")
					guesses_remaining = 0
				else:
					print("Keep Going!\n")
		guesses_remaining -= 1
	print("Game Over!")
					
					
	
game("wotrd")


#calling the functions to play the game.
  
#game(input_word())