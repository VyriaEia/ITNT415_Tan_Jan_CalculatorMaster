from datetime import datetime

# ============================================================
# CALCULATOR MASTER
# Student: Jan Rhodes P. Tan
# Course: S-ITNT415
# Section: BIT42
# ============================================================

calculation_history = []
operation_counts = {
    "Addition": 0,
    "Subtraction": 0,
    "Multiplication": 0,
    "Division": 0
}


# ---------------------- BASIC OPERATIONS ----------------------

def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError("A number cannot be divided by zero.")
    return num1 / num2


# ---------------------- INPUT HANDLING ------------------------

def get_number(prompt):
    """Continuously asks the user until a valid number is entered."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("\n[ERROR] Invalid input. Please enter a valid number.")


def format_number(number):
    """Removes unnecessary .0 from whole-number results."""
    if float(number).is_integer():
        return str(int(number))

    return f"{number:.4f}".rstrip("0").rstrip(".")


# ---------------------- HISTORY SYSTEM ------------------------

def save_calculation(num1, symbol, num2, result, operation):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    calculation = {
        "number": len(calculation_history) + 1,
        "expression": (
            f"{format_number(num1)} {symbol} "
            f"{format_number(num2)} = {format_number(result)}"
        ),
        "operation": operation,
        "time": timestamp
    }

    calculation_history.append(calculation)
    operation_counts[operation] += 1


def view_history():
    print("\n" + "=" * 55)
    print("                 CALCULATION HISTORY")
    print("=" * 55)

    if not calculation_history:
        print("No calculations have been performed yet.")
    else:
        for record in calculation_history:
            print(
                f"#{record['number']:02d} | "
                f"{record['expression']} | "
                f"{record['time']}"
            )

    print("=" * 55)
    input("\nPress Enter to return to the main menu...")


def clear_history():
    print("\n--- CLEAR CALCULATION HISTORY ---")

    if not calculation_history:
        print("History is already empty.")
        input("\nPress Enter to continue...")
        return

    confirmation = input(
        "Are you sure you want to clear all history? (Y/N): "
    ).strip().lower()

    if confirmation == "y":
        calculation_history.clear()

        for operation in operation_counts:
            operation_counts[operation] = 0

        print("Calculation history successfully cleared.")
    else:
        print("Clear operation cancelled.")

    input("\nPress Enter to continue...")


# ---------------------- STATISTICS ----------------------------

def show_statistics():
    total = len(calculation_history)

    print("\n" + "=" * 55)
    print("                CALCULATOR STATISTICS")
    print("=" * 55)
    print(f"Total calculations performed : {total}")
    print(f"Addition operations           : {operation_counts['Addition']}")
    print(f"Subtraction operations        : {operation_counts['Subtraction']}")
    print(f"Multiplication operations     : {operation_counts['Multiplication']}")
    print(f"Division operations           : {operation_counts['Division']}")
    print("=" * 55)

    if total > 0:
        most_used = max(operation_counts, key=operation_counts.get)

        if operation_counts[most_used] > 0:
            print(f"Most frequently used operation: {most_used}")

    input("\nPress Enter to return to the main menu...")


# ---------------------- INFORMATION ---------------------------

def show_about():
    print("\n" + "=" * 55)
    print("                  ABOUT CALCULATOR")
    print("=" * 55)
    print("Application : Calculator Master")
    print("Developer   : Jan Rhodes P. Tan")
    print("Course      : S-ITNT415")
    print("Section     : BIT42")
    print("Version     : 2.0")
    print()
    print("A menu-driven Python calculator developed using")
    print("Git feature branches, commits, pull requests,")
    print("merge operations, validation, and error handling.")
    print("=" * 55)

    input("\nPress Enter to return to the main menu...")


# ---------------------- CALCULATION ENGINE --------------------

def perform_calculation(operation_name, symbol, function):
    print("\n" + "-" * 55)
    print(f"{operation_name.upper()} OPERATION")
    print("-" * 55)

    num1 = get_number("Enter the first number : ")
    num2 = get_number("Enter the second number: ")

    try:
        result = function(num1, num2)

        print("\n" + "-" * 55)
        print(
            f"RESULT: {format_number(num1)} {symbol} "
            f"{format_number(num2)} = {format_number(result)}"
        )
        print("-" * 55)

        save_calculation(
            num1,
            symbol,
            num2,
            result,
            operation_name
        )

        print(
            f"Calculation #{len(calculation_history)} "
            "saved to session history."
        )

    except ZeroDivisionError as error:
        print(f"\n[ERROR] {error}")

    input("\nPress Enter to return to the main menu...")


# ---------------------- MENU SYSTEM ---------------------------

def display_menu():
    print("\n" + "=" * 55)
    print("                   CALCULATOR MASTER")
    print("               Jan Rhodes P. Tan - BIT42")
    print("=" * 55)

    print("\n[BASIC OPERATIONS]")
    print("  1. Addition")
    print("  2. Subtraction")
    print("  3. Multiplication")
    print("  4. Division")

    print("\n[CALCULATOR TOOLS]")
    print("  5. View Calculation History")
    print("  6. Clear Calculation History")
    print("  7. Calculator Statistics")
    print("  8. About Calculator")

    print("\n  9. Exit")
    print("=" * 55)


def main():
    while True:
        display_menu()
        choice = input("Select an option [1-9]: ").strip()

        if choice == "1":
            perform_calculation("Addition", "+", add)

        elif choice == "2":
            perform_calculation("Subtraction", "-", subtract)

        elif choice == "3":
            perform_calculation("Multiplication", "*", multiply)

        elif choice == "4":
            perform_calculation("Division", "/", divide)

        elif choice == "5":
            view_history()

        elif choice == "6":
            clear_history()

        elif choice == "7":
            show_statistics()

        elif choice == "8":
            show_about()

        elif choice == "9":
            print("\n" + "=" * 55)
            print("Thank you for using Calculator Master.")
            print("Program terminated successfully.")
            print("=" * 55)
            break

        else:
            print(
                "\n[ERROR] Invalid menu selection. "
                "Please choose from 1 to 9."
            )
            input("\nPress Enter to continue...")


# ---------------------- PROGRAM ENTRY POINT -------------------

if __name__ == "__main__":
    main()