
full_name = 'Vieri Escamilla'
index = full_name.find(" ")


if index != -1:
    first_name = full_name[:index]
    last_name = full_name[index + 1:]
else: 
    first_name = full_name
    last_name = ""

print(f'Full Name: {full_name}')
print(f'First Name: {first_name}')
print(f'Last Name; {full_name}')