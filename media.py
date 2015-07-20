import webbrowser

class Movie():

    VALID_RATINGS = ["Not Rated","Unrated","R","PG","PG-13"]
    GENRES = ["Drama","Crime","Action","Adventure","Fantasy","Biography","Sci-Fi","Mystery","Thriller","Western","Romance","Comedy"]

    def __init__(self, movie_title, movie_year, movie_rate, movie_duration, movie_genre, movie_date, movie_location, star_rate, movie_storyline, movie_director, movie_writer, movie_casts, poster_image, trailer_youtube):
        self.title = movie_title
        self.year = movie_year
        self.movie_rating = self.VALID_RATINGS[movie_rate]
        self.duration = movie_duration

        #Get genre(s)
        genre_list = []
        for genre in movie_genre:
            genre_list.append(self.GENRES[genre])
        
        self.genre = genre_list
        self.date = movie_date
        self.location = movie_location
        self.star_rating = star_rate
        self.storyline = movie_storyline
        self.director = movie_director
        self.writer = movie_writer
        self.casts = movie_casts
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
