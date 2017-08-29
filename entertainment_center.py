import fresh_tomatoes
import media

#Movie information being defined to be display on website.

hunger_games = media.Reel("The Hunger Games",
                           "The Hunger Games is a trilogy of young adult dystopian novels.",
                           "https://upload.wikimedia.org/wikipedia/en/4/4b/Hunger_Games_Film_Poster.jpg",
                           "https://www.youtube.com/watch?v=LrXIG4oK7Ew")


friday = media.Reel("Friday",
                           "The film takes a look at one single Friday in the life of two friends, in South Central Los Angeles",
                           "https://upload.wikimedia.org/wikipedia/en/2/27/Fridayposter1995.jpg",
                           "https://www.youtube.com/watch?v=umvFBoLOOgo")


gladiator = media.Reel("Gladiator",
                           "Story of a roman soldier who seeks to avenge his families death",
                           "https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg",
                           "https://www.youtube.com/watch?v=Q-b7B8tOAQU")



history_of_the_world = media.Reel("History of the World",
                           "The film is a parody of the historical spectacular film genre anthology.",
                           "https://upload.wikimedia.org/wikipedia/en/5/59/History_of_the_World_poster.jpg",
                           "https://www.youtube.com/watch?v=AILiI6f83L8")



road_house = media.Reel("Road House",
                           "James Dalton is a professional specialized doorman  with a mysterious past who is enticed from his current job at a club in New York City to take over security at the Double Deuce.",
                           "https://upload.wikimedia.org/wikipedia/en/6/67/Road-house-poster.jpg",
                           "https://www.youtube.com/watch?v=oByMeAfwARs")



alien_covenant = media.Reel("Alien Covenant",
                           "Looking for civilization beguinings",
                           "https://upload.wikimedia.org/wikipedia/en/3/33/Alien_Covenant_Teaser_Poster.jpg",
                           "https://www.youtube.com/watch?v=svnAD0TApb8")


#Create movies container
movies = [hunger_games, friday, gladiator, history_of_the_world, road_house, alien_covenant]
#launches movie website
fresh_tomatoes.open_movies_page(movies)