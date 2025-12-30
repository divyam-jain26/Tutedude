std_marks = {
    "Alice": 85,
    "Bob": 65,
    "Charlie": 90,
    "David": 20,
}

try:

    user = input("Enter the student's name: ").capitalize()
    if user in std_marks:
        print(f"{user}'s marks: {std_marks[user]}")
    else:
        print("Student not found.")

except:
    print("Unexpected error occured.")  