import random
print("Welcome to the Hangman Game.")
wordslist=["ahmad","camel","car","bike","supreme"]
word=random.choice(wordslist)
n=1
while n<=len(word):
    print("_",end=" ")
    n+=1
guess=input("\nGuess the letter in the word")
wordlist=list(word)
print(wordlist)
n=0
length=0
while n<len(word):
    if guess==wordlist[n]:
        print(wordlist[n],end=" ")
        length+=1
    else:
        print("_",end=" ")
    n+=1


