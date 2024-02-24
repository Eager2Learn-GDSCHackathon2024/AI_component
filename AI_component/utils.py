import numpy as np

def cosine_similarity(matrix1, matrix2):
    # Flatten the matrices
    flat_matrix1 = matrix1.flatten()
    flat_matrix2 = matrix2.flatten()

    # Compute dot product
    dot_product = np.dot(flat_matrix1, flat_matrix2)

    # Compute magnitudes
    magnitude1 = np.linalg.norm(flat_matrix1)
    magnitude2 = np.linalg.norm(flat_matrix2)

    # Compute cosine similarity
    return dot_product / (magnitude1 * magnitude2)