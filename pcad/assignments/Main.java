        System.out.println();

        /*
         * PRACTICE PROBLEMS AND SOLUTIONS
         * Try to solve each problem yourself before reading the solution.
         */

        // PROBLEM 1 (for): Print numbers from 1 to 10.
        System.out.println("\nProblem 1: Print numbers from 1 to 10");
        for (int i = 1; i <= 10; i++) {
            System.out.print(i + " ");
        }
        System.out.println();

        // PROBLEM 2 (for): Find the sum of numbers from 1 to 100.
        System.out.println("\nProblem 2: Sum numbers from 1 to 100");
        int sum = 0;
        for (int i = 1; i <= 100; i++) {
            sum += i;
        }
        System.out.println("Solution: " + sum);

        // PROBLEM 3 (for): Print the multiplication table of 7.
        System.out.println("\nProblem 3: Multiplication table of 7");
        for (int i = 1; i <= 10; i++) {
            System.out.println("7 x " + i + " = " + (7 * i));
        }

        // PROBLEM 4 (while): Count down from 10 to 1.
        System.out.println("\nProblem 4: Count down from 10 to 1");
        int countdown = 10;
        while (countdown >= 1) {
            System.out.print(countdown + " ");
            countdown--;
        }
        System.out.println("\nSolution: Blast off!");

        // PROBLEM 5 (while): Find how many digits are in a positive number.
        System.out.println("\nProblem 5: Count digits in 5832");
        int digitsNumber = 5832;
        int digits = 0;
        while (digitsNumber > 0) {
            digitsNumber /= 10;
            digits++;
        }
        System.out.println("Solution: " + digits + " digits");

        // PROBLEM 6 (while): Reverse a positive integer.
        System.out.println("\nProblem 6: Reverse the number 1234");
        int original = 1234;
        int temp = original;
        int reversed = 0;
        while (temp > 0) {
            int lastDigit = temp % 10;
            reversed = reversed * 10 + lastDigit;
            temp /= 10;
        }
        System.out.println("Solution: " + reversed);

        // PROBLEM 7 (do-while): Print numbers from 1 to 5.
        System.out.println("\nProblem 7: Print numbers from 1 to 5 using do-while");
        int n = 1;
        do {
            System.out.print(n + " ");
            n++;
        } while (n <= 5);
        System.out.println();

        // PROBLEM 8 (do-while): Show a menu at least once.
        System.out.println("\nProblem 8: Simple menu using do-while");
        Scanner scanner = new Scanner(System.in);
        int choice;
        do {
            System.out.println("Menu: 1 = Say Hello, 0 = Exit");
            System.out.print("Enter your choice (0 or 1): ");

            // Check that the user entered an integer.
            while (!scanner.hasNextInt()) {
                System.out.print("Please enter a number (0 or 1): ");
                scanner.next();
            }

            choice = scanner.nextInt();

            if (choice == 1) {
                System.out.println("Hello!");
            } else if (choice != 0) {
                System.out.println("Invalid choice.");
            }
        } while (choice != 0);
        System.out.println("Program ended.");
        scanner.close();

        // PROBLEM 9 (for): Count even numbers from 1 to 20.
        System.out.println("\nProblem 9: Even numbers from 1 to 20");
        for (int i = 2; i <= 20; i += 2) {
            System.out.print(i + " ");
        }
        System.out.println();

        // PROBLEM 10 (while): Find the factorial of 5.
        System.out.println("\nProblem 10: Find 5 factorial (5!)");
        int factorialNumber = 5;
        int factorial = 1;
        int counter = 1;
        while (counter <= factorialNumber) {
            factorial *= counter;
            counter++;
        }
        System.out.println("Solution: 5! = " + factorial);
    }
}
