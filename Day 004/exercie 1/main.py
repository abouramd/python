import random
test_seed = int(input("Creat a seed number: "))
random.seed(test_seed)
#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲

r = round(random.random())

if r == 1:
    print("Heads")
else:
    print("Tails")



