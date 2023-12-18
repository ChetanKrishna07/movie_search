from elasticsearch import Elasticsearch
import pandas as pd

es = Elasticsearch("http://localhost:9200")
# print(es.info().body)
df = pd.read_csv("wiki_movie_plots_deduped.csv").dropna().sample(5000, random_state=42).reset_index()
# print(df.head())

# setting the document structure for the index
mappings = {
        "properties": {
            "title": {"type": "text", "analyzer": "english"},
            "ethnicity": {"type": "text", "analyzer": "standard"},
            "director": {"type": "text", "analyzer": "standard"},
            "cast": {"type": "text", "analyzer": "standard"},
            "genre": {"type": "text", "analyzer": "standard"},
            "plot": {"type": "text", "analyzer": "english"},
            "year": {"type": "integer"},
            "wiki_page": {"type": "keyword"}
    }
}

# creating the index
es.indices.create(index="movies", mappings=mappings)

# adding data to the index
for i, row in df.iterrows():
    doc = {
        "title": row["Title"],
        "ethnicity": row["Origin/Ethnicity"],
        "director": row["Director"],
        "cast": row["Cast"],
        "genre": row["Genre"],
        "plot": row["Plot"],
        "year": row["Release Year"],
        "wiki_page": row["Wiki Page"]
    }
    
    # Add index to ES ad id i
    es.index(index="movies", id=i, body=doc)
    
# checking if the data is added
es.indices.refresh(index="movies")
print(es.cat.count(index="movies", format="json"))
