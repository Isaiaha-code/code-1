# tester.py

from CreateClass import Collection


my_collection = Collection()

# Add items
my_collection.add_item("movie", "Black Panther")
my_collection.add_item("movie", "The Batman")
my_collection.add_item("game", "Madden NFL 24")
my_collection.add_item("game", "Spider-Man 2")

# Display items
print("\n--- All Movies ---")
my_collection.display_movies()

print("\n--- All Games ---")
my_collection.display_video_games()

# Set favorites
my_collection.set_favorite("movie", "The Batman")
my_collection.set_favorite("game", "Spider-Man 2")

# Remove one of each
my_collection.remove_item("movie", "Black Panther")
my_collection.remove_item("game", "Madden NFL 24")

# Display updates
print("\n--- Updated Movies ---")
my_collection.display_movies()

print("\n--- Updated Games ---")
my_collection.display_video_games()

# Show favorites
print("\n--- Favorites ---")
print(f"Favorite Movie: {my_collection.favMovie}")
print(f"Favorite Game: {my_collection.favGame}")
