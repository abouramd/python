# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

l = 0
s = 0

for i in student_heights:
  l += 1
for i in student_heights:
  s += i

print(round(s / l))


