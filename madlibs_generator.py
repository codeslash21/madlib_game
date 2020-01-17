import sys

print('##Mad Libs is a phrasal template word game where one player prompts others for a list of words to substitute')
print('for blanks in a story,before reading the – often comical or nonsensical – story aloud')

# String for the Test:
t1 = "Hi, my name is NAME and I really like to VERB PLURALNOUN. I am also a OCCUPATION at PLACE."
t2 = "PERSON! What is PERSON going to do with all these ADJECTIVE PLURALNOUN? Only a registered OCCUPATION could VERB them."
t3 = "What a ADJECTIVE day! I can VERB the day off from being a OCCUPATION and go VERB at PLACE."

#Words to be replaced:
parts_of_speech1 = ['NAME','PERSON','PRONOUN','PLURALNOUN','NOUN','PLACE','VERB','OCCUPATION','ADJECTIVE','CONJUNCTION','ADVERB']

#Checking if a word in parts_of_speech is a substring of word or not:
def word_in_pos(word,parts_of_speech):
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None

#Play a full game Mad Libs. Player has to replace the words in ml_string which appear in partd_of_speech.
def play_game(ml_string,parts_of_speech):
    replaced = []
    ml_string = ml_string.split()
    for word in ml_string:
        replacement = word_in_pos(word,parts_of_speech)
        if replacement != None:
            user_input = input("This is a: "+replacement+" ")
            word = word.replace(replacement,user_input)

        replaced.append(word)

    replaced = " ".join(replaced)
    return replaced

#Are You want to Plat Now?
s = "Yes"
while s.lower() != "exit":
    # Get User Input OR Not:
    print("Are you want to give the Story? Yes OR No: ")
    if input().lower()=="yes":
        ml_string = str(input("Enter here: "))
        print(play_game(ml_string,parts_of_speech1))
    else:
        print(play_game(t1,parts_of_speech1))
    s = str(input("Are You To Play Again?  Yes OR Exit: "))
