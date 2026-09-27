
# Calculator Master
# S-ITNT415 Midterm Summative Assessment
def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b
    
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
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                result = addition(num1, num2)
                print("Result:", result)

            except ValueError:
                print("Invalid input. Please enter numbers only.")

        elif choice == "2":
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                result = subtraction(num1, num2)
                print("Result:", result)

            except ValueError:
                print("Invalid input. Please enter numbers only.")

        elif choice == "3":
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                result = multiplication(num1, num2)
                print("Result:", result)

            except ValueError:
                print("Invalid input. Please enter numbers only.")

        elif choice == "4":
            print("This operation is not implemented yet.")
        else:
            print("Invalid choice. Please try again.")

        


if __name__ == "__main__":
    main()
