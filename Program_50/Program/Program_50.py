# Import TMDb from tmdbv3api module using the import keyword 
from tmdbv3api import TMDb
# Import Movie from tmdbv3api module using the import keyword 
from tmdbv3api import Movie
# Initialize the TMDb object and store it in a variable 
tmdbobj=TMDb()
# Set your unique API key, which you'll receive when registering with TMDB;
# Here, this is my API key.
TMDb.api_key= '6f15568d9aa3d15d0261a5454578c28b'
# Using the export command below, you may also export your API key as an environment variable.
# commnad:- export TMDb_API_KEY= '6f15568d9aa3d15d0261a5454578c28b'
# Apply language attribute to the above tmdb object to specify the 
# language of the data must be get from TMDB. It is optional.
tmdbobj.language = 'en'
# Set debug to True to make it enable for debugging.
tmdbobj.debug = True
# Initialize the Movie object and store it in another variable 
movieobj=Movie() 
# Pass movie_id to the similar() function to fetch similar movies data using movie_id 
# Store it in another variable 
similarmovies = movieobj.similar(343611)
# Loop in all the above similar movies and fetch the movie data using the for loop
for movie in similarmovies:
    # Get the required data you want using the corresponding attributes.
    # Here, print the title of the movie using the title attribute
    print("Title of the movie: ", movie.title)
    # Print the overview of the movie using the overview attribute
    print("Overview of the movie:", movie.overview)
    # Print the Poster of the movie using the poster_path attribute
    print("Poster of the Movie:", movie.poster_path)