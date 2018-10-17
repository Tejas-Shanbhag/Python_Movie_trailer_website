# create a class Movie which can be further used to create instances
class Movie():
    # create a constructor and pass four parameters in the __init__ method
    def __init__(self, movie_title, movie_story, movie_image, movie_trailer):
        self.title = movie_title
        self.storyline = movie_story
        self.poster_image_url = movie_image
        self.trailer_youtube_url = movie_trailer
        

        
