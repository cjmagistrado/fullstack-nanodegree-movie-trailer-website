#!/usr/bin/env python
import fresh_tomatoes
import media

__author__ = "Christopher J Magistrado"
__credits__ = "Udacity"
__licens__ = "GPL"
__version__ = "1.0.0"
__email__ = "cjmagistrado@mail.com"
__status__ = "Prototype"

# This class is broken by Title, Year ,Movie rating
# Genre, Release date, Region, Star rating, Storyline,
# Director, Writer, Casts, Poster image, and YouTube Trailer.

boyhood = media.Movie(
    "Boyhood",
    "(2014)",
    2,
    "165 min",
    [0],
    "15 August 2014",
    "(USA)",
    "8.5",
    "The life of Mason, from early childhood to his arrival at college.",
    "Richard Linklater",
    "Richard Linklater",
    "Ellar Coltrane, Patricia Arquette, Ethan Hawke",
    "img/movies/boyhood.jpg",
    "https://www.youtube.com/watch?v=Y0oX0xiwOv8")

the_shawshank_redemption = media.Movie(
    "The Shawshank Redemption",
    "(1994)",
    2,
    "142 min",
    [1,0],
    "14 October 1994",
    "(USA)",
    "9.0",
    "Two imprisoned men bond over a number of years, finding solace and eventual \
    redemption through acts of common decency.",
    "Frank Darabont",
    "Stephen King, Frank Darabont",
    "Tim Robbins, Morgan Freeman, Bob Gunto",
    "img/movies/the_shawshank_redemption.jpg",
    "https://www.youtube.com/watch?v=NmzuHjWmXOc")
                                       
the_godfather = media.Movie(
    "The Godfather",
    "(1972)",
    2,
    "175 min",
    [1,0],
    "24 March 1972",
    "(USA)",
    "9.0",
    "The aging patriarch of an organized crime dynasty transfers control of his \
    clandestine empire to his reluctant son.",
    "Francis Ford Coppola",
    "Mario Puzo, Francis Ford Coppola",
    "Marlon Brando, Al Pacino, James Caan",
    "img/movies/the_godfather.jpg",
    "https://www.youtube.com/watch?v=YBrs0wvkPls")

the_godfather_2 = media.Movie(
    "The Godfather: Part II",
    "(1974)",
    2,
    "200 min",
    [1,0],
    "20 December 1974",
    "(USA)",
    "9.0",
    "The early life and career of Vito Corleone in 1920s New York is portrayed while his \
    son, Michael, expands and tightens his grip on his crime syndicate stretching from Lake \
    Tahoe, Nevada to pre-revolution 1958 Cuba.",
    "Francis Ford Coppola",
    "Francis Ford Coppola, Mario Puzo",
    "Al Pacino, Robert De Niro, Robert Duvall",
    "img/movies/the_godfather_2.jpg",
    "https://www.youtube.com/watch?v=qJr92K_hKl0")

the_dark_knight = media.Movie(
    "The Dark Knight",
    "(2008)",
    4,
    "152 min",
    [2,1,0],
    "18 July 2008",
    "(USA)",
    "9.0",
    "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, \
    the caped crusader must come to terms with one of the greatest psychological tests of his \
    ability to fight injustice.",
    "Christopher Nolan",
    "Jonathan Nolan, Christopher Nolan",
    "Christian Bale, Heath Ledger, Aaron Eckhart",
    "img/movies/the_dark_knight.jpg",
    "https://www.youtube.com/watch?v=yrJL5JxEYIw")

pulp_fiction = media.Movie(
    "Pulp Fiction",
    "(1994)",
    2,
    "154 min",
    [1,0],
    "14 October 1994",
    "(USA)",
    "9.0",
    "The lives of two mob hit men, a boxer, a gangster's wife, and a pair of diner bandits \
    intertwine in four tales of violence and redemption.",
    "Quentin Tarantino",
    "Quentin Tarantino, Roger Avary",
    "John Travolta, Uma Thurman, Samuel L. Jackson",
    "img/movies/pulp_fiction.jpg",
    "https://www.youtube.com/watch?v=ewlwcEBTvcg")

schindlers_list = media.Movie(
    "Schindler's List",
    "(1993)",
    2,
    "195 min",
    [5,0],
    "4 February 1994",
    "(USA)",
    "9.0",
    "In Poland during World War II, Oskar Schindler gradually becomes concerned for his \
    Jewish workforce after witnessing their persecution by the Nazis.",
    "Steven Spielberg",
    "Thomas Keneally, Steven Zaillian",
    "Liam Neeson, Ralph Fiennes, Ben Kingsley",
    "img/movies/schindlers_list.jpg",
    "https://www.youtube.com/watch?v=JdRGC-w9syA")

twelve_angry_men = media.Movie(
    "12 Angry Men",
    "(1957)",
    0,
    "96 min",
    [1,0],
    "April 1957",
    "(USA)",
    "9.0",
    "A dissenting juror in a murder trial slowly manages to convince the others that the \
    case is not as obviously clear as it seemed in court.",
    "Sidney Lumet",
    "Reginald Rose",
    "Henry Fonda, Lee J. Cobb, Martin Balsam",
    "img/movies/twelve_angry_men.jpg",
    "https://www.youtube.com/watch?v=fSG38tk6TpI")

the_good_bad_ugly = media.Movie(
    "The Good, the Bad and the Ugly",
    "(1966)",
    0,
    "161 min",
    [9],
    "23 December 1966",
    "(Italy)",
    "9.0",
    "A bounty hunting scam joins two men in an uneasy alliance against a third in a race \
    to find a fortune in gold buried in a remote cemetery.",
    "Sergio Leone",
    "Luciano Vincenzoni, Sergio Leone",
    "Clint Eastwood, Eli Wallach, Lee Van Cleef",
    "img/movies/the_good_bad_ugly.jpg",
    "https://www.youtube.com/watch?v=WCN5JJY_wiA")

the_lord_of_the_rings_the_return_of_the_king = media.Movie(
    "The Lord of the Rings: The Return of the King",
    "(2003)",
    4,
    "201 min",
    [3,4],
    "17 December 2003",
    "(USA)",
    "9.0",
    "Gandalf and Aragorn lead the World of Men against Sauron's army to draw his gaze from \
    Frodo and Sam as they approach Mount Doom with the One Ring.",
    "Peter Jackson",
    "J.R.R. Tolkien, Fran Walsh",
    "Elijah Wood, Viggo Mortensen, Ian McKellen",
    "img/movies/the_lord_of_the_rings_the_return_of_the_king.jpg",
    "https://www.youtube.com/watch?v=r5X-hFf6Bwo")

fight_club = media.Movie(
    "Fight Club",
    "(1999)",
    2,
    "139 min",
    [0],
    "15 October 1999",
    "(USA)",
    "9.0",
    "An insomniac office worker, looking for a way to change his life, crosses paths with a \
    devil-may-care soap maker, forming an underground fight club that evolves into something \
    much, much more...",
    "David Fincher",
    "Chuck Palahniuk, Jim Uhls",
    "Brad Pitt, Edward Norton, Helena Bonham Carter",
    "img/movies/fight_club.jpg",
    "https://www.youtube.com/watch?v=SUXWAEX2jlg")

the_lord_of_the_rings_the_fellowship_of_the_ring = media.Movie(
    "The Lord of the Rings: The Fellowship of the Ring",
    "(2001)",
    4,
    "178 min",
    [3,4],
    "19 December 2001",
    "(USA)",
    "8.5",
    "A meek hobbit of the Shire and eight companions set out on a journey to Mount Doom to destroy \
    the One Ring and the dark lord Sauron.",
    "Peter Jackson",
    "J.R.R. Tolkien, Fran Walsh",
    "Elijah Wood, Ian McKellen, Orlando Bloom",
    "img/movies/the_lord_of_the_rings_the_fellowship_of_the_ring.jpg",
    "https://www.youtube.com/watch?v=V75dMMIW2B4")

star_wars_ep_five_the_empire_strikes_back = media.Movie(
    "Star Wars: Episode V - The Empire Strikes Back",
    "(1980)",
    3,
    "124 min",
    [2,3,4],
    "20 June 1980",
    "(USA)",
    "8.5",
    "After the rebels have been brutally overpowered by the Empire on their newly established base, \
    Luke Skywalker takes advanced Jedi training with Master Yoda, while his friends are pursued by \
    Darth Vader as part of his plan to capture Luke.",
    "Irvin Kershner",
    "Leigh Brackett, Lawrence Kasdan",
    "Mark Hamill, Harrison Ford, Carrie Fisher",
    "img/movies/star_wars_ep_five_the_empire_strikes_back.jpg",
    "https://www.youtube.com/watch?v=JNwNXF9Y6kY")

forrest_gump = media.Movie(
    "Forrest Gump",
    "(1994)",
    4,
    "142 min",
    [0,10],
    "6 July 1994",
    "(USA)",
    "8.5",
    "Forrest Gump, while not intelligent, has accidentally been present at many historic moments, \
    but his true love, Jenny Curran, eludes him.",
    "Robert Zemeckis",
    "Winston Groom, Eric Roth",
    "Tom Hanks, Robin Wright, Gary Sinise",
    "img/movies/forrest_gump.jpg",
    "https://www.youtube.com/watch?v=YNh9Es8Ut6U")

inception = media.Movie(
    "Inception",
    "(2010)",
    4,
    "148 min",
    [2,5,6],
    "16 July 2010",
    "(USA)",
    "8.5",
    "A thief who steals corporate secrets through use of dream-sharing technology is given the \
    inverse task of planting an idea into the mind of a CEO.",
    "Christopher Nolan",
    "Christopher Nolan",
    "Leonardo DiCaprio, Joseph Gordon-Levitt, Ellen Page",
    "img/movies/inception.jpg",
    "https://www.youtube.com/watch?v=8hP9D6kZseM")

one_flew_over_the_cuckoos_nest = media.Movie(
    "One Flew Over the Cuckoo's Nest",
    "(1975)",
    2,
    "133 min",
    [0],
    "21 November 1975",
    "(USA)",
    "8.5",
    "Upon admittance to a mental institution, a brash rebel rallies the patients to take on the \
    oppressive head nurse.",
    "Milos Forman",
    "Lawrence Hauben, Bo Goldman",
    "Jack Nicholson, Louise Fletcher, Michael Berryman",
    "img/movies/one_flew_over_the_cuckoos_nest.jpg",
    "https://www.youtube.com/watch?v=bzNk3tjGwt8")

the_lord_of_the_rings_the_two_towers = media.Movie(
    "The Lord of the Rings: The Two Towers",
    "(2002)",
    4,
    "179 min",
    [3,4],
    "18 December 2002",
    "(USA)",
    "8.5",
    "While Frodo and Sam edge closer to Mordor with the help of the shifty Gollum, the divided \
    fellowship makes a stand against Sauron's new ally, Saruman, and his hordes of Isengard.",
    "Peter Jackson",
    "J.R.R. Tolkien, Fran Walsh",
    "Elijah Wood, Ian McKellen, Viggo Mortensen",
    "img/movies/the_lord_of_the_rings_the_two_towers.jpg",
    "https://www.youtube.com/watch?v=LbfMDwc4azU")

goodfellas = media.Movie(
    "Goodfellas",
    "(1990)",
    2,
    "146 min",
    [5,1,0],
    "21 September 1990",
    "(USA)",
    "8.5",
    "Henry Hill and his friends work their way up through the mob hierarchy.",
    "Martin Scorsese",
    "Nicholas Pileggi, Nicholas Pileggi",
    "Robert De Niro, Ray Liotta, Joe Pesci",
    "img/movies/goodfellas.jpg",
    "https://www.youtube.com/watch?v=qo5jJpHtI1Y")

the_matrix = media.Movie(
    "The Matrix",
    "(1999)",
    2,
    "136 min",
    [2,6],
    "31 March 1999",
    "(USA)",
    "8.5",
    "A computer hacker learns from mysterious rebels about the true nature of his reality and \
    his role in the war against its controllers.",
    "Andy Wachowski",
    "Andy Wachowski, Lana Wachowski",
    "Keanu Reeves, Laurence Fishburne, Carrie-Anne",
    "img/movies/the_matrix.jpg",
    "https://www.youtube.com/watch?v=m8e-FF8MsqU")

star_wars_ep_four_a_new_hope = media.Movie(
    "Star Wars: Episode IV - A New Hope",
    "(1977)",
    3,
    "121 min",
    [2,3,4],
    "25 May 1977",
    "(USA)",
    "8.5",
    "Luke Skywalker joins forces with a Jedi Knight, a cocky pilot, a wookiee and two droids \
    to save the universe from the Empire's world-destroying battle-station, while also attempting \
    to rescue Princess Leia from the evil Darth Vader.",
    "George Lucas",
    "George Lucas",
    "Mark Hamill, Harrison Ford, Carrie Fisher",
    "img/movies/star_wars_ep_four_a_new_hope.jpg",
    "https://www.youtube.com/watch?v=xioILbwDlEg")

seven_samurai = media.Movie(
    "Seven Samurai",
    "(1954)",
    1,
    "207 min",
    [0],
    "19 November 1956",
    "(USA)",
    "8.5",
    "A poor village under attack by bandits recruits seven unemployed samurai to help them defend themselves.",
    "Akira Kurosawa",
    "Akira Kurosawa, Shinobu Hashimoto",
    "Toshiro Mifune, Takashi Shimura, Keiko Tsushima",
    "img/movies/seven_samurai.jpg",
    "https://www.youtube.com/watch?v=xnRUHtSgJ9o")

city_of_god = media.Movie(
    "City of God",
    "(2002)",
    2,
    "130 min",
    [1,0],
    "13 February 2004",
    "(USA)",
    "8.5",
    "Two boys growing up in a violent neighborhood of Rio de Janeiro take different paths: one becomes a \
    photographer, the other a drug dealer.",
    "Fernanda Meirelles, Katia Lund",
    "Paulo Lins, Braulio Mantovani",
    "Alexandra Rodrigues, Matheus Nachtergaele, Leandro Firmino",
    "img/movies/city_of_god.jpg",
    "https://www.youtube.com/watch?v=dcUOO4Itgmw")

seven = media.Movie(
    "Se7en",
    "(1995)",
    2,
    "127 min",
    [0,7,8],
    "22 September 1995",
    "(USA)",
    "8.5",
    "Two detectives, a rookie and a veteran, hunt a serial killer who uses the seven deadly sins as his modus operandi.",
    "David Fincher",
    "Andrew Kevin Walker",
    "Morgan Freeman, Brad Pitt, Kevin Spacey",
    "img/movies/seven.jpg",
    "https://www.youtube.com/watch?v=TmZbLbPv6Fs")

the_silence_of_the_lambs = media.Movie(
    "The Silence of the Lambs",
    "(1991)",
    2,
    "118 min",
    [0,7,8],
    "14 February 1991",
    "(USA)",
    "8.5",
    "A young F.B.I. cadet must confide in an incarcerated and manipulative killer to receive his help on catching another \
    serial killer who skins his victims.",
    "Jonathan Demme",
    "Thomas Harris, Ted Tally",
    "Jodie Foster, Anthony Hopkins, Lawrence A. Bonney",
    "img/movies/the_silence_of_the_lambs.jpg",
    "https://www.youtube.com/watch?v=lQKs169Sl0I")

the_usual_suspects = media.Movie(
    "The Usual Suspects",
    "(1995)",
    2,
    "106 min",
    [1,0,8],
    "15 September 1995",
    "(USA)",
    "8.5",
    "A sole survivor tells of the twisty events leading up to a horrific gun battle on a boat, which begin when five \
    criminals meet at a seemingly random police lineup.",
    "Bryan Singer",
    "Christopher McQuarrie",
    "Kevin Spacey, Gabriel Byrne, Chazz Palminteri",
    "img/movies/the_usual_suspects.jpg",
    "https://www.youtube.com/watch?v=oiXdPolca5w")

inside_out = media.Movie(
    "Inside Out",
    "(2015)",
    3,
    "94 min",
    [3,11],
    "19 June 2015",
    "(USA)",
    "8.5",
    "After young Riley is uprooted from her Midwest life and moved to San Francisco, her emotions - Joy, Fear, Anger, \
    Disgust and Sadness - conflict on how best to navigate a new city, house, and school.",
    "Pete Docter, Ronaldo Del Carmen",
    "Pete Docter, Ronaldo Del Carmen",
    "Amy Poehler, Bill Hader, Lewis Black",
    "img/movies/inside_out.jpg",
    "https://www.youtube.com/watch?v=seMwpP0yeu4")

back_to_the_future = media.Movie(
    "Back to the Future",
    "(1985)",
    3,
    "116 min",
    [3,11,10],
    "3 July 1985",
    "(USA)",
    "8.5",
    "A young man is accidentally sent 30 years into the past in a time-traveling DeLorean invented by his friend, \
    Dr. Emmett Brown, and must make sure his high-school-age parents unite in order to save his own existence.",
    "Robert Zemeckis",
    "Robert Zemeckis, Bob Gale",
    "Michael J. Fox, Christopher Lloyd, Lea Thompson",
    "img/movies/back_to_the_future.jpg",
    "https://www.youtube.com/watch?v=qvsgGtivCgs")

life_is_beautiful = media.Movie(
    "Life Is Beautiful",
    "(1997)",
    4,
    "116 min",
    [11,0,10],
    "12 February 1999",
    "(USA)",
    "8.5",
    "When an open-minded Jewish librarian and his son become victims of the Holocaust, he uses a perfect \
    mixture of will, humor and imagination to protect his son from the dangers around their camp.",
    "Roberto Benigni",
    "Vincenzo Cerami, Roberto Benigni",
    "Roberto Benigni, Nicoletta Braschi, Giorgio Cantarini",
    "img/movies/life_is_beautiful.jpg",
    "https://www.youtube.com/watch?v=pAYEQP8gx3w")

ted = media.Movie(
    "Ted",
    "(2012)",
    2,
    "106 min",
    [11,4],
    "29 June 2012",
    "(USA)",
    "7.0",
    "As the result of a childhood wish, John Bennett's teddy bear, Ted, came to life and has been by \
    John's side ever since - a friendship that's tested when Lori, John's girlfriend of four years, wants \
    more from their relationship.",
    "Seth MacFarlane",
    "Seth MacFarlane, Alec Sulkin",
    "Mark Wahlberg, Mila Kunis, Seth MacFarlane",
    "img/movies/ted.jpg",
    "https://www.youtube.com/watch?v=9fbo_pQvU7M")

the_lone_ranger = media.Movie(
    "The Lone Ranger",
    "(2013)",
    4,
    "149 min",
    [2,3,9],
    "3 July 2013",
    "(USA)",
    "6.5",
    "Native American warrior Tonto recounts the untold tales that transformed John Reid, a man of the law, \
    into a legend of justice.",
    "Gore Verbinski",
    "Justin Haythe, Ted Elliot",
    "Johnny Depp, Armie Hammer, William Fichtner",
    "img/movies/the_lone_ranger.jpg",
    "https://www.youtube.com/watch?v=JjFsNSoDZK8")

slow_west = media.Movie(
    "Slow West",
    "(2015)",
    2,
    "84 min",
    [2,8,9],
    "16 April 2015",
    "(USA)",
    "7.0",
    "A young Scottish man travels across America in pursuit of the woman he loves, attracting the attention \
    of an outlaw who is willing to serve as a guide.",
    "John Maclean",
    "John Maclean",
    "Kodi Smit-McPhee, Michael Fassbender, Ben Mendelsohn",
    "img/movies/slow_west.jpg",
    "https://www.youtube.com/watch?v=pFfsTsdJfF8")

# This is the movies list
movies = [
    boyhood, the_shawshank_redemption, the_godfather,
    the_godfather_2, the_dark_knight, pulp_fiction,
    schindlers_list, twelve_angry_men, the_good_bad_ugly,
    the_lord_of_the_rings_the_return_of_the_king, fight_club,
    the_lord_of_the_rings_the_fellowship_of_the_ring,
    star_wars_ep_five_the_empire_strikes_back, forrest_gump,
    inception, one_flew_over_the_cuckoos_nest,
    the_lord_of_the_rings_the_two_towers, goodfellas,
    the_matrix, star_wars_ep_four_a_new_hope, seven_samurai,
    city_of_god, seven, the_silence_of_the_lambs,
    the_usual_suspects, inside_out, back_to_the_future,
    life_is_beautiful, ted, the_lone_ranger, slow_west
    ]

# This function generates and opens the page
fresh_tomatoes.open_movies_page(movies)
