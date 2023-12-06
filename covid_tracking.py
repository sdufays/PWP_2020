def track(login):
    global covid_symptoms, covid_points, list_of_people

    print(f"{login}, please answer the following questions with either 'Y' for yes or 'N' for no.")
    questions = {
        "Have you had any fever recently?": 30,
        "Do you find yourself with a runny nose?": 30,
        "Do you find yourself often coughing?": 25,
        "Have you identified a loss of smell or taste?": 35,
        "Do you have a sore throat?": 15,
        "Have you had any headaches?": 10,
        "Have you had any muscle aches?": 30,
        "Have you experienced any Diarrhea or abdominal cramps?": 10
    }

    for question, points in questions.items():
        response = input(question + " : ")
        if response == "Y":
            covid_symptoms += 1
            covid_points += points

    list_of_people.setdefault(login, []).extend([covid_symptoms, covid_points])
    write_to_file('covid_roster.txt', list_of_people)
    covid_symptoms, covid_points = 0, 0  # Reset after logging


def write_to_file(filename, data):
    with open(filename, 'w+') as file:
        for key, value in data.items():
            file.write(f"{key},{value}\n")


def tracking():
    global list_of_people

    while True:
        try:
            login = input("What is your name?: ")
            if login in list_of_people:
                password = input("What is your four-digit password?: ")
                if password in list_of_people[login]:
                    track(login)
                    break
                else:
                    print("Your password is incorrect. Try again or delete your account and sign in if you forgot!")
                    break
            else:
                print("Please sign up before logging in symptoms!")
                break
        except Exception as e:
            print(f"An error occurred: {e}")

# Initialize global variables
covid_symptoms = 0
covid_points = 0
list_of_people = {}  # This should be populated with user data

# Example usage
# tracking()
