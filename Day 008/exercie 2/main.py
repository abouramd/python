#Write your code below this line 👇

def testprime(num, i):
    if num == i or num == 1 or num == 2:
        return True
    if num <= 0 or num % i == 0:
        return False
    return testprime(num, i + 1)

def prime_checker(number):
    if testprime(number, 2) == True:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



