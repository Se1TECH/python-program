import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class MovieRecommendationSystem:
    def __init__(self, ratings):
        self.ratings = np.array(ratings)
    
    def get_movie_similarity(self):
        similarity_matrix = cosine_similarity(self.ratings.T)
        return similarity_matrix
    
    def recommend_movies(self, user_index, num_recommendations=5):
        similarity_matrix = self.get_movie_similarity()
        user_ratings = self.ratings[user_index]
        weighted_ratings = similarity_matrix.dot(user_ratings)
        sorted_indices = np.argsort(weighted_ratings)[::-1]
        
        recommendations = []
        for i in range(num_recommendations):
            movie_index = sorted_indices[i]
            if user_ratings[movie_index] == 0:
                recommendations.append(movie_index)
        
        return recommendations


# Example usage
ratings = [
    [5, 4, 3, 0, 0, 0],
    [0, 0, 0, 4, 5, 0],
    [4, 0, 0, 2, 0, 0],
    [0, 0, 0, 0, 4, 5]
]

rec_sys = MovieRecommendationSystem(ratings)
recommendations = rec_sys.recommend_movies(0, num_recommendations=3)

print("Recommended movies:")
for movie_index in recommendations:
    print("Movie", movie_index + 1)
