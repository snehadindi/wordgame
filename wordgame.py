import random
print("Hey! This is a word guessing game, Top 10 Famous Artists/Painters edition.")
print("Are you into old paintings, like I am? Then how well do you know your artists???")
chances = 15
print("The rules are simple, there is a list of 10 famous artists of all time. The computer will choose a name of the artist and you have to guess it by entering a random alphabet. If the alphabet is in the word to be guessed you will be prompted to proceed to guess the next alphabet until you guess it correctly. If not, you will get a chance to try again until you run out of chances. You will be given 15 chances. So use them wisely!!")

liswords = {"vangogh", "michelangelo", "picasso", "monet", "rembrandt", "vermeer", "watteau", "munch", "delacroix", "seurat"}
print("Let the guessing begin *drumroll* ;)")
words = list(liswords)
guessed = ""

ans = random.choice(words)
print("_ " * len(ans))  # print initial blanks

while chances > 0:
    count = 0
    for char in ans:
        if char in guessed:
            print(char, end=" ")
        else:
            print("_", end=" ")
            count += 1

    if count == 0:
        print("\n Righty-right! You guessed the word: " + ans)
        break

    print()
    guess = input("Your guess: ")

    if guess in guessed:
        print("Uh-oh! Seems like you have already guessed that letter.")
        continue

    guessed += guess

    if guess not in ans:
        chances -= 1
        print(f"Wrong guess! You have {chances} chances left.")

if chances == 0:
    print(f"Oopsies! You ran out of chances. The word was: {ans}")