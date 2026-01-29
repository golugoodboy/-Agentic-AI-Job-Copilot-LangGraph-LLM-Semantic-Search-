from sentence_transformers import SentenceTransformer
import numpy as np

_model = SentenceTransformer("all-MiniLM-L6-v2")

def get_embedding(text: str) -> np.ndarray:
    return _model.encode(text, normalize_embeddings=True)

def cosine_similarity(vec1: np.ndarray, vec2: np.ndarray) -> float:
    # Since vectors are normalized, dot product = cosine similarity
    return float(np.dot(vec1, vec2))

