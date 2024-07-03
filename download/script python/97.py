def celsius_para_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

def fahrenheit_para_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius


temp_celsius = float(input('Digite a temperatura em Celsius: '))
temp_fahrenheit = celsius_para_fahrenheit(temp_celsius)
print(f'{temp_celsius} graus Celsius equivalem a {temp_fahrenheit} graus Fahrenheit.')

temp_fahrenheit = float(input('Digite a temperatura em Fahrenheit: '))
temp_celsius = fahrenheit_para_celsius(temp_fahrenheit)
print(f'{temp_fahrenheit} graus Fahrenheit equivalem a {temp_celsius} graus Celsius.')
