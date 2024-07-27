import numpy as np

def calculate_anp(scores):
    # Membuat matriks perbandingan berpasangan
    sambal_names = list(scores.keys())
    n = len(sambal_names)
    pairwise_matrix = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            if i == j:
                pairwise_matrix[i, j] = 1
            else:
                pairwise_matrix[i, j] = scores[sambal_names[i]] / scores[sambal_names[j]]

    # Menghitung eigenvector untuk mendapatkan bobot
    eigenvalues, eigenvectors = np.linalg.eig(pairwise_matrix)
    max_eigenvalue_index = np.argmax(eigenvalues)
    weights = eigenvectors[:, max_eigenvalue_index]
    weights = weights / np.sum(weights)  # Normalisasi bobot

    # Mengembalikan hasil dalam bentuk dictionary
    result = {sambal_names[i]: weights[i] for i in range(n)}
    return result
