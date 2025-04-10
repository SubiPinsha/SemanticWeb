import rdflib

g = rdflib.Graph()

g.parse("ds.owl",format =  "xml")

g.parse("ml.owl",format =  "xml")

g.serialize("merged.owl",format ="xml")