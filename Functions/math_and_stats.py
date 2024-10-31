import random
import math
import statistics
import random


vals1_100 = range(1,100)
vals_sample = random.sample(vals1_100, 75)
vals_choices = random.choices(vals1_100, k = 200)
radius = random.randint(3, 10)
pi = math.pi

# Experimenting with a subset of 100
sum_of_sample = sum(vals_sample)
print(sum_of_sample)

average_of_75 = sum_of_sample / len(vals_sample)
print(average_of_75)

median_of_75 = statistics.median(vals_sample)
print(median_of_75)


# Experimenting with a supeset of 200 values
ave_of_200 = sum(vals_choices) / len(vals_choices)
print(ave_of_200)

med_of_200 = statistics.median(vals_choices)
print(med_of_200)

mode_of_200 = statistics.mode(vals_choices)
print(mode_of_200)

dev_of_200 = statistics.stdev(vals_choices)
print(dev_of_200)