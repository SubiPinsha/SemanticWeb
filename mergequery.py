import rdflib

# Load the merged RDF graph
g = rdflib.Graph()
g.parse("merged.owl", format="xml")

# SPARQL query to retrieve all models and their algorithms
query = """
PREFIX ds: <http://example.org/ds#>
PREFIX ml: <http://example.org/ml#>

SELECT ?model ?algorithm WHERE {
    ?model a ds:Model .
    ?model ds:usesAlgorithm ?algorithm .
}
"""

# Execute the query
results = g.query(query)

# Print the results
for row in results:
    print(f"Model: {row['model']}, Algorithm: {row['algorithm']}")
