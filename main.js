
// initialize movies array
var movies = [];

// preload images
var preload = function(array){
    var images = [];
    $(array).each(function(i){
        images[i] = new Image();
        images[i].src = array[i];
	   });
};

// Pause the video when the modal is closed
$(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
    // Remove the src so the player itself gets removed, as this is the only
    // reliable way to ensure the video stops playing in IE
    $("#trailer-video-container").empty();
});

// Start playing the video whenever the trailer modal is opened
$(document).on('click', '#btn-watch-trailer', function (event) {
    var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
    var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
    $("#trailer-video-container").empty().append($("<iframe></iframe>", {
        'id': 'trailer-video',
        'type': 'text-html',
        'src': sourceUrl,
        'frameborder': 0
    }));
});

// Back button when clicked
$(document).on('click', '.btn-back', function(event) {
    var to = event.currentTarget.dataset.to;
    switch (to) {
        case "genres":
            $('#main-section').fadeOut(500);
            setTimeout(function() {
                $('#genre-section').fadeIn(500);
            }, 1000);
            break;
        case "movies":
            $('#info-section').fadeOut(500);
            setTimeout(function() {
                $('#main-section').fadeIn(500);
            }, 1000);
            break;
        default:
            break;
    }
});

// Select movie genre
$(document).on('click', '.genre-tile', function (event) {
    var genre = event.currentTarget.dataset.genre;
    $('#genre-section').fadeOut(500);
    load(genre);
});

// To movie info section
$(document).on('click', '.movie-tile', function(event) {
    $('#main-section').fadeOut(500);
    setTimeout(function() {
        $('#info-section').fadeIn(500);
    }, 1000);
    updateInfo(getMovie(event.currentTarget.dataset.title));
});

// Get movie info
var getMovie = function(title) {
    for (movie in movies) {
        if (title === movies[movie].title) {
            return movies[movie];
        }
    }
};

// Update movie info in info section
var updateInfo = function(movie) {
    // update movie poster image
    $('#info-movie-img').attr('src', movie.image_url);
    // update movie title
    $('#movie-title').text(movie.title);
    // update movie year
    $('#movie-year').text(movie.year);
    // update movie rating
    $('#movie-rating').text(movie.movie_rating);
    // update movie length
    $('#movie-duration').text(movie.duration);
    // update movie genre
    var genre = movie.genre.toString();
    genre = genre.replace(/,/g,", ");
    $('#movie-genre').text(genre);
    // update movie date
    $('#movie-date').text(movie.date);
    // update movie location
    $('#movie-location').text(movie.location);
    // update movie star rating
    var star_rating = movie.star_rating;
    var core_rating = star_rating.charAt(0);
    var half_rating = parseInt(star_rating.charAt(2));
    var i;
    $('#movie-star-rating').empty();
    for (i = 0; i < core_rating; i++) {
        $('#movie-star-rating').append('<div class="star"></div>');
    }
    if (half_rating) {
        $('#movie-star-rating').append('<div class="star-half"></div>');
        i++;
    }
    while (i < 10) {
        $('#movie-star-rating').append('<div class="star-empty"></div>');
        i++;
    }
    $('#movie-star-rating').append('<span>'+star_rating+'</span>');
    // update movie storyline
    $('#movie-storyline').text(movie.storyline);
    // update movie director
    $('#movie-director').text(movie.director);
    // update movie writer
    $('#movie-writer').text(movie.writer);
    // update movie casts
    $('#movie-casts').text(movie.casts);
    // update movie trailer
    var youtubeID = movie.trailer.split('v=')[1];
    $('#btn-watch-trailer').attr('data-trailer-youtube-id', youtubeID);
};

// Load movies
var load = function(genre) {
    setTimeout(function() {
        $('#main-section').show();
        listMovies(genre, function() {
            $('.movie-tile').hide().first().show("fast", function showNext() {
                $(this).next("div").show("fast", showNext);
            });
        });
    }, 1000);
};

// Append movies
var listMovies = function(genre, callback) {
 
    $('#main-section').empty();
 
    $('#main-section').append(
    '<div class="col-md-12">'+
        '<div class="btn-back" data-to="genres" role="button">Back</div>'+
    '</div>'
    );
    
    if (genre === "All") {
        for (movie in movies) {
            $('#main-section').append(
            '<div class="col-md-6 col-lg-4 movie-tile text-center">'+
                '<img src="'+movies[movie].image_url+'" class="movie-img" width="220" height="342">'+
                '<h2>'+movies[movie].title+'</h2>'+
            '</div>'
            )
        }
    }else{
        for (movie in movies) {
            for (var i = 0; i < movies[movie].genre.length; i++) {
                if (genre === movies[movie].genre[i]) {
                    $('#main-section').append(
                    '<div class="col-md-6 col-lg-4 movie-tile text-center" data-title="'+movies[movie].title+'">'+
                        '<img src="'+movies[movie].image_url+'" class="movie-img" width="220" height="342">'+
                        '<h2>'+movies[movie].title+'</h2>'+
                    '</div>'
                    );
                }
            }
        }
    }
    callback();
};