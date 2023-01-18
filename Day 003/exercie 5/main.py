# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name2 = input("What is their name? \n")
name1 = input("What is your name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

love_score_true = 0
love_score_love = 0
total_love = 0
for t in "true":
    love_score_true += (name1 + name2).lower().count(t)
for l in "love":
    love_score_love += (name1 + name2).lower().count(l)
total_love = int(f"{love_score_true}{love_score_love}")
if total_love < 10 or total_love > 90:
    print(f"Your score is {total_love}, you go together like coke and mentos.")
elif total_love >= 40 and total_love <= 50:
    print(f"Your score is {total_love}, you are alright together.")
else:
    print(f"Your score is {total_love}.")
