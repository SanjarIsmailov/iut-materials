import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        // FOR LOOP
        for (int i = 1; i <= 5; i++) {
            System.out.print(i + " ");
        }
        System.out.println();

        // WHILE LOOP
        int number = 1;
        while (number <= 5) {
            System.out.print(number + " ");
            number++;
        }
        System.out.println();

        // DO-WHILE LOOP
        int value = 1;
        do {
            System.out.print(value + " ");
            value++;
        } while (value <= 5);
        System.out.println();

        // Problem 1: Print numbers from 1 to 10.
        for (int i = 1; i <= 10; i++) {
            System.out.print(i + " ");
        }
        System.out.println();

        // Problem 2: Find the sum of numbers from 1 to 100.
        int sum = 0;
        for (int i = 1; i <= 100; i++) {
            sum += i;
        }
        System.out.println(sum);

        // Problem 3: Print the multiplication table of 7.
        for (int i = 1; i <= 10; i++) {
            System.out.println("7 x " + i + " = " + (7 * i));
        }

        // Problem 4: Print numbers from 10 down to 1.
        int countdown = 10;
        while (countdown >= 1) {
            System.out.print(countdown + " ");
            countdown--;
        }
        System.out.println();

        // Problem 5: Count the digits in the number 5832.
        int digitsNumber = 5832;
        int digits = 0;
        while (digitsNumber > 0) {
            digitsNumber /= 10;
            digits++;
        }
        System.out.println(digits);

        // Problem 6: Reverse the number 1234.
        int temp = 1234;
        int reversed = 0;
        while (temp > 0) {
            int lastDigit = temp % 10;
            reversed = reversed * 10 + lastDigit;
            temp /= 10;
        }
        System.out.println(reversed);

        // Problem 7: Print numbers from 1 to 5 using do-while.
        int n = 1;
        do {
            System.out.print(n + " ");
            n++;
        } while (n <= 5);
        System.out.println();

        // Problem 8: Show a menu until the user enters 0.
        Scanner scanner = new Scanner(System.in);
        int choice;
        do {
            System.out.println("1 - Say Hello");
            System.out.println("0 - Exit");
            choice = scanner.nextInt();

            if (choice == 1) {
                System.out.println("Hello!");
            }
        } while (choice != 0);

        // Problem 9: Print even numbers from 1 to 20.
        for (int i = 2; i <= 20; i += 2) {
            System.out.print(i + " ");
        }
        System.out.println();

        // Problem 10: Find the factorial of 5.
        int factorial = 1;
        int counter = 1;
        while (counter <= 5) {
            factorial *= counter;
            counter++;
        }
        System.out.println(factorial);

        scanner.close();
    }
}
