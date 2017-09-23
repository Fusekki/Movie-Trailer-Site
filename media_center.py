import media
import fresh_tomatoes

# Movie instance - Desplicable Me
despicable_me = media.Movie("Despicable Me 3",
                            "Gru meets his long-lost charming, cheerful, "
                            "and more successful twin brother Dru who wants "
                            "to team up with him for one last criminal heist.",
                            "https://movies.universalpictures.com/media/dm3"
                            "-adv1sheet-rgb-5-58c818a68f809-1.png",
                            "https://www.youtube.com/watch?v=6DBi41reeF0")
# Movie instance - Kingsman
kingsman = media.Movie("Kingsman",
                       "When their headquarters are destroyed and the world "
                       "is held hostage, the Kingsman's journey leads them "
                       "to the discovery of an allied spy organization in "
                       "the US. These two elite secret organizations must "
                       "band together to defeat a common enemy.",
                       "https://images-na.ssl-images-amazon.com/images/M"
                       "/MV5BNTBlOWZhZTctOTY0MC00Y2QyLTljMmYtZDkxZDFlMWU4"
                       "Y2EyXkEyXkFqcGdeQXVyNDg2MjUxNjM@._V1_UY1200_CR90,"
                       "0,630,1200_AL_.jpg",
                       "https://www.youtube.com/watch?v=6Nxc-3WpMbg")
# Movie instance - Atomic Blonde
atomic_blonde = media.Movie("Atomic Blonde",
                            "An undercover MI6 agent is sent to Berlin "
                            "during the Cold War to investigate the murder "
                            "of a fellow agent and recover a missing list of "
                            "double agents.",
                            "https://posterspy.com/wp-content/uploads/2017"
                            "/03/Atomic-Blonde-MD-Posters.jpg",
                            "https://www.youtube.com/watch?v=nI7HVnZlleo")
# Movie instance - Dunkirk
dunkirk = media.Movie("Dunkirk",
                      "Allied soldiers from Belgium, the British Empire, "
                      "Canada, and France are surrounded by the German army "
                      "and evacuated during a fierce battle in World War II.",
                      "http://cdn1-www.comingsoon.net/assets/uploads/gallery"
                      "/dunkirk/dunkirk.jpg",
                      "https://www.youtube.com/watch?v=F-eMt3SrfFU")
# Movie instance - Blade Runner
blade_runner = media.Movie("Blade Runner 2049",
                           "Thirty years after the events of the first film, "
                           "a new blade runner, LAPD Officer K (Ryan "
                           "Gosling), unearths a long-buried secret that has "
                           "the potential to plunge what's left of society "
                           "into chaos. K's discovery leads him on a quest "
                           "to find Rick Deckard (Harrison Ford), a former "
                           "LAPD blade runner who has been missing for 30 "
                           "years.",
                           "http://www.impawards.com/2017/posters/"
                           "blade_runner_twenty_forty_nine_ver3_xlg.jpg",
                           "https://www.youtube.com/watch?v=gCcx85zbxz4")
# Movie instance - The Last Jedi
last_jedi = media.Movie("The Last Jedi",
                        "The next chapter in the Skywalker saga arrives "
                        "December 2017",
                        "https://cdn.vox-cdn.com/uploads/chorus_asset/file"
                        "/8341575/star_wars_the_last_jedi_poster_1688.jpg",
                        "https://www.youtube.com/watch?v=zB4I68XVPzQ")

movies = [despicable_me, kingsman, atomic_blonde, dunkirk, blade_runner,
          last_jedi]
# display the movies in a web page.
fresh_tomatoes.open_movies_page(movies)
