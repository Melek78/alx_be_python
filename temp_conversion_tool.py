FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
temprature = float(input("Enter the temperature to convert: "))
type_of_temprature = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
if type_of_temprature == "C":
    converted_temprature = convert_to_celsius(temprature)
    print(f"{temprature}°F is {converted_temprature}°C")
elif type_of_temprature == "F":
    converted_temprature = convert_to_fahrenheit(temprature)
    print(f"{temprature}°C is {converted_temprature}°F")
else:
    print("Invalid temperature. Please enter a numeric value.")