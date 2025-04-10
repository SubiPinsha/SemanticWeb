import rdflib
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_similarity

g1 = rdflib.Graph()
g2 = rdflib.Graph()

g1.parse("ds.owl", format="xml")
g2.parse("ml.owl", format="xml")

def get_classes(graph):
    classes = set()
    for s, p, o in graph:
        if isinstance(o, rdflib.URIRef) and o.startswith("http://www.w3.org/2002/07/owl#Class"):
            classes.add(s)
    return list(classes)

classes1 = get_classes(g1)
classes2 = get_classes(g2)


all_classes = classes1 + classes2


class_texts = [str(cls) for cls in all_classes]


vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(class_texts)

# Apply K-means clustering
num_clusters = 2  
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
kmeans.fit(X)

# Print the cluster assignments for each class
for idx, label in enumerate(kmeans.labels_):
    print(f"Class: {all_classes[idx]} is in cluster {label}")

# Group the classes based on the clusters
clustered_classes = {i: [] for i in range(num_clusters)}
for idx, label in enumerate(kmeans.labels_):
    clustered_classes[label].append(all_classes[idx])

# Now you have clustered classes from both ontologies
# Example of how to print them (or you could align them manually/semantically)
for cluster, classes in clustered_classes.items():
    print(f"\nCluster {cluster}:")
    for cls in classes:
        print(f" - {cls}")