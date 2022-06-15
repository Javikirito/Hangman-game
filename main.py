import random
import time
print("\nWelcome to Hangman game\n")
name = input("Enter your name: ")
print("\nHello " + name + "! Best of Luck!")
time.sleep(1)
print("\nThe game is about to start!\n   Let's play Hangman!\n")
print("---------------------")
time.sleep(1)

def main():
    print("---------------------")
    global word
    word=random.choice(open("/home/cybrosys/Desktop/assignments/hangman/words","r").readline().split())
    print(word)
    global crct
    global words
    words=word.upper()
    crct=word.upper()
    length = len(word)
    global count1
    count1=0
    global already_guessed
    already_guessed=[]
    global display
    display = ['_']*len(word)
    print("length of the word",length," : ",display,"\n")
    hangman()


def play_loop():
    yn=input("do you want to play again? (y/n) : ")
    if yn=='n' or yn=='N':
        print("thanks for playing")
        exit()
    elif yn=='y' or yn=='Y':
        main()
    else:
        print("invalid input\n")
        play_loop()

def hangman():
    global limit 
    global count1
    global display
    global word
    global crct
    global gues
    global already_guessed
    limit=7
    guess = input("Enter your guess : ")
    gues=guess.upper()
    gues = gues.strip()
    if len(gues.strip()) == 0 or gues.isdigit() :
        print("Invalid Input, Try a letter or the word \n")
        hangman()
    elif len(gues.strip())>1 and len(gues.strip())!=len(crct):
        print("Invalid Input, Try a letter or the word \n")
        hangman()
    elif words == gues:
        print("Congrats! You have guessed the word correctly!\n")
        play_loop()

    elif (gues in already_guessed):
        print("already guessed, try another , \n")

    elif gues in words:
        already_guessed.append(gues)
        crct,display=get_letter_position(gues, crct, display)
        print(display,"\n")

    else:
        already_guessed.append(gues)
        count1=count1+1
        if count1 == 1:
            print(
            "      __________     \n "
            "     |         |     \n"
            "      |         |     \n"
            "      |         O     \n"
            "      |             \n"
            "      |               \n"
            "      |              \n "
            "     |                 \n"
            "      |                \n"
            "______|_____       \n")
            print("Wrong guess. " + str(limit - count1) + " guesses remaining\n")

        elif count1 == 2:
            print(
            "      __________     \n "
            "     |         |     \n"
            "      |         |     \n"
            "      |         O     \n"
            "      |         |     \n"
            "      |               \n"
            "      |              \n "
            "     |                 \n"
            "      |                \n"
            "______|_____       \n")
            print("Wrong guess. " + str(limit - count1) + " guesses remaining\n")

        elif count1 == 3:
            print(
            "      __________     \n "
            "     |         |     \n"
            "      |         |     \n"
            "      |         O     \n"
            "      |         |     \n"
            "      |         |     \n"
            "      |              \n "
            "     |                 \n"
            "      |                \n"
            "______|_____       \n")
            print("Wrong guess. " + str(limit - count1) + " guesses remaining\n")

        elif count1 == 4:
            print(
            "      __________     \n "
            "     |         |     \n"
            "      |         |     \n"
            "      |         O     \n"
            "      |        /|     \n"
            "      |         |    \n"
            "      |              \n "
            "     |                 \n"
            "      |                \n"
            "______|_____       \n")
            print("Wrong guess. " + str(limit - count1) + " guesses remaining\n")

        elif count1 == 5:
            print(
            "      __________     \n "
            "     |         |     \n"
            "      |         |     \n"
            "      |         O     \n"
            "      |        /|\     \n"
            "      |         |      \n"
            "      |              \n "
            "     |                 \n"
            "      |                \n"
            "______|_____       \n")
            print("Wrong guess. " + str(limit - count1) + " guesses remaining\n")

        elif count1 == 6:
            print(
            "      __________     \n "
            "     |         |     \n"
            "      |         |     \n"
            "      |         O     \n"
            "      |        /|\     \n"
            "      |         |      \n"
            "      |        /      \n "
            "     |                 \n"
            "      |                \n"
            "______|_____       \n")
            print("Wrong guess. " + str(limit - count1) + " guesses remaining\n")

        elif count1 == 7:
            print(
            "      __________     \n "
            "     |         |     \n"
            "      |         |     \n"
            "      |         O     \n"
            "      |        /|\     \n"
            "      |         |      \n"
            "      |        / \     \n "
            "     |                 \n"
            "      |                \n"
            "______|_____       \n")
            print("Wrong guess. You are hanged!!!\n")
            print("The word was",words)
            play_loop()

    if listToString(display) == words:
        print("Congrats! You have guessed the word correctly!\n")
        play_loop()

    if words == gues:
        print("\nCongrats! You have guessed the word correctly!\n")
        play_loop()
    
    elif count1 != limit:
        hangman()

def get_letter_position(guess, word, display):
    index = -2
    while index != -1:
        if guess in word:
            index = word.find(guess)
            removed_character ='*'
            word = word[:index]+removed_character+word[index+1:]
            display[index] = guess
        else:
            index = -1
     
    return (word, display)

def listToString(s): 
    str1 = ""  
    for ele in s: 
        str1 += ele   
    return str1 

main()
hangman()  
