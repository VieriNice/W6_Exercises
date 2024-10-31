# Open the file

with open("sample_data.csv", 'r') as f:
    data = f.readlines()


# Read the file


data = f.readlines()


# print(f.readline()) # Gives you the first line
# print(f.readline(25)) # Gives you the first line with only 25 characters
# print(f.readlines(20000)) # Returns full amount of characters asked for and finish the line it was on.

#Close the file

f.close()

data_list = []

for i in data: 
    data_list.append(i.split(','))

print(data_list)
print(data_list[0][2])








ages = []

for i in data_list:
    ages.append(i[2])

ages.pop(0)

# print(f'List of ages: {ages}')

ages_file = open("survey_ages.txt", 'x')
ages_file.write(str(ages))
ages_file.close()

