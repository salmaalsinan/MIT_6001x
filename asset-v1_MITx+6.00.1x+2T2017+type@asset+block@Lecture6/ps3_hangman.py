# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for l in secretWord:
        if l not in lettersGuessed:
            return False
    return True   



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    word = []
    for l in secretWord:
        if l in lettersGuessed:
            word.append(l)
        else:
            word.append('_')
        
    return ' '.join(word)


import string
str= string.ascii_lowercase

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    letters=[]
    for j in str:
        if j not in lettersGuessed:
            letters.append(j)
    return ' '.join(letters)
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print('Hi, welcome to hangman !!')
    print('The secret word I am thinking of is', len(secretWord),'letters long !')
    
    mistakes =0
    lettersGuessed=[]
    
    while 8-mistakes >0:
        if isWordGuessed(secretWord, lettersGuessed)== True:
            print('Cool you guessed right, ding ding you win')
            break
        else:
                print('so far you have', 8 - mistakes, 'guesses left.')
                print('Available letters:', getAvailableLetters(lettersGuessed))
                l = input('Guess a letter').lower()
                if l in secretWord and l not in lettersGuessed:
                    lettersGuessed.append(l)
                    print('Good job',getGuessedWord(secretWord, lettersGuessed))
                
                elif l in lettersGuessed:
                    print('oopps, you already guessed that',  getGuessedWord(secretWord, lettersGuessed))
               
                elif l not in secretWord:
                    print('no that letter is not in secret word',getGuessedWord(secretWord, lettersGuessed))
                    lettersGuessed.append(l)
                    mistakes +=1
        if 8-mistakes ==0 :
                print('sorry you are out of guesses, the secret word was' , secretWord)
                break
       
        else:
            continue
 






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

 #secretWord = chooseWord(wordlist).lower()
 #hangman(secretWord)
