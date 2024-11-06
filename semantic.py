import numpy
import h5py
import spacy



# Load the English model
nlp = spacy.load("en_core_web_md")

def compute_similarity(text1, text2):
    """
    Compute the semantic similarity between two texts.
    
    Args:
        text1 (str): The first text.
        text2 (str): The second text.
        
    Returns:
        float: Similarity score between 0 and 1.
    """
    # Process the texts with spaCy
    doc1 = nlp(text1)
    doc2 = nlp(text2)
    
    # Calculate and return the similarity
    return doc1.similarity(doc2)

if __name__ == "__main__":
    # Sample input texts
    text1 = "I enjoy learning about artificial intelligence."
    text2 = "Studying AI is fascinating and rewarding."
    
    similarity_score = compute_similarity(text1, text2)
    print(f"Semantic Similarity between the two texts: {similarity_score:.4f}")
