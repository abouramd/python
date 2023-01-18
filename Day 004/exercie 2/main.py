import random
# Split string method
test_seed = int(input("Creat a seed number: "))
random.seed(test_seed)
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

print(names[random.randint(0, len(names) - 1)] + " is going to buy the meal today!")

