from sentence_transformers import SentenceTransformer, util
import torch

# Load pre-trained sentence transformer model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Sample documents
documents = [
    "Artificial Intelligence is transforming industries.",
    "Machine Learning enables computers to learn from data.",
    "Football is a popular sport worldwide.",
    "Deep learning is a subset of machine learning."
]

# Encode documents
doc_embeddings = model.encode(documents, convert_to_tensor=True)

print("🔎 Semantic Search System Ready\n")

while True:
    query = input("Enter your search query (type 'quit' to exit): ")

    if query.lower() == "quit":
        break

    # Encode query
    query_embedding = model.encode(query, convert_to_tensor=True)

    # Compute cosine similarity
    scores = util.cos_sim(query_embedding, doc_embeddings)

    # Get best match
    best_match = torch.argmax(scores)

    print("\nMost Relevant Document:")
    print(documents[best_match])
    print("Similarity Score:", round(float(scores[0][best_match]), 3))
    print("-" * 50)
