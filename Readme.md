# Steps to run
1. Create a virtual environment and activate it (optional)

```
python -m venv venv
source ./venv/bin/activate
```

2. Install neccesary libraries
```

pip install -r requirements.txt
```

3. Run the single cluster docker container
```
docker run --rm -p 9200:9200 -p 9300:9300 -e "xpack.security.enabled=false" -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:8.7.0
```

4. Add data into elastic search cluster
```
python add_data.py
```

5. Run the API
```
uvicorn data_search:app
```

6. Run the front-end
```
streamlit run frontend.py
```
