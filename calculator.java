import java.util.Arrays;
import java.util.Scanner;

public class NumberOperations {
    private static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        float[] numbers = new float[5];

        // Input 5 numbers
        for (int i = 0; i < 5; i++) {
            System.out.print("Enter number " + (i + 1) + ": ");
            while (true) {
                try {
                    numbers[i] = Float.parseFloat(scanner.nextLine());
                    break;
                } catch (NumberFormatException e) {
                    System.out.print("Invalid input. Please enter a number: ");
                }
            }
        }

        // Menu
        while (true) {
            System.out.println("\nMenu:");
            System.out.println("1. Find the Sum");
            System.out.println("2. Obtain the Average");
            System.out.println("3. Get the Median");
            System.out.println("4. Find the Difference");
            System.out.println("5. Exit");

            System.out.print("Choose an option (1-5): ");
            int choice;
            try {
                choice = Integer.parseInt(scanner.nextLine());
            } catch (NumberFormatException e) {
                System.out.println("Invalid input. Please enter a number between 1 and 5.");
                continue;
            }

            switch (choice) {
                case 1:
                    System.out.println("Sum: " + sumNumber(numbers));
                    break;
                case 2:
                    System.out.println("Average: " + averageNumber(numbers));
                    break;
                case 3:
                    System.out.println("Median: " + medianNumber(numbers));
                    break;
                case 4:
                    System.out.println("Difference: " + numberDifference(numbers));
                    break;
                case 5:
                    System.out.println("Exiting program.");
                    return;
                default:
                    System.out.println("Invalid choice. Please choose a number between 1 and 5.");
                    break;
            }
        }
    }

    private static float sumNumber(float[] numbers) {
        float sum = 0;
        for (float number : numbers) {
            sum += number;
        }
        return sum;
    }

    private static float averageNumber(float[] numbers) {
        return sumNumber(numbers) / numbers.length;
    }

    private static float medianNumber(float[] numbers) {
        float[] sortedNumbers = Arrays.copyOf(numbers, numbers.length);
        Arrays.sort(sortedNumbers);
        return sortedNumbers[sortedNumbers.length / 2];
    }

    private static float numberDifference(float[] numbers) {
        float[] sortedNumbers = Arrays.copyOf(numbers, numbers.length);
        Arrays.sort(sortedNumbers);
        return sortedNumbers[sortedNumbers.length - 1] - sortedNumbers[0];
    }
}
