import java.util.Scanner;

class Expense {
    String category;
    double amount;

    public Expense(String category, double amount) {
        this.category = category;
        this.amount = amount;
    }
}

class ExpenseTracker {
    LinkedList<Expense> expenses;

    public ExpenseTracker() {
        expenses = new LinkedList<>();
    }

    public void addExpense(String category, double amount) {
        expenses.add(new Expense(category, amount));
    }

    public double calculateTotalExpense() {
        double totalExpense = 0;
        for (Expense expense : expenses) {
            totalExpense += expense.amount;
        }
        return totalExpense;
    }
}

public class BudgetManager {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ExpenseTracker expenseTracker = new ExpenseTracker();

        while (true) {
            System.out.println("Enter category of expense (or type 'quit' to exit): ");
            String category = scanner.nextLine();
            if (category.equals("quit")) {
                break;
            }

            System.out.println("Enter amount: ");
            double amount = scanner.nextDouble();
            scanner.nextLine(); // Consume newline character

            expenseTracker.addExpense(category, amount);
        }

        System.out.println("Total Expense: $" + expenseTracker.calculateTotalExpense());
    }
}