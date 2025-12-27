###..Rock_Paper_Scissor.project

"""
Workfolw of project: 

1- input from user(Rock,Paper,Scissor)
2- computer choice (computer will choose randoly no conditionally)
3- Result print


Case :  ( Soo What It Is The Logic OF Our  Prject..)

A- Rock
Rock == Rock = Tie
Rock == Paper = Paper Win
Rock == Scissor = Rock Win

B- Paper
Paper == Paper =  Tie
Paper == Rock = Paper win
Paper ==  Scissor = Scissor Win

C-Scissor
Scissor == Scissor = Tie
Scissor == Rock = Rock Win
Scissor== Paper = Scissor Win

"""

import random                                                          # Import the random module to generate computer's random choice
move_list=["Rock","Paper","Scissor"]                                   # List of possible moves in the game
while True:                                                            # Start an infinite loop to keep the game running

 user_choice=input("Enter your move = ")                               # Get user's move as input
 user_choice = user_choice.capitalize()                                # Convert first letter to uppercase to match list items (e.g., "rock" becomes "Rock")

 computer_choice=random.choice(move_list)                              # Computer randomly selects one move from the list

 print(f"user choice ={user_choice},Computer Choice={computer_choice}")            # Display both choices

 if user_choice == computer_choice :              # index.user_0                              # Check if it's a tie (both chose same)
         print("Both choose same,Match Tie")
 elif user_choice =="Rock":                       #.index.user_1                               # If user chose Rock     
    if computer_choice == "Paper":                                                 # Check if computer chose Paper (Paper beats Rock)
        print("Paper covers Rock, Computer Win")                                   # Otherwise computer must have chosen Scissor (Rock beats Scissor)
    else:
        print(" Rock smashes Scissor,You win")
 elif user_choice =="Paper":                      #.index.user_2                                      # If user chose Paper          
    if computer_choice =="Scissor":                                               # Check if computer chose Scissor (Scissor beats Paper)
        print(" Scissor cuts paper, Computer Win")                                # Otherwise computer must have chosen Rock (Paper beats Rock)
    else:
        print("Paper covers Rock,You win")
 elif user_choice =="Scissor":                      #.index.user_3      
    if computer_choice=="Rock":
        print("Rock smash Scissor,Computer Win")
    else:
        print("Scissor cuts Paper,You win")
 else:                                                                         # If user entered something invalid (not Rock, Paper, or Scissor)
    print("Only form this  choice! Choose Rock, Paper, or Scissor")


 play_again=input("Press enter to continue or type 'quit' to exit:")           # Ask user if they want to play again or quit
 if play_again=="quit":
    print("Game over ! Thank you for playing ")   
    break                                                                      # Break out of the while loop to end the game


        

# Breaking it down:
# When you choose PAPER:
# Possibility 1: Computer chose SCISSOR → Computer wins
# Possibility 2: Computer chose ROCK → You win
# Possibility 3: Computer chose PAPER → Already handled as TIE in first if
# So in the else part:
# It's NOT scissor (that's in the if)
# It's NOT paper (that would be a tie, already handled)
# Therefore, it MUST be rock!
    
    
        
        





