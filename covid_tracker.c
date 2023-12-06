#include <stdio.h>
#include <string.h>

#define MAX_USERS 10
#define MAX_NAME_LENGTH 50
#define MAX_PASSWORD_LENGTH 10
#define MAX_QUESTIONS 8

typedef struct {
    char name[MAX_NAME_LENGTH];
    char password[MAX_PASSWORD_LENGTH];
    int covid_symptoms;
    int covid_points;
} User;

// Global array of users
User users[MAX_USERS];
int userCount = 0;

void trackSymptoms(int userIndex) {
    const char* questions[MAX_QUESTIONS] = {
        "Have you had any fever recently? (Y/N): ",
        "Do you find yourself with a runny nose? (Y/N): ",
        // Add other questions here
    };

    int points[MAX_QUESTIONS] = {30, 30 /*, ... other points */};
    char answer;

    printf("Answer the following questions with 'Y' for yes or 'N' for no.\n");
    for (int i = 0; i < MAX_QUESTIONS; i++) {
        printf("%s", questions[i]);
        scanf(" %c", &answer); // Space before %c to skip any whitespace
        if (answer == 'Y' || answer == 'y') {
            users[userIndex].covid_symptoms++;
            users[userIndex].covid_points += points[i];
        }
    }
}

int main() {
    char login[MAX_NAME_LENGTH], password[MAX_PASSWORD_LENGTH];

    while (1) {
        printf("What is your name?: ");
        scanf("%s", login);

        int userIndex = -1;
        for (int i = 0; i < userCount; i++) {
            if (strcmp(users[i].name, login) == 0) {
                userIndex = i;
                break;
            }
        }

        if (userIndex != -1) {
            printf("What is your four-digit password?: ");
            scanf("%s", password);

            if (strcmp(users[userIndex].password, password) == 0) {
                trackSymptoms(userIndex);
                break;
            } else {
                printf("Incorrect password.\n");
                break;
            }
        } else {
            printf("User not found.\n");
            break;
        }
    }

    return 0;
}
