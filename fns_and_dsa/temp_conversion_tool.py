#!/usr/bin/env python3 
FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5)

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def main():
    try:
        temp_input = float(input("Enter the temperature to convert: "))
        scale = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().lower()
        if scale == "c":
            converted_temp = convert_to_fahrenheit(temp_input)
            print(f"{temp_input}°C is equal to {converted_temp:.2f}°F")
        elif scale == "f":
            converted_temp = convert_to_celsius(temp_input)
            print(f"{temp_input}°F is equal to {converted_temp:.2f}°C")
        else:
            print("Invalid input. Please specify 'C' for Celsius or 'F' for Fahrenheit.")
    
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
if __name__ == "__main__":
    main()

