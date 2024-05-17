def calculate_average_grade():
    student_name =input("Please enter your name: ")
    print(f"Student: {student_name}")

    math_score = float(input("Enter math score: "))
    print(f"Math: {math_score}")
    science_score = float(input("Enter science score: "))
    print(f"Science: {science_score}")
    english_score = float(input("Enter English score: "))
    print(f"English: {english_score}")

    average_grade = float((math_score + science_score + english_score) / 3.0)
    print("Average Grade:", average_grade)
    return student_name, average_grade

if __name__ == '__main__':
    student_name, average_grade = calculate_average_grade()

    print(f"{student_name}'s average grade is {average_grade:.2f}.")