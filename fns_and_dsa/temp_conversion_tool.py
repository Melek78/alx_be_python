CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
try:
    temperature = float(input("Enter the temperature to convert: "))
    type_of_temperature = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    if type_of_temperature == "C":
        converted_temperature = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted_temperature:.2f}°F")
    elif type_of_temperature == "F":
        converted_temperature = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted_temperature:.2f}°C")
    else:
        raise ValueError("Invalid unit. Please enter 'C' or 'F'.")
except ValueError:
    print("Invalid temperature. Please enter a numeric value.")
