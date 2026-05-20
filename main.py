import math_util
import math
import random

print(math_util.add(5, 3))
print(math_util.subtract(5, 3))
print(math_util.multiply(5, 3))
print(math_util.divide(5, 3))

print(math.sqrt(16))
print(math.pi)

print(random.randint(1, 10))


import gradh_util

marks = []
n = int(input("Enter number of students: "))

for i in range(1, n + 1):
    num1 = int(input("Enter the marks: "))
    marks.append(num1)

avg = gradh_util.calculate_avg(marks)
grade = gradh_util.get_grade(avg)

print("Average Marks:", avg)
print("Grade:", grade)