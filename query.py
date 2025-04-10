from rdflib import Graph

# Load the RDF graph
g = Graph()
g.parse("ds.owl")  # Replace with the correct path to your RDF file

# 1. Query to Get Models with Their Algorithms and Execution Times
query_1 = """
PREFIX ds: <http://example.org/ds#>

SELECT ?model ?algorithm ?executionTime
WHERE {
  ?model a ds:Model .
  ?model ds:usesAlgorithm ?algorithm .
  ?model ds:executionTime ?executionTime .
}
"""
print("1. Models with Algorithms and Execution Times:")
results_1 = g.query(query_1)
for row in results_1:
    print(f"Model: {row.model}, Algorithm: {row.algorithm}, Execution Time: {row.executionTime}")
print()

# 2. Query to Get Metrics with Accuracy Above a Threshold
query_2 = """
PREFIX ds: <http://example.org/ds#>

SELECT ?metric ?accuracy
WHERE {
  ?metric a ds:Metric .
  ?metric ds:accuracy ?accuracy .
  FILTER (?accuracy > 0.9)
}
"""
print("2. Metrics with Accuracy Above Threshold:")
results_2 = g.query(query_2)
for row in results_2:
    print(f"Metric: {row.metric}, Accuracy: {row.accuracy}")
print()

# 3. Query to Get Visualizations Associated with a Specific Dataset
query_3 = """
PREFIX ds: <http://example.org/ds#>

SELECT ?visualization ?label
WHERE {
  ?visualization a ds:Visualization .
  ?visualization ds:visualizes ?dataset .
  ?dataset rdfs:label "Iris Dataset" .
  ?visualization rdfs:label ?label .
}
"""
print("3. Visualizations Associated with 'Iris Dataset':")
results_3 = g.query(query_3)
for row in results_3:
    print(f"Visualization: {row.visualization}, Label: {row.label}")
print()





# 6. Query to Get All Algorithms and the Models Using Them (Distinct Models)
query_6 = """
PREFIX ds: <http://example.org/ds#>

SELECT DISTINCT ?algorithm ?model
WHERE {
  ?model a ds:Model .
  ?model ds:usesAlgorithm ?algorithm .
}
"""
print("6. Distinct Models Using Algorithms:")
results_6 = g.query(query_6)
for row in results_6:
    print(f"Algorithm: {row.algorithm}, Model: {row.model}")
print()

# 7. Query to Get Models, Their Execution Times, and Associated Algorithms (With Sorting)
query_7 = """
PREFIX ds: <http://example.org/ds#>

SELECT ?model ?algorithm ?executionTime
WHERE {
  ?model a ds:Model .
  ?model ds:usesAlgorithm ?algorithm .
  ?model ds:executionTime ?executionTime .
}
ORDER BY ?executionTime
"""
print("7. Models, Their Execution Times, and Associated Algorithms (Sorted by Execution Time):")
results_7 = g.query(query_7)
for row in results_7:
    print(f"Model: {row.model}, Algorithm: {row.algorithm}, Execution Time: {row.executionTime}")
print()
