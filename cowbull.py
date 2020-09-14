import random
def game(num):
	number=[random.randint(0,9) for x in range(num)]
	count=0
	print("Please guess 4digit number:")
	
	while True:
		count+=1
		print("-------guess: "+str(count)+"--------")
		
		run=True
		while run:
			try:
				guess=[int(x) for x in str(input())]
				if len(guess)==num:
					run= False
				else:
					print("Please !!! Enter "+str(num)+"-digit number.")
			except Exception:
				print("Please!!! Enter valid "+str(num)+"-digit number.")

		
		if guess==number:
			print("You won :) ")
			print("It took you "+str(count)+"guesses")
			break
		else:
			cow=0
			bull=0
			
			for i in range(0,num):
				if number[i]==guess[i]:
					print(str(guess[i])+" is correct at correct position.")
					cow+=1
				elif guess[i] in number:
					print(str(guess[i])+" is correct but at wrong place")
					bull+=1
			print("cow:"+str(cow)+"bull:"+str(bull))
			print("Again enter your guesses")

game(4)
