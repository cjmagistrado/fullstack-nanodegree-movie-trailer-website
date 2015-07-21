import webbrowser
import os
import re

# The main page layout, title bar, styles and scripting for the page
main_page_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>
    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <link rel="stylesheet" href="style.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <script src="main.js"></script>
</head>
<body>
<!-- Trailer Video Modal -->
<div class="modal" id="trailer">
    <div class="modal-dialog">
        <div class="modal-content">
            <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
                <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
            </a>
            <div class="scale-media" id="trailer-video-container"></div>
        </div>
    </div>
</div>   
<!-- Main Page Content -->
<div class="container">
    <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
            <div class="navbar-header">
                <a class="navbar-brand" href="#">Fresh Tomatoes Movie Trailers</a>
            </div>
        </div>
    </div>
</div>
<div id="main-section" class="container"></div>
<!-- Genre Section -->
<div id="genre-section" class="container">
    <div id="genre-tile-all" data-genre="All" class="col-md-4 col-lg-4 genre-tile text-center">
        <div id="genre-icon-all" class="genre-icon" role="img"></div>
        <h2>All</h2>
    </div>
    <div id="genre-tile-drama" data-genre="Drama" class="col-md-4 col-lg-4 genre-tile text-center">
        <div id="genre-icon-drama" class="genre-icon" role="img"></div>
        <h2>Drama</h2>
    </div>
    <div id="genre-tile-crime" data-genre="Crime" class="col-md-4 col-lg-4 genre-tile text-center">
        <div id="genre-icon-crime" class="genre-icon" role="img"></div>
        <h2>Crime</h2>
    </div>
    <div id="genre-tile-action" data-genre="Action" class="col-md-4 col-lg-4 genre-tile text-center">
        <div id="genre-icon-action" class="genre-icon" role="img"></div>
        <h2>Action</h2>
    </div>
    <div id="genre-tile-adventure" data-genre="Adventure" class="col-md-4 col-lg-4 genre-tile text-center">
        <div id="genre-icon-adventure" class="genre-icon" role="img"></div>
        <h2>Adventure</h2>
    </div>
    <div id="genre-tile-fantasy" data-genre="Fantasy" class="col-md-4 col-lg-4 genre-tile text-center">
        <div id="genre-icon-fantasy" class="genre-icon" role="img"></div>
        <h2>Fantasy</h2>
    </div>
    <div id="genre-tile-biography" data-genre="Biography" class="col-md-4 col-lg-4 genre-tile text-center">
        <div id="genre-icon-biography" class="genre-icon" role="img"></div>
        <h2>Biography</h2>
    </div>
    <div id="genre-tile-sci-fi" data-genre="Sci-Fi" class="col-md-4 col-lg-4 genre-tile text-center">
        <div id="genre-icon-sci-fi" class="genre-icon" role="img"></div>
        <h2>Sci-Fi</h2>
    </div>
    <div id="genre-tile-mystery" data-genre="Mystery" class="col-md-4 col-lg-4 genre-tile text-center">
        <div id="genre-icon-mystery" class="genre-icon" role="img"></div>
        <h2>Mystery</h2>
    </div>
    <div id="genre-tile-thriller" data-genre="Thriller" class="col-md-4 col-lg-4 genre-tile text-center">
        <div id="genre-icon-thriller" class="genre-icon" role="img"></div>
        <h2>Thriller</h2>
    </div>
    <div id="genre-tile-western" data-genre="Western" class="col-md-4 col-lg-4 genre-tile text-center">
        <div id="genre-icon-western" class="genre-icon" role="img"></div>
        <h2>Western</h2>
    </div>
    <div id="genre-tile-romance" data-genre="Romance" class="col-md-4 col-lg-4 genre-tile text-center">
        <div id="genre-icon-romance" class="genre-icon" role="img"></div>
        <h2>Romance</h2>
    </div>
    <div id="genre-tile-comedy" data-genre="Comedy" class="col-md-4 col-lg-4 genre-tile text-center">
        <div id="genre-icon-comedy" class="genre-icon" role="img"></div>
        <h2>Comedy</h2>
    </div>
</div>
<!-- Info Section -->
<div id="info-section" class="container">
    <div class="col-md-12">
        <div class="btn-back" data-to="movies" role="button">Back</div>
    </div>
    <div class="col-md-3">
        <img id="info-movie-img" class="movie-img" src="" width="220" height="342">
    </div>
    <div class="col-md-9">
        <h2><span id="movie-title"></span> <span id="movie-year"></span></h2>
        <div class="sub-info main-text"><span id="movie-rating"></span> | <span id="movie-duration"></span> | <span id="movie-genre"></span> | <span id="movie-date"></span> <span id="movie-location"></span></div>
        <div id="movie-star-rating" class="movie-rating main-text"></div>
        <div id="movie-storyline" class="main-text">The life of Mason, from early childhood to his arrival at college.</div>
        <div class="main-text">
            <strong>Director:</strong> <span id="movie-director"></span>
        </div>
        <div class="main-text">
            <strong>Writer:</strong> <span id="movie-writer"></span>
        </div>
        <div class="main-text">
            <strong>Cast:</strong> <span id="movie-casts"></span>
        </div>
        <div id="btn-watch-trailer" role="button" data-trailer-youtube-id="" data-toggle="modal" data-target="#trailer">Watch Trailer</div>
    </div>
</div>
</body>
</html>
{movie_data}
<script src="preload.js"></script>
'''

# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="220" height="342">
    <h2>{movie_title}</h2>
</div>
'''

# Movie entry javascript template
movie_data_push_object = '''<script> movies.push({movie_data_content}); </script>'''

def push_movie_data(movies):
    # Append movie content
    script = ''
    for movie in movies:
        script += movie_data_push_object.format(
            movie_data_content = ' { title : "'+movie.title+'", year : "'+movie.year+'", movie_rating : "'+movie.movie_rating+'", duration : "'+movie.duration+'", genre : '+str(movie.genre)+', date : "'+movie.date+'", location : "'+movie.location+'", star_rating : "'+movie.star_rating+'", storyline : "'+movie.storyline+'", director : "'+movie.director+'", writer : "'+movie.writer+'", casts : "'+movie.casts+'", image_url : "'+movie.poster_image_url+'", trailer : "'+movie.trailer_youtube_url+'" } '
        )
    return script

def open_movies_page(movies):
  # Create or overwrite the output file
  output_file = open('index.html', 'w')

  # Replace the placeholder for the movie tiles with the actual dynamically generated content
  rendered_content = main_page_content.format(movie_data=push_movie_data(movies))

  # Output the file
  output_file.write(rendered_content)
  output_file.close()

  # open the output file in the browser
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://' + url, new=2) # open in a new tab, if possible
