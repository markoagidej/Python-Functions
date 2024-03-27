#Task 1: Code a function to calculate the average grade.

grade_list = [54, 82, 97, 100, 10, 73, 61, 24, 92, 84]

def average_grade(list):
    return sum(list)/len(list)

class_average = average_grade(grade_list) # Expected 67.7
print(class_average)

#Task 2: Implement a function to find the highest and lowest grade.

def top_bot_finder(list):
    print("The top grade of the class is " + str(max(grade_list)))
    print("The bottom grade of the class is " + str(min(grade_list)))

top_bot_finder(grade_list)

#Task 3: Create a feature that categorizes grades into letter grades (A, B, C, etc.).

grades_a = []
grades_b = []
grades_c = []
grades_d = []
grades_f = []

for grade in grade_list:
    if grade >= 90:
        grades_a.append(grade)
    elif grade >= 80:
        grades_b.append(grade)
    elif grade >= 70:
        grades_c.append(grade)
    elif grade >= 60:
        grades_d.append(grade)
    else:
        grades_f.append(grade)

print("\"A\" Grades: " + str(grades_a))
print("\"B\" Grades: " + str(grades_b))
print("\"C\" Grades: " + str(grades_c))
print("\"D\" Grades: " + str(grades_d))
print("\"F\" Grades: " + str(grades_f))