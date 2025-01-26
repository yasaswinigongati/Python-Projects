# import random
# l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
#  'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
# n=['0','1','2','3','4','5','6','7','8','9']
# s=['$','%','&','*','#','+','!','(',')','@']
# print("welcome to password generator")
# letters=int(input("no of letters to be there"))
# numbers=int(input("no of numbers to be there"))
# symbols=int(input("no of characters to be there"))
# password=''
# for i in range(letters):
#     char=random.choice(l)
#     password+=char
# for i in range(numbers):
#     char=random.choice(n)
#     password+=char
# for i in range(symbols):
#     char=random.choice(s)
#     password+=char
# print(password)



import random
l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
n=['0','1','2','3','4','5','6','7','8','9']
s=['$','%','&','*','#','+','!','(',')','@']
print("welcome to password generator")
letters=int(input("no of letters to be there"))
numbers=int(input("no of numbers to be there"))
symbols=int(input("no of characters to be there"))
password_=[]
for i in range(letters):
    char=random.choice(l)
    password_+=char
for i in range(numbers):
    char=random.choice(n)
    password_+=char
for i in range(symbols):
    char=random.choice(s)
    password_+=char
print(password_)
random.shuffle(password_)
print(password_)
password=''
for i in password_:
    password+=i
print(password)

