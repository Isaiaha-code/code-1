from CreateClass import Collection

# Create an instance of the Collection class
my_collection = Collection()

# Add some movies
my_collection.add_item("movie", "Spider-Man")
my_collection.add_item("movie", "Black Panther")

# Add some video games
my_collection.add_item("game", "Fortnite")
my_collection.add_item("game", "NBA 2K25")

# Display all movies
print("Movies in collection:")
my_collection.display_movies()

print("\nUpdated movie list:")
my_collection.display_movies()

print("\nUpdated video game list:")
my_collection.display_video_games()

print("\nFavorite movie:", my_collection.favorite_movie)
print("Favorite game:", my_collection.favorite_game)










