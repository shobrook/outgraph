import numpy as np
from collections import namedtuple


Graph = namedtuple("Graph", ["node_attrs", "adjacency_matrix"])


def _mean_feature_vector(G):
    return np.mean(G.node_attrs, axis=0)


def _adjacency_vector(G):
    A = G.adjacency_matrix
    n = A.shape[0]

    return A[np.tril_indices(n)]


def vectorize_graphs(graphs, method=1):
    vectors = []
    for G in graphs:
        if method == 1:
            vector = _mean_feature_vector(G)
        elif method == 2:
            vector = _adjacency_vector(G)
        elif method == 3:
            v0 = _mean_feature_vector(G)
            v1 = _adjacency_vector(G)
            vector = np.concat(v0, v1)

        vectors.append(vector)

    return np.vstack(vectors)
