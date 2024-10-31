#loops
#dictionaries, lists, tuples in a list

movies = [('The Minions', 'Her'), 
          ('The Whale', '8 Mile', 'Fall Guy'),
          ('La La Land', 'Wolf of Wall Street')]



m1, m2, m3 = movies

change_m1 = list(m1)
change_m1.append('The Last Unicorn')

m1 = tuple(change_m1)
print(m1)

change_m2 = list(movies)
change_m2[2] = 'The Fall Guy'
print(change_m2)













# set1, set2, set3 = movies 
# print(set1)

# set1 = movies[0]
# set2 = movies[1]



# set3 = movies[2]











# movie1, movie2 = set1 #Gives back one movie from tuple
# print(movie1)
# print(movies[0][0])

# print(f'I heard {movies[1][1]} is a good movie')



# for x in movies:
#     for i in x:
#         print(f'{i} is a great movie.')