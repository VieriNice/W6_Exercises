import random 

# I am using the .shuffle function to mix the color list
color_list = ['Red', 'Blue', 'Green', 'Yellow' ]
random.shuffle(color_list)
print(color_list)

# This list is being used for the .randint function 
print(random.randint(0,3))

# This functions gives me random animals from the list set at only 2
animal_list = ['Dog', 'Cat', 'Turtle', 'Bird']
print(random.sample(animal_list, k=2))