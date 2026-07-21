from sentence_transformers import SentenceTransformer


model = SentenceTransformer(
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)

def get_embedding(line):
    return model.encode(line, normalize_embeddings=True)

get_embedding("russia")
