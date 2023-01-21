#Write your code below this row 👇
F = "Fizz"
B = "Buzz"

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(F + B)
    elif i % 3 == 0:
        print(F)
    elif i % 5 == 0:
        print(B)
    else:
        print(i)
