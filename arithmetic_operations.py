def main():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (add, subtract, multiply, divide): ").lower()
        result = perform_operation(num1, num2, operation)
        print(f"The result of the operation is: {result}")
    except ValueError:
        print("Invalid input. Please enter numerical values.")

if __name__ == "__main__":
    main()