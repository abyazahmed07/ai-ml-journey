# student_info_manager_v2.py

def get_student_info():
    student = {
        "name": input("Enter name: "),
        "age": int(input("Enter age: ")),
        "cgpa": float(input("Enter CGPA: "))
    }
    student["university"] = "UCSI"
    return student


def classify_student(cgpa):
    if cgpa >= 3.50:
        return "Excellent"
    elif cgpa >= 3.00:
        return "Good"
    else:
        return "Needs Improvement"


def display_student(student):
    print("\n--- STUDENT INFORMATION ---")
    for key, value in student.items():
        print(f"{key}: {value}")


student = get_student_info()
display_student(student)
classification = classify_student(student["cgpa"])
print(f"\nClassification: {classification}")