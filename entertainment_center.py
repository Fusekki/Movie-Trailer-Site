import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

#print(toy_story.storyline)
avatar = media.Movie("Avatar",
                     "A maring on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=-9ceBgWV8io")
#print(avatar.storyline)
#avatar.show_trailer()

last_jedi = media.Movie("Star Wars Episode VIII: The Last Jedi",
                     "The next chapter in the Skywalker saga arrives December 2017",
                     "https://cdn.vox-cdn.com/uploads/chorus_asset/file/8341575/star_wars_the_last_jedi_poster_1688.jpg",
                     "https://www.youtube.com/watch?v=zB4I68XVPzQ")
#print(last_jedi.storyline)
#last_jedi.show_trailer()

school_of_rock = media.Movie("School of Rock",
                     "Using rock music to learn",
                     "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                     "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille",
                     "A rat is a chef in Paris",
                     "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                     "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris",
                     "Going back in time to meet authors",
                     "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                     "https://www.youtube.com/watch?v=FAfR8omt-CY")

hunger_games = media.Movie("Hunger Games",
                     "A really real reality show",
                     "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                     "https://www.youtube.com/watch?v=PbA63a7H0bo")

movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]
fresh_tomatoes.open_movies_page(movies)

