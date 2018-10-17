# import the media.py file to create an insatnce of the class
import media
# import fresh_tomatoes.py file to create a web page
import fresh_tomatoes

# create the first instance with four arguments
a_gentleman = media.Movie(
             "A Gentleman",
             "Miami-based Gaurav wants to marry his girlfriend Kavya " +
             "but she wants her partner to be more adventurous." +
             "When he goes on an assignment to Mumbai, he is mistaken " +
             "for Rishi, who works for a spy unit",
             "https://upload.wikimedia.org/wikipedia/en/c/c6/A_Gentleman.jpg",
             "https://www.youtube.com/watch?v=IMXifj-peiQ")

# create the second instance of the class/adding a new movie
commando = media.Movie(
    "Commando: A One Man Army",
    "The Chinese government incarcerates Karan, " +
    "an Indian commando,accusing him of being  Indian spy,after he survives" +
    "a plane crash in their " +
    "territory. He must fight to clear his name.",
    "https://upload.wikimedia.org/wikipedia/en/d/d4/" +
    "Commando_%282013_film%29.jpg",
    "https://www.youtube.com/watch?v=sLIs-4oM3m4")

# create the third instance of a class/adding a new movie
never_back_down = media.Movie(
    "Never Back Down",
    "The new high school proves to be more trouble than he " +
    "reckoned when Jake's friends and family face a threat." +
    " He seeks the mentoring of a mixed martial arts " +
    "veteran to train him for a final fight.",
    "https://upload.wikimedia.org/wikipedia/en/3/39/Never_back_down.jpg",
    "https://www.youtube.com/watch?v=s8aGqjNM0k4")

# create fourth instance of a class/adding a new movie
deadpool_2 = media.Movie(
    "Deadpool 2", "Foul-mouthed mutant mercenary Wade Wilson(AKA. Deadpool)," +
    " brings together a team of fellow mutant rogues to" +
    " protect a young boy with supernatural abilities from " +
    "the brutal, time-traveling cyborg, Cable. ",
    "https://upload.wikimedia.org/wikipedia/en/c/cf/Deadpool_2_poster.jpg",
    "https://www.youtube.com/watch?v=D86RtevtfrA")

# create fifth instance of a class /adding a new movie
twilight = media.Movie(
    "Twilight",
    "A teenage girl risks everything when she falls in love with a vampire.",
    "https://upload.wikimedia.org/wikipedia/en/b/b6/" +
    "Twilight_%282008_film%29_poster.jpg",
    "https://www.youtube.com/watch?v=fFLrRlPBg0A")

# create sixth instance of a class /adding a new movie
enter_the_dragon = media.Movie(
    "Enter the Dragon",
    "A martial artist agrees to spy on a reclusive crime lord using his " +
    "invitation to a tournament there as cover.",
    "https://upload.wikimedia.org/wikipedia/en/e/ef/Enter_the_dragon.jpg",
    "https://www.youtube.com/watch?v=81jCPIag4KA")


# make a list to store the names of all the movies
movies = [never_back_down, twilight, a_gentleman, deadpool_2,
          commando, enter_the_dragon]

# use the open_movies_page function from fresh_tomatoes.py
# and pass the movie list as an argument
fresh_tomatoes.open_movies_page(movies)
