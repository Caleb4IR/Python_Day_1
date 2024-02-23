movies = [

    {"title": "Inception", "ratings": [5, 4, 5, 4, 5]},

    {"title": "Interstellar", "ratings": [5, 5, 4, 5, 4]},

    {"title": "Dunkirk", "ratings": [4, 4, 4, 3, 4]},

    {"title": "The Dark Knight", "ratings": [5, 5, 5, 5, 5]},

    {"title": "Memento", "ratings": [4, 5, 4, 5, 4]},

]

#Task 1
#Output
#["Inception", "Interstellar", "Dunkirk", "The Dark Knight", "Memento"]
titles = list(map(lambda movie: movie["title"], movies))
print(titles)

#task 1.1
average = map(lambda x: sum(x['ratings'])/len(x['ratings']),movies)
print(list(average))



# Task 1.2 - Find average for all, use  map, filter, all, ...
# Dont use for loop or List comp
#Output should be:
# movies = [

#     {"title": "Inception", "ratings": [5, 4, 5, 4, 5], "average_rating": 4.6},

#     {"title": "Interstellar", "ratings": [5, 5, 4, 5, 4], "average_rating": 4.6},

#     {"title": "Dunkirk", "ratings": [4, 4, 4, 3, 4], "average_rating": 3.8},

#     {"title": "The Dark Knight", "ratings": [5, 5, 5, 5, 5], "average_rating": 5},

#     {"title": "Memento", "ratings": [4, 5, 4, 5, 4], "average_rating": 4.4},

# ]

# def calculate_average(movie):
#   average_rating = sum(movie["ratings"]) / len(movie["ratings"])
#   movie["average_rating"] = average_rating
#   return movie

# movies = list(map(calculate_average, movies))

# print(movies)

#Or

average = map(lambda x: {**x, "average_rating": sum(x['ratings'])/len(x['ratings'])}, movies)
movies = list(average)
print(movies)

#Task 2
#Find the top rated movie
#Output
#The top rated movie is "The dark Knight"


top_rated_movie = max(movies, key=lambda x: sum(x['ratings'])/len(x['ratings']))
print(f"The top rated movie is {top_rated_movie['title']}")

#Task 3
#Title of movies with ratings more than 4.6
#Output = ["Inception", "Interstellar","The Dark Knight"]

# Calculate average rating for each movie
average_ratings = map(lambda x: sum(x['ratings']) / len(x['ratings']), movies)

# Filter movies with ratings more than or equal to 4.6
top_rated_titles = list(map(lambda movie: movie['title'], filter(lambda movie: sum(movie['ratings']) / len(movie['ratings']) >= 4.6, movies)))

print(top_rated_titles)

#Task 4
#Movie names in order of rating
#Output
#["Dark Knight", "Inception", "Interstellar", "Memento", "Dunkirk"]"

movies_with_ratings = list(map(lambda movie: (movie['title'], sum(movie['ratings']) / len(movie['ratings'])), movies))

sorted_movies = sorted(movies_with_ratings, key=lambda x: x[1], reverse=True)

sorted_movie_titles = list(map(lambda x: x[0], sorted_movies))

print(sorted_movie_titles)