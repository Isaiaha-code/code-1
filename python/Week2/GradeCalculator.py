# Prompt the user for a number grade between 1 and 100
grade = int(input("Enter your numeric grade (1–100): "))

# Determine the letter grade using if/elif/else statements
if grade >= 90:
    print("You got an A.")
elif grade >= 80:
    print("You got a B.")
elif grade >= 70:
    print("You got a C.")
elif grade >= 60:
    print("You got a D.")
else:
    print("You got an F.")
