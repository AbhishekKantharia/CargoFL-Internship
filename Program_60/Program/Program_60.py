#welcoming the user
name = input("Enter your name: ")
print("Hello, " + name, "Let's play hangman!")

print("So what's your first guess?")

#here we set the edureka
word = "edureka"

#creates an variable with an empty value
guesses = ''

#determine the number of turns
turns = 10

# Create a while loop and check if the number of turns are more than zero
while turns > 0:         

    # make a counter that starts with zero. Just a flag.
    failed = 0             

    # for every character in secret_word    
    for char in word:      

    # Print if the character is in the players guess
        if char in guesses:    
          print(char)
        else:
   
        # if not found, print a dash
            print("_")
       
        # and increase the failed counter with one. 
            failed += 1    

    # if failed is equal to zero print You Won
    if failed == 0:        
        print("You won")

    # exit the script
        break              

    print()
    # ask the user go guess a character
    guess = input("guess a character:") 

    # set the players guess to guesses
    guesses += guess                    

    # if the guess is not found in the secret word
    if guess not in word:  
 
     # No. of turn decreases: turns counter decreases with 1 (now 9)denoting wrong guess
        turns -= 1        
        print("Wrong Guess")    
 
    # how many turns are left
        print("You have", + turns, 'more guesses')  
    # if the turns are equal to zero. User has exhausted all the 10 moves.
        if turns == 0:           
    
        # print "You Lose"
            print ("You Lose")