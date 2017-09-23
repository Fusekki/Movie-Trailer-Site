import webbrowser


class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube_url):
        # Movie title
        self.title = movie_title
        # Movie Storyline
        self.storyline = movie_storyline
        # Movie Post Image
        self.poster_image_url = poster_image
        # Movie YouTube Trailer
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube)
