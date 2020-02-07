#Vowels in Pig Latin Game
vowels = "aeiou"
print("Welcome to Pig Latin Game.\nRemember to press -1 to end game!")

#Loop allows game to keep running untill the user enter -1 to end the game
while True:
    word = input("Please enter any word: ")
    if word == "-1":
        print("Thanks for playing Pig Latin Game")
        break

    #When first word is vowel, append the word with "yay" 
    if word[0] in vowels:
        new_word = word + "yay"
        print (new_word)

    #If otherwise, remove the consonants up until the first vowel and append it to the removed part and "ay"
    else:
        for vowel in vowels:
            w = word.replace(word[0:word.find(vowel)], "")
            newly_formed_word = w + word[0:word.find(vowel)] + "ay"
            print(newly_formed_word)
            break