# ==============================================================================
# LAB 16: UTILITY CALCULATOR (ENTERPRISE MODULAR UTILITY CALCULATOR)
# ==============================================================================

# Session history ledger to store past calculations
history_ledger = []


# ------------------------------------------------------------------------------
# 1. Modular Function Definitions
# ------------------------------------------------------------------------------

def add(a, b):
    """Adds two numbers."""
    return a + b


def subtract(a, b):
    """Subtracts second number from the first."""
    return a - b


def multiply(a, b):
    """Multiplies two numbers."""
    return a * b


def divide(a, b):
    """Divides first number by second with defensive zero check."""
    if b == 0:
        return "Error: Division by zero is undefined."
    return a / b


def modulus(a, b):
    """Calculates remainder safely using modulus operator."""
    if b == 0:
        return "Error: Modulus by zero is undefined."
    return a % b


def power(base, exp=2):
    """Computes power with a default argument (exp=2 for square)."""
    return base ** exp


def view_history():
    """Displays audit log of all calculations performed in current session."""
    print("\n--- CALCULATION HISTORY ---")
    if not history_ledger:
        print("No calculations recorded yet.")
    else:
        for index, record in enumerate(history_ledger, 1):
            print(f"{index}. {record}")
    print("---------------------------\n")


# ------------------------------------------------------------------------------
# 2. Main Interactive Loop & Interface
# ------------------------------------------------------------------------------

def main():
    while True:
        print("==================================================")
        print("       ENTERPRISE MODULAR UTILITY CALCULATOR       ")
        print("==================================================")
        print("Select an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Modulus / Remainder (%)")
        print("6. Power / Exponentiation (Default: Square)")
        print("7. View Calculation History")
        print("8. Exit")
        print("--------------------------------------------------")

        choice = input("Enter your choice (1-8): ").strip()

        if choice == '8':
            print("Terminating the program. Goodbye!")
            break

        elif choice == '7':
            view_history()

        elif choice in ('1', '2', '3', '4', '5'):
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
            except ValueError:
                print("[ERROR] Invalid numeric input. Please enter valid numbers.\n")
                continue

            if choice == '1':
                res = add(a, b)
                log = f"[RESULT] {a} + {b} = {res}"
            elif choice == '2':
                res = subtract(a, b)
                log = f"[RESULT] {a} - {b} = {res}"
            elif choice == '3':
                res = multiply(a, b)
                log = f"[RESULT] {a} * {b} = {res}"
            elif choice == '4':
                res = divide(a, b)
                log = f"[RESULT] {a} / {b} = {res}"
            elif choice == '5':
                res = modulus(a, b)
                log = f"[RESULT] {a} % {b} = {res}"

            print(log)
            history_ledger.append(log)

        elif choice == '6':
            try:
                base = float(input("Enter base number: "))
                exp_input = input("Enter exponent (press Enter to default to 2): ").strip()

                if exp_input == "":
                    res = power(base)
                    log = f"[RESULT] {base} ^ 2 = {res}"
                else:
                    exp = float(exp_input)
                    res = power(base, exp)
                    log = f"[RESULT] {base} ^ {exp} = {res}"

                print(log)
                history_ledger.append(log)
            except ValueError:
                print("[ERROR] Invalid numeric input. Please try again.\n")

        else:
            print("[ERROR] Invalid choice. Please enter a number from 1 to 8.\n")


# Standard entry point execution
if __name__ == "__main__":
    main()
