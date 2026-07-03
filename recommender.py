import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import os

# Absolute path banayega
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

hotels = pd.read_csv(
    os.path.join(BASE_DIR, "dataset", "cleaned_hotels.csv")
)

user_hotel = pd.crosstab(
    hotels["userCode"],
    hotels["name"]
)

similarity = cosine_similarity(user_hotel)


def recommend_hotels(user_id, top_n=5):

    if user_id not in user_hotel.index:
        return []

    user_idx = list(user_hotel.index).index(user_id)

    scores = similarity[user_idx]

    similar_users = np.argsort(scores)[::-1][1:6]

    hotels_seen = set(
        user_hotel.loc[user_id][
            user_hotel.loc[user_id] > 0
        ].index
    )

    recommendations = []

    for idx in similar_users:

        sim_user = user_hotel.index[idx]

        sim_hotels = set(
            user_hotel.loc[sim_user][
                user_hotel.loc[sim_user] > 0
            ].index
        )

        recommendations.extend(
            list(sim_hotels - hotels_seen)
        )

    return list(set(recommendations))[:top_n]


# Recommendation Engine

# this module contains the business logic for hotel recommendations.

## Functionality

- Loads hotel booking dataset
- Creates User-Hotel Interaction Matrix
- Calculates Cosine Similarity
- Identifies similar users
- Recommends hotels not previously visited by the target user

## Algorithm

Collaborative Filtering using Cosine Similarity

## Output

Returns Top-N hotel recommendations for a given user.