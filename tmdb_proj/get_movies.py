import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tmdb_proj.settings")

import django
django.setup()

from django.core.management import call_command

import requests
from tmdb_projapp.models import Movie

from dotenv import load_dotenv

# TMDb API URL and API key
API = os.getenv("API")
URL = 'https://api.themoviedb.org/3/discover/movie'


def fetch_and_save_movies():
    # Fetch data from the API
    response = requests.get(URL, params={'api_key': API})
    
    if response.status_code != 200:
        print(f"Error fetching data from API: {response.status_code}")
        return

    data = response.json()

    # Loop through the results and save to the database
    for movie_data in data.get('results', []):
        try:
            Movie.objects.create(
                adult=movie_data.get('adult', False),
                backdrop_path=movie_data.get('backdrop_path'),
                genre_ids=movie_data.get('genre_ids'),
                movie_id=movie_data.get('id'),  # Mapping 'id' from API to 'movie_id'
                original_language=movie_data.get('original_language'),
                original_title=movie_data.get('original_title'),
                overview=movie_data.get('overview'),
                popularity=movie_data.get('popularity'),
                poster_path=movie_data.get('poster_path'),
                release_date=movie_data.get('release_date'),
                title=movie_data.get('title'),
                video=movie_data.get('video', False),
                vote_average=movie_data.get('vote_average'),
                vote_count=movie_data.get('vote_count'),
            )
            print(f"Saved movie: {movie_data.get('title')}")
        except Exception as e:
            print(f"Error saving movie {movie_data.get('title')}: {e}")

    print("Movies have been successfully saved to the database!")


# Run the function
if __name__ == "__main__":
    fetch_and_save_movies()


