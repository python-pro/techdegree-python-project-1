import random
	
	
def start_game():
	print("""
					---------------------------------------------------
	
						Welcome to the number guessing game
	
					---------------------------------------------------
	""")
	

	solution=random.randint(1,10)
	print(solution)
	
	
	attempts = []
	def attempt(guess):
		attempts.append(guess)
		
	
	while True:
		
		prompt=int(input("Pick a number between 1 and 10  "))
		attempt(prompt)	
	
		if prompt < solution:
			print("It is higher")
		
		elif prompt > solution:
			print("It is lower")
		
		else:
			print("""
		~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		
		You've got it
		
		~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		""")
			print("""
		^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
		
		It took you {} attempts to guess the correct number
		
		^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^""".format(len(attempts)))
		
			break
				
			
def play_again():
	while True:
		
		play_again=input("""


Would you like to play again? [y]es/[no]   """)
		play_again=play_again.lower()
		if play_again == 'y':
			start_game()
			
		elif play_again == 'n':
			print("""
		==========================================
		
				THE GAME IS OVER THEN
				
		==========================================
		""")
			break
		else:
			print("                					Excuse me?            ")
			print("				   Please say yes or no, pressing 'y' or 'n' accordingly          ")


	
  

start_game()



play_again()
