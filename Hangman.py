import random
import HangmanPics
import urllib.request
import urllib.parse
import os

#Instanciate variables
word = ''
wordLen = -1
livesRemaining = 6


#Download the words into a list
url = 'https://pastebin.com/raw/7KJNUqax'
f = urllib.request.urlopen(url)
words = f.read().decode('utf-8')
words = words.split("\n")



def startGame():
    #Instanciate game vars
    win = False
    livesRemaining = 6
    guessedLetters = []
    correctLetterInedxies = []

    #Get random word
    word = random.choice(words).strip()

    #Get word length
    wordLen = len(word)

    #While the user has lives
    while livesRemaining != 0:
      
      #Print there progress with the word
      print("The word is: " + getWordWithCorrectLetters(word, correctLetterInedxies) + "\n")

      #Tell them how many lives they have
      print(f"You have {livesRemaining} lives remaining!\n")

      #Prompts for a letter input
      letterInput = input("Guess a letter: ").strip().lower()

      #Clear
      os.system('cls' if os.name == 'nt' else 'clear') 
      
      #Check if the user pressed enter to show the letters they guessed already
      if (letterInput == ""):
        print("You have currently guessed the following letters: " + str(sorted(guessedLetters)).replace("'", ""))
      else:
        #Verify the input
        if not verifyInput(letterInput):

          #Invalid letter
          
          print(f"{letterInput} is not a valid letter.")

          #Loop again
          continue

        #If the letter has not been guessed
        if not letterInput in guessedLetters:

          #Add it to the guessed list
          guessedLetters.append(letterInput)
          

          isInWord = checkLetterInWord(word, letterInput)

          #isInWord = false in this case
          if not  isInWord:
            os.system('cls' if os.name == 'nt' else 'clear') 
            #Tell the user the letter is not in the word
            print(f"The character {letterInput} is not in word.")

            #Remove a life
            livesRemaining -= 1

            #Print the image
            print('\t\t' + HangmanPics.pics[(6 - (livesRemaining + 1))])
          else:
            #In this else case the function returned a list of index's at which the guessed letter appear in the word
            os.system('cls' if os.name == 'nt' else 'clear') 
            #Loop through these indexs
            for index in isInWord:

              #Check if that index has already been appended to the list for found letters
              if not index in correctLetterInedxies:

                #Since it has not, append it
                correctLetterInedxies.append(index)

            #If the length of the array matches the wordLen the user found all the letters
            if len(correctLetterInedxies) == wordLen:

              #User won
              win = True
              break

        else:
          os.system('cls' if os.name == 'nt' else 'clear') 
          #Letter has been guessed
          print("You have already guessed that letter, please guess another letter.\nTo see the letters you have already guessed press [ENTER]\n")

    #Check if the user won
    if win:
      #Tell the user they won
      print("\nYou won!")
    else:
      #Tell the user they lost
      print("YOU LOST! The word was:", word)

    playAgainCheck()


#This will verify the user input
def verifyInput(val):

  #Check the length is only 1 and its not a number
  if len(val) == 1 and not val.isnumeric():

    #If this is the case we can return true
    return True
  else:

    #Else return false
    return False



#This function will take the word and correct letter index's that the user has guessed
#and return what will be outputted to the user

#example: 

# If the function is called as so getWordWithCorrectLetters('apple', [0, 3])
# It will return 
# a _ _ l _ _

def getWordWithCorrectLetters(word, indexArr):

  #Create the blank word AKA converting "apple" to "_ _ _ _ _"
  blank = "_" * len(word)

  #Convert this to a list of each character so we have access to index's
  charList = list(blank)

  #Instanciate a var for the output
  newWord = ''

  #Check if there are correct index's passed in with the function
  if len(indexArr) > 0:

    #Since there are correct index's we will loop through them
    for correctLetterIndex in indexArr:

      #Replace the underscore at the index that is correct with the letter at the index from the word
      charList[correctLetterIndex] = word[correctLetterIndex]

    #Rebuild the list into a string
    newWord = ''.join(charList)

    #Return the string AKA "a _ _ l _"
    return(newWord)
  else:

    #No correct letters were passed, return the blank string aka "_ _ _ _ _"
    return(blank)
  

def checkLetterInWord(word, letter):

  #Instanciate a return value for the function


  #Loop through each char
  for eachLetter in word:

    #Check if the letter is in the word
    if eachLetter == letter:

      #Letter is in the word, we will instead return all the indexies that the letter appears at
      return getLetterIndeiesFromWord(word, letter)
      
  #Letter is not in the word, return false
  return False

def getLetterIndeiesFromWord(word, letter):
  #This will return a list with all the indexs for that letter that are in the word
  return [pos for pos, char in enumerate(word) if char == letter]



def playAgainCheck():
  #Var to detect play again
  askUntilBool = False

  #While its false
  while askUntilBool == False:

    #ask 
    startNewGame = input("\nWould you like to start a new game? (Yes or No)")


    #Check if yes
    if startNewGame.lower() == 'yes' or startNewGame.lower() == 'y':

      #Break out of loop
      askUntilBool = True

      #Clear
      os.system('cls' if os.name == 'nt' else 'clear')  
      
      #Start new game
      startGame()

    #no
    elif startNewGame.lower() == 'no' or startNewGame.lower() == 'n':
      #clear
      os.system('cls' if os.name == 'nt' else 'clear') 
      menu()
    else:
      print("Unknown input, please try again")

def menu():
  #Get user command
  command = input("Enter a command (Type 'HELP' for a list of commands): \t").strip().lower()

  #Check if command is clear
  if command == 'clear' or command == 'cls':
    
    #Clear the console
    os.system('cls' if os.name == 'nt' else 'clear')      
    
    #Go back to main menu
    menu()

  #Check for newgame command
  elif command == 'newgame':
      
    #Clear
    os.system('cls' if os.name == 'nt' else 'clear')  

    #Start the game    
    startGame() 

  #Check if command is help
  elif command == 'help':
      
      #Print help menu
      print('\n\n\tCommand List: \n\tnewgame: Start a new game\n\tclear: Clear the console\n\texit: Exit the game\n\tabout: More info on the origin of the project\n\n')
      
      #Go back to main menu
      menu()

  #check if command is exit
  elif command == 'exit':
      
      #Exit the game
      os._exit(0)

  #Check if the command is about
  elif command == 'about':
      
      #Print about message
      print("\n\tHangman V2 is developed by me, Andrew Abercrombie. I got bored one day and realized \n\tmy old version of this was trash. I have revamped how the code works to ensure\n\tmore common programming practices are being utilized.\n\n\tYou can check out the old version here: https://github.com/AndrewAbercrombie/HangmanPY\n\n")
      
      #Go back to main menu
      menu()
  else:
      #Clear
      os.system('cls' if os.name == 'nt' else 'clear') 

      #Unknown Command
      print("\nUnknown command. Type HELP for a list of commands..\n\n")

      #Go back to main menu
      menu()

def main():
  #Clear
  os.system('cls' if os.name == 'nt' else 'clear')  

  #Show welcome message
  print("Welcome to Hangman V2 - Developed By Andrew Abercrombie \n\n\n")

  #Show menu
  menu()

#Start main function
main()
