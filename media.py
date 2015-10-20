import webbrowser


class Movie:
    """This class stores movie information."""
# information about each movie is located in entertainment_center.py
    def __init__(self, movie_title, movie_reviews, movie_storyline,
                 movie_director, movie_actors, poster_image, trailer_youtube):
        self.title = movie_title
        self.reviews = movie_reviews
        self.storyline = movie_storyline
        self.director = movie_director
        self.actors = movie_actors
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
