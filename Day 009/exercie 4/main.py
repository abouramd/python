from os import system
system('cls || clear')


secret_doc = {}

print("Welcome to the secret auction program.")

add_more = True
while add_more:
    name = input("What is your name?: ")
    bid = input("what's your bid?: $")
    secret_doc [name] = bid
    add_more = False
    if input("are there any other bidders? Type 'yes' or 'no'").lower() == "yes":
        add_more = True





