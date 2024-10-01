import sys
import random
from colorama import Fore
from art import *
print("_" * 100)
def get_guess():
	while True:
		guess = input("\nGuess a 5 letter word : ").upper()
		if len(guess) == 5 and guess.isalpha():
			return guess.upper()
			break
		else:
			print("Invalid Guess\n")
			print("_" * 100)
def choose_word():
	lines = open('word.txt').read().splitlines()
	word =random.choice(lines)
	return word
list1 = {} 
list2 = {}  
list3 = {}
def compare(guess, answer):
	list1 = {} 
	list2 = {}  

	result = ""
	if guess == answer:
		win=text2art("YOU WIN",font="univers") 
		print(Fore.GREEN + win + Fore.RESET)
	
		sys.exit(0)

	list3 = {}
	for i in range(5):
		if guess[i] == answer[i]:
			list1[i] = guess[i]  
		elif guess[i] in answer and guess[i] not in list1.values():
			list2[i] = guess[i]  
		else:
			list3[i] = guess[i]  
	return list1,list2,list3

def give_feedback(list1, list2, list3,attempts):
    print("\nCorrect letter & index:", list(list1.values()))
    print("Correct letter but wrong index:", list(list2.values()))
    print(str(attempts) + "  attempts left \n")
    print("_" * 100)
def main():
	key = choose_word().upper()
	attempts = 6
	while attempts > 0:
		guess = get_guess().upper()
		attempts = attempts - 1
		print("Answer : " + key)
		l1,l2,l3 = compare(guess,key)
		give_feedback(l1,l2,l3,attempts)
	lose=text2art("YOU LOSE",font="univers") 
	print(Fore.RED + lose + Fore.RESET)
	
try :
	main()
except KeyboardInterrupt:
		print("\n\nCaught Keyboard Intruption! " + Fore.RED + 'Quiting program...\n' + Fore.RESET)
		sys.exit(0)
print("hello")
