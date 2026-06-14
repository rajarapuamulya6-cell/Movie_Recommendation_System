import pandas as pd
import random

# Load dataset
data = pd.read_csv("movies.csv")

print("=" * 50)
print("🎬 Mood-Based Movie Recommendation System")
print("=" * 50)

while True:

    print("\nAvailable moods:")
    print("😊 Happy")
    print("💪 Inspirational")
    print("😢 Sad")
    print("🔥 Excited")
    print("😌 Relaxed")

    mood = input("\nEnter your mood (or type exit): ")

    if mood.lower() == "exit":
        print("\nThank you for using the Movie Recommendation System!")
        break

    recommendations = data[
        data["mood"].str.lower() == mood.lower()
    ]

    if len(recommendations) > 0:

        print("\n🎥 Recommended Movies For You:\n")

        movies = recommendations["movie"].tolist()

        random.shuffle(movies)

        for movie in movies:
            print("⭐", movie)

    else:
        print("\n❌ Mood not found. Try again.")