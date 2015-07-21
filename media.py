#!/usr/bin/env python
import webbrowser

__author__ = "Christopher J Magistrado"
__credits__ = "Udacity"
__licens__ = "GPL"
__version__ = "1.0.0"
__email__ = "cjmagistrado@mail.com"
__status__ = "Prototype"

# This class is used for a Movie Trailer Website
class Movie():

    # List of movie ratings
    VALID_RATINGS = [
        "Not Rated",
        "Unrated","R",
        "PG","PG-13"
        ]

    # List of movie genres
    GENRES = [
        "Drama","Crime",
        "Action","Adventure",
        "Fantasy","Biography",
        "Sci-Fi","Mystery","Thriller",
        "Western","Romance","Comedy"
        ]

    # Initiate
    def __init__(
        self, movie_title, movie_year,
        movie_rate, movie_duration, movie_genre,
        movie_date, movie_location, star_rate,
        movie_storyline, movie_director, movie_writer,
        movie_casts, poster_image, trailer_youtube
        ):
            # Title
            self.title = movie_title
            # Year
            self.year = movie_year
            # Movie Rating
            self.movie_rating = self.VALID_RATINGS[movie_rate]
            # Length
            self.duration = movie_duration

            #Get genre(s)
            genre_list = []
            for genre in movie_genre:
            genre_list.append(self.GENRES[genre])

            # Genre
            self.genre = genre_list
            # Release Date
            self.date = movie_date
            # Region
            self.location = movie_location
            # Star Rating
            self.star_rating = star_rate
            # Storyline
            self.storyline = movie_storyline
            # Director
            self.director = movie_director
            # Writer
            self.writer = movie_writer
            # Casts
            self.casts = movie_casts
            # Poster Image
            self.poster_image_url = poster_image
            # YouTube Trailer
            self.trailer_youtube_url = trailer_youtube

    # Shows movie trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
