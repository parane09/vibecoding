# Simple Budget Calculator

def calculate_budget():
    try:
        # Ask for total monthly budget
        total_budget = float(input("Enter your total monthly budget: $"))

        # Ask for three expenses with names
        expenses = []
        for i in range(1, 4):
            print(f"\n--- Expense {i} ---")
            name = input(f"Enter description for expense {i}: ")
            amount = float(input(f"Enter amount for '{name}': $"))
            expenses.append({"name": name, "amount": amount})

        # Calculate total expenses and remaining balance
        total_expenses = sum(exp["amount"] for exp in expenses)
        remaining_balance = total_budget - total_expenses

        # Display the remaining balance
        print(f"\n" + "="*25)
        print(f"    BUDGET SUMMARY")
        print(f"="*25)
        print(f"Total Budget:   ${total_budget:10.2f}")
        print("-" * 25)
        
        for exp in expenses:
            print(f"{exp['name'][:15]:15}: ${exp['amount']:10.2f}")

        print("-" * 25)
        print(f"Total Expenses: ${total_expenses:10.2f}")
        print(f"Remaining:      ${remaining_balance:10.2f}")
        print(f"="*25)

    except ValueError:
        print("Invalid input. Please enter numeric values for budget and expense amounts.")

if __name__ == "__main__":
    calculate_budget()
