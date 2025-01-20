import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tmdb_proj.settings")

import django
django.setup()

from tmdb_projapp.models import Movie
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def fetch_movies_data():
    # Query data from the Movie model
    queryset = Movie.objects.all().values(
        "title", "popularity", "vote_average", "release_date"
    )
    # Convert the queryset to a pandas DataFrame
    df = pd.DataFrame(queryset)
    print(df.head())  # Optional: Preview the data
    return df

def scatter_plot(df):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(
        data=df,
        x="popularity",
        y="vote_average",
        hue="vote_average",
        size="popularity",
        sizes=(20, 200),
    )
    plt.title("Popularity vs. Vote Average")
    plt.xlabel("Popularity")
    plt.ylabel("Vote Average")
    plt.legend(title="Vote Average", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()

def top_10_movies_bar_chart(df):
    top_10_movies = df.nlargest(10, "popularity")

    plt.figure(figsize=(12, 8))
    sns.barplot(data=top_10_movies, x="popularity", y="title", palette="viridis")
    plt.title("Top 10 Most Popular Movies")
    plt.xlabel("Popularity")
    plt.ylabel("Movie Title")
    plt.show()


if __name__ == "__main__":
    df = fetch_movies_data()

    # Choose the type of visualization
    #scatter_plot(df)
    top_10_movies_bar_chart(df)
