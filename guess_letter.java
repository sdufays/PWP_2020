import java.util.Random;
import java.util.Scanner;

public class GuessTheLetterGame {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();
        int attempts = 10;

        // Generate a random letter
        char correctLetter = (char) ('a' + random.nextInt(26));

        // Game loop
        while (attempts > 0) {
            System.out.print("Guess a letter (you have " + attempts + " tries left): ");
            String input = scanner.nextLine().toLowerCase();

            // Validate input
            if (input.length() != 1 || !Character.isLetter(input.charAt(0))) {
                System.out.println("Invalid input. Please enter a single letter.");
                continue;
            }

            char guess = input.charAt(0);
            int distance = Math.abs(correctLetter - guess);
            attempts--;

            // Provide feedback based on the distance
            if (guess == correctLetter) {
                System.out.println("Correct! You have guessed the letter in " + (10 - attempts) + " tries!");
                break;
            } else if (distance == 1) {
                System.out.println("Hot! Almost there!");
            } else if (distance <= 4) {
                System.out.println("Warm! Keep trying!");
            } else {
                System.out.println("Cold...");
            }

            // Check if attempts are exhausted
            if (attempts == 0) {
                System.out.println("Out of tries! The correct letter was '" + correctLetter + "'.");
            }
        }

        scanner.close();
    }
}
