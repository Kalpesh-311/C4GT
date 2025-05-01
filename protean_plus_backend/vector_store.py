import weaviate
import uuid

client = weaviate.Client("http://localhost:8080")

def create_schema():
    if not client.schema.contains({"classes": [{"class": "KPIQuery"}]}):
        client.schema.create_class({
            "class": "KPIQuery",
            "properties": [
                {"name": "text", "dataType": ["text"]},
                {"name": "lang", "dataType": ["text"]}
            ],
            "vectorIndexConfig": {"distance": "cosine"}
        })

def insert_query(text, lang, vector):
    client.data_object.create(
        data_object={"text": text, "lang": lang},
        class_name="KPIQuery",
        vector=vector,
        uuid=str(uuid.uuid4())
    )

def search_similar(vector, k=3):
    return client.query.get("KPIQuery", ["text", "lang"]).with_near_vector({
        "vector": vector
    }).with_limit(k).do()
