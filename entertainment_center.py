import media
import fresh_tomatoes

# media.py uses the information below to make an educational web page about 
# the movies provided. The information provided is given in order as follows:
# movie title, IMDb rating out of 10, plot summary, director, starring actors,
# movie poster link, and YouTube link to movie trailer.

the_avengers = media.Movie(
                           "The Avengers",
                           "8.1",
                           "Earth's mightiest heroes must come together and \
                            learn to fight as a team if they are to stop the \
                            mischievous Loki and his alien army from \
                            enslaving humanity.",
                           "Joss Whedon",
                           "Robert Downey Jr., Chris Evans, Scarlett Johansson \
                            and more.",
                           "https://upload.wikimedia.org/wikipedia/en/thumb/f/f9/TheAvengers2012Poster.jpg/220px-TheAvengers2012Poster.jpg",  # noqa
                           "https://www.youtube.com/watch?v=eOrNdBpGMv8")
thor = media.Movie(
                   "Thor",
                   "7.0",
                   "The powerful but arrogant god Thor is cast out of Asgard \
                   to live amongst humans in Midgard (Earth), where he soon \
                   becomes one of their finest defenders.",
                   "Kenneth Branagh",
                   "Chris Hemsworth, Anthony Hopkins, Natalie Portman and \
                   more.",
                   "https://upload.wikimedia.org/wikipedia/en/thumb/f/fc/Thor_poster.jpg/220px-Thor_poster.jpg",  # noqa
                   "https://www.youtube.com/watch?v=JOddp-nlNvQ")
iron_man = media.Movie(
                       "Iron Man",
                       "7.9",
                       "After being held captive in an Afghan cave, an \
                       industrialist creates a unique weaponized suit of \
                       armor to fight evil.",
                       "Jon Favreau",
                       "Robert Downey Jr., Gwyneth Paltrow, Terrence Howard \
                       and more.",
                       "https://upload.wikimedia.org/wikipedia/en/thumb/7/70/Ironmanposter.JPG/220px-Ironmanposter.JPG",  # noqa
                       "https://www.youtube.com/watch?v=8hYlB38asDY")
the_hulk = media.Movie(
                       "The Incredible Hulk",
                       "6.9",
                       "Bruce Banner, a scientist on the run from the U.S. \
                       Government must find a cure for the monster he emerges \
                       whenever he loses his temper. However, Banner then \
                       must fight a soldier whom unleashes himself as a \
                       threat stronger than he.",
                       "Louis Leterrier",
                       "Edward Norton, Liv Tyler, Tim Roth, Tim Blake Nelson, \
                       Ty Burrell, William Hurt",
                       "http://www.freemovieposters.net/posters/incredible_hulk_the_2008_352_poster.jpg",  # noqa
                       "https://www.youtube.com/watch?v=xbqNb2PFKKA")
captain_america = media.Movie(
                              "Captain America",
                              "6.8",
                              "Steve Rogers, a rejected military soldier \
                              transforms into Captain America after taking a \
                              dose of a Super-Soldier serum. But being \
                              Captain America comes at a price as he \
                              attempts to take down a war monger and a \
                              terrorist organization.",
                              "Joe Johnston",
                              "Chris Evans, Hugo Weaving, Samuel L. Jackson \
                              and more.",
                              "https://upload.wikimedia.org/wikipedia/en/thumb/3/37/Captain_America_The_First_Avenger_poster.jpg/220px-Captain_America_The_First_Avenger_poster.jpg",  # noqa
                              "https://www.youtube.com/watch?v=JerVrbLldXw")
agents_of_shield = media.Movie(
                              "Agents of Shield",
                               "7.5",
                               "The missions of the Strategic Homeland \
                               Intervention, Enforcement and Logistics \
                               Division.",
                               "Maurissa Tancharoen, Jed Whedon, Joss Whedon",
                               "Clark Gregg, Ming-Na Wen, Brett Dalton and \
                               more.",
                               "http://www.gstatic.com/tv/thumb/tvbanners/9975633/p9975633_b_v7_aj.jpg",  # noqa
                               "https://www.youtube.com/watch?v=T3T-evQZiQo")


movies = [the_avengers, thor, iron_man, the_hulk, captain_america,
          agents_of_shield]
# These movies are listed here so fresh_tomatoes.py can display info for each
# movie without me typing all this information out again. I can also select 
# what pieces of information I wish to display using code like {movie_director}
# on fresh_tomatoes.py.
fresh_tomatoes.open_movies_page(movies)
# This line allows my code to open a new browser window and display the above
# information using the style guidelines included in fresh_tomatoes.py.
