# CreateClass.py

class Collection:
    def __init__(self):
        self.movieList = []
        self.gameList = []
        self.favMovie = None
        self.favGame = None

    # 1. Display all movies
    def display_movies(self):
        print("Movies:")
        for movie in self.movieList:
            print(f"- {movie}")

    # 2. Display all video games
    def display_video_games(self):
        print("Video Games:")
        for game in self.gameList:
            print(f"- {game}")

    # 3. Add a movie or video game
    def add_item(self, item_type, item_name):
        if item_type == "movie":
            self.movieList.append(item_name)
        elif item_type == "game":
            self.gameList.append(item_name)
        else:
            print("Please choose 'movie' or 'game'.")

    # 4. Remove a movie or video game
    def remove_item(self, item_type, item_name):
        if item_type == "movie":
            if item_name in self.movieList:
                self.movieList.remove(item_name)
            else:
                print("Movie not found.")
        elif item_type == "game":
            if item_name in self.gameList:
                self.gameList.remove(item_name)
            else:
                print("Game not found.")
        else:
            print("Please choose 'movie' or 'game'.")

    # 5. Set favorite movie or game
    def set_favorite(self, item_type, item_name):
        if item_type == "movie":
            if item_name in self.movieList:
                self.favMovie = item_name
            else:
                print("Movie not found.")
        elif item_type == "game":
            if item_name in self.gameList:
                self.favGame = item_name
            else:
                print("Game not found.")
        else:
            print("Please choose 'movie' or 'game'.")
