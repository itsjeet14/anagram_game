import random
# calling txt file
f = open("word.txt", 'r')
# reading txt file
r = f.readline()
# reading only one word
words = r.split(",")

# creating jumble word
word = random.choice(words)
jumble = ''.join(random.sample(word, len(word)))

# chances to attempt
chance = 3
while chance != 0:
    print("Jumble Word: ",jumble)
    guess = input("Enter Answer: ")
    if guess == word:
        print("Correct Answer!!")
        print()
        break
    else:
        chance -= 1
        print()
        print("Attempt left: ",chance)
     
else:
    print("You Lose!!")
    print("Correct Answer: ",word)
print()
print("Thank you for playing!")
