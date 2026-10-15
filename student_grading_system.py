# Python program to calculate percentage and grade

# Input marks for five subjects
sub1 = float(input("Enter marks for Subject 1: "))
sub2 = float(input("Enter marks for Subject 2: "))
sub3 = float(input("Enter marks for Subject 3: "))
sub4 = float(input("Enter marks for Subject 4: "))
sub5 = float(input("Enter marks for Subject 5: "))

# Calculate total and percentage
total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = total / 5

# Display percentage
print("\nPercentage:", percentage, "%")

# Determine grade using if...else
if percentage >= 75:
    print("Grade: Distinction")
elif percentage >= 65:
    print("Grade: I Class")
elif percentage >= 40:
    print("Grade: II Class")
else:
    print("Grade: Fail")
