from datetime import datetime

# ============================================================
# CALCULATOR MASTER
# Student: Jan Rhodes P. Tan
# Course: S-ITNT415
# Section: BIT42
# ============================================================

calculation_history = []
calculator_memory = 0.0
last_result = None

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

def format_number(number):
    if float(number).is_integer():
        return str(int(number))

    return f"{number:.4f}".rstrip("0").rstrip(".")


def get_number(prompt):
    """
    Accepts regular numbers or ANS to reuse the previous result.
    """
    while True:
        user_input = input(prompt).strip()

        if user_input.lower() == "ans":
            if last_result is None:
                print("[ERROR] No previous result is available yet.")
                continue

            print(f"Using ANS = {format_number(last_result)}")
            return last_result

        try:
            return float(user_input)
        except ValueError:
            print(
                "[ERROR] Invalid input. Enter a valid number "
                "or type ANS."
            )


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
    print("\n" + "=" * 60)
    print("                    CALCULATION HISTORY")
    print("=" * 60)

    if not calculation_history:
        print("No calculations have been performed yet.")
    else:
        for record in calculation_history:
            print(
                f"#{record['number']:02d} | "
                f"{record['expression']} | "
                f"{record['time']}"
            )

    print("=" * 60)
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


# ---------------------- MEMORY SYSTEM -------------------------

def memory_menu():
    global calculator_memory

    while True:
        print("\n" + "=" * 60)
        print("                      MEMORY SYSTEM")
        print("=" * 60)
        print(f"Current Memory: {format_number(calculator_memory)}")
        print()
        print("  1. M+  Add value to memory")
        print("  2. M-  Subtract value from memory")
        print("  3. MR  Recall memory")
        print("  4. MC  Clear memory")
        print("  5. Return to Main Menu")
        print("=" * 60)

        choice = input("Select an option [1-5]: ").strip()

        if choice == "1":
            value = get_number("Enter value to add to memory: ")
            calculator_memory += value
            print(
                f"Memory updated: "
                f"{format_number(calculator_memory)}"
            )

        elif choice == "2":
            value = get_number(
                "Enter value to subtract from memory: "
            )
            calculator_memory -= value
            print(
                f"Memory updated: "
                f"{format_number(calculator_memory)}"
            )

        elif choice == "3":
            print(
                f"Memory Recall (MR): "
                f"{format_number(calculator_memory)}"
            )

        elif choice == "4":
            calculator_memory = 0.0
            print("Memory successfully cleared.")

        elif choice == "5":
            break

        else:
            print("[ERROR] Please select an option from 1 to 5.")


# ---------------------- STATISTICS ----------------------------

def show_statistics():
    total = len(calculation_history)

    print("\n" + "=" * 60)
    print("                   CALCULATOR STATISTICS")
    print("=" * 60)
    print(f"Total calculations performed : {total}")
    print(f"Addition operations           : {operation_counts['Addition']}")
    print(f"Subtraction operations        : {operation_counts['Subtraction']}")
    print(f"Multiplication operations     : {operation_counts['Multiplication']}")
    print(f"Division operations           : {operation_counts['Division']}")

    if last_result is None:
        print("Previous result (ANS)          : None")
    else:
        print(
            f"Previous result (ANS)          : "
            f"{format_number(last_result)}"
        )

    print(
        f"Calculator memory              : "
        f"{format_number(calculator_memory)}"
    )

    if total > 0:
        most_used = max(operation_counts, key=operation_counts.get)

        if operation_counts[most_used] > 0:
            print(f"Most used operation            : {most_used}")

    print("=" * 60)
    input("\nPress Enter to return to the main menu...")


# ---------------------- INFORMATION ---------------------------

def show_about():
    print("\n" + "=" * 60)
    print("                     ABOUT CALCULATOR")
    print("=" * 60)
    print("Application : Calculator Master")
    print("Developer   : Jan Rhodes P. Tan")
    print("Course      : S-ITNT415")
    print("Section     : BIT42")
    print("Version     : 2.1")
    print()
    print("Features:")
    print("- Four fundamental arithmetic operations")
    print("- Input validation and error handling")
    print("- Calculation history with timestamps")
    print("- Operation usage statistics")
    print("- ANS previous-result functionality")
    print("- Calculator memory (M+, M-, MR, MC)")
    print("- Continuous menu-driven interface")
    print("=" * 60)

    input("\nPress Enter to return to the main menu...")


# ---------------------- CALCULATION ENGINE --------------------

def perform_calculation(operation_name, symbol, function):
    global last_result

    print("\n" + "-" * 60)
    print(f"{operation_name.upper()} OPERATION")
    print("-" * 60)
    print("Tip: Type ANS to reuse your previous result.\n")

    num1 = get_number("Enter the first number : ")
    num2 = get_number("Enter the second number: ")

    try:
        result = function(num1, num2)
        last_result = result

        print("\n" + "-" * 60)
        print(
            f"RESULT: {format_number(num1)} {symbol} "
            f"{format_number(num2)} = {format_number(result)}"
        )
        print("-" * 60)

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
        print(
            f"ANS updated to {format_number(last_result)}."
        )

    except ZeroDivisionError as error:
        print(f"\n[ERROR] {error}")

    input("\nPress Enter to return to the main menu...")


# ---------------------- MENU SYSTEM ---------------------------

def display_menu():
    print("\n" + "=" * 60)
    print("                     CALCULATOR MASTER")
    print("                 Jan Rhodes P. Tan - BIT42")
    print("=" * 60)

    print("\n[BASIC OPERATIONS]")
    print("  1. Addition")
    print("  2. Subtraction")
    print("  3. Multiplication")
    print("  4. Division")

    print("\n[CALCULATOR TOOLS]")
    print("  5. View Calculation History")
    print("  6. Clear Calculation History")
    print("  7. Calculator Statistics")
    print("  8. Memory System")
    print("  9. About Calculator")

    print("\n  0. Exit")
    print("=" * 60)

    if last_result is not None:
        print(f"ANS: {format_number(last_result)}")

    print(f"Memory: {format_number(calculator_memory)}")


def main():
    while True:
        display_menu()
        choice = input("Select an option [0-9]: ").strip()

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
            memory_menu()

        elif choice == "9":
            show_about()

        elif choice == "0":
            print("\n" + "=" * 60)
            print("Thank you for using Calculator Master.")
            print("Program terminated successfully.")
            print("=" * 60)
            break

        else:
            print(
                "\n[ERROR] Invalid menu selection. "
                "Please choose from 0 to 9."
            )
            input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()