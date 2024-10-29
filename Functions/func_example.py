def my_first_function():
    print("Hello World!")
    return "How are you?"


print(my_first_function())

# def calculator(n1, n2, operation = '+'): 
#     print(f"You have chosen the {operation} operation ")
#     if operation == '-':
#         return n1 - n2
#     elif operation == '*':
#         return n1 * n2 
#     elif operation == '/':
#         return n1 / n2 
#     else: 
#         n1 + n2

# print(calculator(n2 = 23, n1 = 2, operation = '-'))



# def calculator2(*nums):
#     return nums

# print(calculator2(2, 4, 6 , 8))


# def guest_list(*args):
#   return f'The guest list includes: {args}'

# print(guest_list('Michael', 'Maria', 'Ana'))


# def relative(name, relationship):
#     return f'{name} is my {relationship}'

# print(relative('becky', 'cousin'))





def rels(rel, name, **kwargs):
    kwargs['relationship'] = rel
    kwargs['name'] = name
    return kwargs

person1 = rels('Cousin', 'Becky', attribute = 'funny')
print(person1)

person2 = rels('Uncle', 'Joe', address = '103 Maple', city_state_zip = 'Berwyn, Illinois, 60402')
print(person2)



