student_name = "Jaylen Chavers"  # Replace with your actual name
current_gpa = 2  # Float between 1.0-4.0
study_hours = 25  # Integer (Ex. 25)
social_points = 40  # Integer (Ex. 50)
stress_level = 95  # Integer 0-100

# Display welcome message with starting stats
print(
    f"Welcome {student_name} your starting stats are \nCurrent GPA: {current_gpa}\nStudy Hours: {study_hours}\nSocial Points: {social_points}\nStress Level: {stress_level}")
choice = input(
    """Choose your course load:
    A) Light (12 credits)
    B) Standard (15 credits)
    C) Heavy (18 credits)
    """)
print(choice)
if choice == "A" or choice == "a":
    if current_gpa >= 3.2:
        study_hours = 5
        social_points = 50
        stress_level = 5
        print(
            f"Updated Stats:\nCurrent GPA: {current_gpa}\nStudy Hours: {study_hours}\nSocial Points: {social_points}\nStress Level: {stress_level}")
        print(
            "\n\nYou performed very well if not the best in every class you have ever taken.\nYou became a dentist and paid off your student loans at 65!")

    elif current_gpa >= 2.8:

        current_gpa = 3.1
        study_hours = 15
        social_points = 30
        stress_level = 45
        # Use comparison operators to check GPA and adjust variables
        print(
            f"Updated Stats:\nCurrent GPA: {current_gpa}\nStudy Hours: {study_hours}\nSocial Points: {social_points}\nStress Level: {stress_level}")
        print("\n\nYou performed adequately in every class you have ever taken.\nBecome a Lawyer, work a 9 to 5!")

    else:
        current_gpa = 1.4
        study_hours = 3
        social_points = 75
        stress_level = 99
        # Use comparison operators to check GPA and adjust variables
        print(
            f"Updated Stats:\nCurrent GPA: {current_gpa}\nStudy Hours: {study_hours}\nSocial Points: {social_points}\nStress Level: {stress_level}")
        print("\n\nYou performed poorly in every class you have ever taken.\nGo work contruction!")

elif choice == "B" or choice == "b":
    if current_gpa >= 3.2:
        study_hours = 15
        social_points = 45
        stress_level = 5
        print(
            f"Updated Stats:\nCurrent GPA: {current_gpa}\nStudy Hours: {study_hours}\nSocial Points: {social_points}\nStress Level: {stress_level}")
        print(
            "\n\nYou performed very well if not the best in every class you have ever taken.\nYou became a Lawyer and paid off your student loans at 48!")

    elif current_gpa >= 2.8:

        current_gpa = 2.6
        study_hours = 24
        social_points = 26
        stress_level = 65
        # Use comparison operators to check GPA and adjust variables
        print(
            f"Updated Stats:\nCurrent GPA: {current_gpa}\nStudy Hours: {study_hours}\nSocial Points: {social_points}\nStress Level: {stress_level}")
        print(
            "\n\nYou performed adequately in every class you have ever taken.\nYou are now a Lawyer, at San Francisco Law Group!")

    else:
        current_gpa = 1.1
        study_hours = 6
        social_points = 75
        stress_level = 99
        # Use comparison operators to check GPA and adjust variables
        print(
            f"Updated Stats:\nCurrent GPA: {current_gpa}\nStudy Hours: {study_hours}\nSocial Points: {social_points}\nStress Level: {stress_level}")
        print(
            "\n\nYou performed poorly in every class you have ever taken.\nYour are now a bouncer at a dry night club!")

elif choice == "C" or choice == "c":
    if current_gpa >= 3.2:
        study_hours = 38
        social_points = 10
        stress_level = 78
        print(
            f"Updated Stats:\nCurrent GPA: {current_gpa}\nStudy Hours: {study_hours}\nSocial Points: {social_points}\nStress Level: {stress_level}")
        print(
            "\n\nYou performed very well if not the best in every class you have ever taken.\nYou became a Doctor and paid off your student loans at 26!")

    elif current_gpa >= 2.8:

        current_gpa = 2.7
        study_hours = 30
        social_points = 20
        stress_level = 89
        # Use comparison operators to check GPA and adjust variables
        print(
            f"Updated Stats:\nCurrent GPA: {current_gpa}\nStudy Hours: {study_hours}\nSocial Points: {social_points}\nStress Level: {stress_level}")
        print("\n\nYou barely passed every class you have ever taken.\nC's get degrees right?")

    else:
        current_gpa = .5
        study_hours = 15
        social_points = 0
        stress_level = 110
        # Use comparison operators to check GPA and adjust variables
        print(
            f"Updated Stats:\nCurrent GPA: {current_gpa}\nStudy Hours: {study_hours}\nSocial Points: {social_points}\nStress Level: {stress_level}")
        print(
            "\n\nYou performed poorly in every class you have ever taken.\nYou work at McDonalds as a cashier and have no plans to retire!")

else:
    # Handle invalid input
    print("Invalid Input")

