import random
word=['potato','apple','watermelon','pomegranate']
lives=6
chosen=random.choice(word)
print(chosen)
word1=[]
for i in range(len(chosen)):
    word1+='_'
print(word1)
game=False
while not game:
    guess=input("guess a letter:").lower()
    for j in range(len(chosen)):
        letter=chosen[j]
        if letter == guess:
            word1[j]=guess
    print(word1)
    if guess not in chosen:
        lives-=1
        if lives==0:
            game=True
            print('you loose')
    if '_' not in word1:
        game=True
        print("you win")
