# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = weight / height**2
str1 = "Your BMI is "
if bmi <= 18.5 :
    print(str1 + str(round(bmi)) + ", you are underweight.")
elif bmi <= 25:
    print(str1 + str(round(bmi)) + ", you have a normal weight.")
elif bmi <= 30:
    print(str1 + str(round(bmi)) + ", you are slightly overweight.")
elif bmi <= 35:
    print(str1 + str(round(bmi)) + ", you are obese.")
else:
    print(str1 + str(round(bmi)) + ", you are clinically obese.")

