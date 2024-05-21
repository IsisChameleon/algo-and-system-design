import numpy as np
from sklearn.cluster import KMeans

class Candidate:
    def __init__(self, name, availability, interests):
        self.name = name
        self.availability = availability  # list of booleans
        self.interests = interests        # list of strings

def encode_features(candidates):
    # Create index maps for interests and timeslots
        # Collect all unique interests
    all_interests = set(interest for candidate in candidates for interest in candidate.interests)
    number_of_time_slots =  len(candidates[0].availability) # assuming they all share the same availability list length

    interest_index = {interest: idx for idx, interest in enumerate(all_interests)}
    total_features = len(all_interests) + number_of_time_slots

    # Initialize the feature matrix
    feature_matrix = np.zeros((len(candidates), total_features))

    for i, candidate in enumerate(candidates):
        # Encode interests
        for interest in candidate.interests:
            feature_matrix[i, interest_index[interest]] = 1

        # Encode availability
        for j in range(number_of_time_slots):
            feature_matrix[i, len(all_interests) + j] = 1 if candidate.availability[j] else 0

    return feature_matrix

def cluster_candidates(candidates, num_clusters):

    # Encode interests and availability into feature vectors
    feature_matrix = encode_features(candidates)
    
    # Perform K-means clustering on the composite feature matrix
    kmeans = KMeans(n_clusters=num_clusters, random_state=0).fit(feature_matrix)
    
    # Group candidates based on clusters
    clusters = [[] for _ in range(num_clusters)]
    for candidate, label in zip(candidates, kmeans.labels_):
        clusters[label].append(candidate)
    
    return clusters, feature_matrix, kmeans.labels_

from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

def visualize_with_tsne(X, labels):
    n_samples = len(X)
    perplexity = min(30, n_samples - 1) 
    tsne = TSNE(n_components=2, verbose=1, perplexity=perplexity, n_iter=300)
    tsne_results = tsne.fit_transform(X)
    
    plt.figure(figsize=(16,10))
    scatter = plt.scatter(tsne_results[:,0], tsne_results[:,1], c=labels, cmap='viridis')
    plt.colorbar(scatter)
    plt.title('t-SNE visualization of high-dimensional data')
    plt.xlabel('TSNE-1')
    plt.ylabel('TSNE-2')       
    plt.show()

# Assume 'features' is your high-dimensional data and 'labels' is the cluster or class labels
# visualize_with_tsne(features, labels)




if __name__ == "__main__":      
    

    # Example Candidates
    candidates = [
        Candidate("Alice", [True, False, True], ["python", "agile"]),
        Candidate("Bob", [True, True, False], ["python", "devops"]),
        Candidate("Charlie", [False, True, True], ["java", "agile", "blurb"]),
    ]

    # Perform clustering
    clusters, features, labels = cluster_candidates(candidates, 2)
    for idx, cluster in enumerate(clusters):
        print(f"Cluster {idx + 1}: {[candidate.name for candidate in cluster]}")

    visualize_with_tsne(features, labels)
