def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def convert_temperature(value, unit):
    if unit == "C":
        fahrenheit = celsius_to_fahrenheit(value)
        kelvin = celsius_to_kelvin(value)
        print(f"\n{value}°C is equivalent to:")
        print(f"  {fahrenheit:.2f}°F (Fahrenheit)")
        print(f"  {kelvin:.2f}K (Kelvin)\n")
    elif unit == "F":
        celsius = fahrenheit_to_celsius(value)
        kelvin = fahrenheit_to_kelvin(value)
        print(f"\n{value}°F is equivalent to:")
        print(f"  {celsius:.2f}°C (Celsius)")
        print(f"  {kelvin:.2f}K (Kelvin)\n")
    elif unit == "K":
        celsius = kelvin_to_celsius(value)
        fahrenheit = kelvin_to_fahrenheit(value)
        print(f"\n{value}K is equivalent to:")
        print(f"  {celsius:.2f}°C (Celsius)")
        print(f"  {fahrenheit:.2f}°F (Fahrenheit)\n")
    else:
        print("\n[Error] Invalid unit entered. Please try again.")

def main():
    print("Welcome to the Temperature Converter!")
    print("You can convert temperatures between Celsius, Fahrenheit, and Kelvin.\n")
    
    while True:
        try:
            value = float(input("Please enter the temperature value you'd like to convert: "))
            unit = input("Please enter the unit of temperature (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()
            
            if unit in ["C", "F", "K"]:
                convert_temperature(value, unit)
            else:
                print("\n[Error] Invalid unit entered. Please enter C, F, or K.")
            
            another_conversion = input("Would you like to perform another conversion? (yes/no): ").strip().lower()
            if another_conversion != 'yes':
                print("\nThank you for using the Temperature Converter. Goodbye!")
                break
            
        except ValueError:
            print("\n[Error] Invalid input. Please enter a numerical value for the temperature.\n")

if __name__ == "__main__":
    main()
