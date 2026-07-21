from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    PointStruct,
    VectorParams,
)
from core.embedder import get_embedding


client = QdrantClient(path="./knowledge")

if not client.collection_exists("rag_facts"):    
    client.create_collection(
        collection_name="rag_facts",
        vectors_config=VectorParams(
            size=384,
            distance=Distance.COSINE,
        )
    )

def add(line):
    point = PointStruct(
        id=1,
        vector=get_embedding(line).tolist(),
        payload={
            "text": line
        }
    )

    client.upsert(
        collection_name="rag_facts",
        points=[point]
    )

def find(line, how_many=1):
    response = client.query_points(
        collection_name="rag_facts",
        query=get_embedding(line).tolist(),
        limit=how_many,
        with_payload=True
    )
    return response.points

def all(how_many=100):
    points, next_offset = client.scroll(
        collection_name="rag_facts",
        with_payload=True,
        limit=how_many,
        with_vectors=False
    )
    return points
