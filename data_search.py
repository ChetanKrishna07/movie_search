from elasticsearch import Elasticsearch
import fastapi
import uvicorn

app = fastapi.FastAPI()

es = Elasticsearch("http://localhost:9200")


@app.get("/title/{title}")
def get_title(title: str):
    try:
        query = {
            "bool": {
                "should": [
                    {
                        "match": {
                            "title": {
                                "query": title,
                                "operator": "and"
                            }
                        }
                    },
                    {
                        "fuzzy": {
                            "title": {
                                "value": title,
                                "fuzziness": "AUTO"
                            }
                        }
                    }
                ]
            }
        }

        res = es.search(index="movies", query=query)
        hits = res.body["hits"]["hits"]
        data = [doc["_source"] for doc in hits]
        return {"status": "success", "data": data}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    