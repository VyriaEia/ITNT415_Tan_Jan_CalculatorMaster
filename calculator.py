
# Calculator Master
# S-ITNT415 Midterm Summative Assessment
def addition(a, b):
    return a + b
    
def main():
    while True:
        print("\n===== CALCULATOR MASTER =====")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "5":
            print("Thank you for using Calculator Master!")
            break
        elif choice == "1":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            result = addition(num1, num2)
            print("Result:", result)

        elif choice in ["2", "3", "4"]:
            print("This operation is not implemented yet.")
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
