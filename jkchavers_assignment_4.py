student_name = "Jaylen Chavers"  # Replace with your actual name
current_gpa = 4  # Float between 1.0-4.0
study_hours = 1  # Integer (Ex. 25)
social_points = 40  # Integer (Ex. 50)
stress_level = 10  # Integer 0-100

study_Options = ["Programming", "Math", "English", "History"]
study_Prompt = """Choose your study option:
A) Programming
B) Math
C) English
D) History
"""
valid_inputs = ["A", "a", "B", "b", "C", "c", "D", "d"]
chosenStudyOption = ""
choice = input(
    """Choose your course load:
    A) Light (12 credits)
    B) Standard (15 credits)
    C) Heavy (18 credits)
    """)

finalAssesssment = ""

if choice not in valid_inputs:
    print("Invalid options")
else:
    # Display welcome message with starting stats
    print(
        f"Welcome {student_name} your starting stats are \nCurrent GPA: {current_gpa}\nStudy Hours: {study_hours}\nSocial Points: {social_points}\nStress Level: {stress_level}")

    print(choice)
    if choice == "A" or choice == "a":
        if current_gpa >= 3.2 and current_gpa <= 4.0:
            current_gpa += .2
            study_hours += 5
            social_points += 50
            stress_level += 5

        elif current_gpa >= 2.8:

            current_gpa += .3
            study_hours += 15
            social_points += 30
            stress_level += 45
            # Use comparison operators to check GPA and adjust variables


        else:
            current_gpa -= .5
            study_hours += 3
            social_points += 75
            stress_level += 99
            # Use comparison operators to check GPA and adjust variables

        finalAssesssment += "\nYou have chosen the path of least resistance! You may be expendable\n"
        chosenStudyOption = input(study_Prompt)

    elif choice == "B" or choice == "b":
        if current_gpa <= 3.2 and current_gpa <= 4.0:
            current_gpa += .1
            study_hours += 15
            social_points += 45
            stress_level += 5


        elif current_gpa >= 2.8:

            current_gpa -= .2
            study_hours += 24
            social_points += 26
            stress_level += 65
            # Use comparison operators to check GPA and adjust variables


        else:
            current_gpa -= 1.1
            study_hours += 6
            social_points += 75
            stress_level += 99
            # Use comparison operators to check GPA and adjust variables
        finalAssesssment += "\nAn arduous path lies ahead! Your courage will be rewarded\n"
        chosenStudyOption = input(study_Prompt)


    elif choice == "C" or choice == "c":
        if current_gpa >= 3.2 and current_gpa <= 4.0:
            current_gpa -= .3
            study_hours += 38
            social_points += 10
            stress_level += 78


        elif current_gpa >= 2.8:

            current_gpa -= .7
            study_hours += 30
            social_points += 20
            stress_level += 89
            # Use comparison operators to check GPA and adjust variables


        else:
            current_gpa -= 1.8
            study_hours += 15
            social_points += 0
            stress_level += 110
            # Use comparison operators to check GPA and adjust variables

        finalAssesssment += "\nYour survival is not expected! IF YOU DO SURVIVE, YOU WILL BE ONE STEP CLOSER TO YOUR DESTINY!!!!!!\n"
        chosenStudyOption = input(study_Prompt)

if chosenStudyOption is study_Options:
   
    if chosenStudyOption != study_Options[0]:
        finalAssesssment += "\nYou have achieved the rank of Sith Assassin\n"
    elif chosenStudyOption == study_Options[1]:
        finalAssesssment += "\nYou have achieved the rank of Sith Acolyte\n"
    elif chosenStudyOption == study_Options[0]:
        finalAssesssment += "\nYou have achieved the rank of Sith Lord\n"

elif chosenStudyOption not in study_Options:
    print("Invalid option")

if study_hours >= 50 and current_gpa <= 3.5:
    current_gpa += .4
    finalAssesssment += "\n Your GPA was boosted to new levels\n"
elif study_hours <= 25 and current_gpa <= 3.5:
    current_gpa -= .1
    finalAssesssment += "\n Your GPA was too low to study less than 26 hours a week. DO BETTER\n"

finalAssesssment += f"\nUpdated Stats:\nGPA: {current_gpa:.2f}\nStudy Hours: {study_hours}\nSocial Points: {social_points}\nStress Level: {stress_level}"

print(finalAssesssment)