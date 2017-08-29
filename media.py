import webbrowser

class Reel():
	 #This is the object constructor, or sometimes called the initialiser of a movie object.
        def __init__(self,movie_title, movie_storyline, poster_image, trailer_youtube):
        	self.title = movie_title
        	self.storyline = movie_storyline
        	self.poster_image_url = poster_image
        	self.trailer_youtube_url = trailer_youtube

        def show_trailer(self):
        	""" This function activates the modal window that shows the trailer for the movies"""
        	webbrowser.open(self.trailer_youtube_url)
