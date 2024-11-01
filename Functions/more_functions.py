
def display_mailing_label(name, address, city, state, zip):
    print(f'Customer name: {name}')
    print(f'Customer Address: {address}')
    print(f'Customer City: {city}')
    print(f'Customer State: {state} ')
    print(f'Customer Zip: {zip}')

display_mailing_label('Vieri Escamilla', '123 East Ave', 'Chicago', 'Illinois', '60636')

def add_numbers(*args):
    return args

result = add_numbers(2, 4, 6, 8)

sum_result = 0


for n in result:
    sum_result += n
    

print(sum_result)



