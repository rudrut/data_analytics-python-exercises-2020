fahrenheitMeltDegrees = 32.0
fahrenheitBoilDegrees = 212.0

celsiusMeltDegrees = 0.0
celsiusBoilDegrees = 100.0

# a)
celsiusConvert = float(input("Convert Celsius to Fahrenheit: "))
celsiusResult = celsiusConvert * 1.8 + fahrenheitMeltDegrees
print("Celsius degrees converted to Fahrenheit: " + str(round(celsiusResult, 2)))

print()

# b)
fahrenheitConvert = float(input("Convert Fahrenheit to Celsius: "))
fahrenheitResult = (fahrenheitConvert - fahrenheitMeltDegrees) / 1.8
print("Fahrenheit degrees converted to Celsius: " + str(round(fahrenheitResult, 2)))