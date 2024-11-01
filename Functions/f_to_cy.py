def conv_f_to_c(fahrenheit):
    '''Convert Fahrenheit to Celcius'''
    celcius = (fahrenheit - 32) * 5.0 / 9.0
    return round(celcius)

if __name__ == '__main__':
    fahrenheit_values = [212, 90, 72, 32, 0, ]

for temp_F in fahrenheit_values:
    temp_C = conv_f_to_c(temp_F)
print(f'{temp_F}F is {temp_C}C')
