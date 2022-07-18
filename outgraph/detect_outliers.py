import numpy as np
from scipy.stats import chi2
from outgraph.vectorize_graphs import vectorize_graphs


def detect_outliers(graphs, method=1, p_value=0.05):
    vectors = vectorize_graphs(graphs, method)
    num_components = vectors.shape[1]

    covariance  = np.cov(vectors, rowvar=False)
    covariance_pm1 = np.linalg.matrix_power(covariance, -1)
    centerpoint = np.mean(vectors, axis=0)

    def _mahalanobis_distance(v):
        return (v - centerpoint).T.dot(covariance_pm1).dot(v - centerpoint)

    distances = np.apply_along_axis(_mahalanobis_distance, 1, vectors)
    cutoff = chi2.ppf(1 - p_value, num_components)

    outlier_indices, = np.where(distances > cutoff)
    outliers = [graphs[int(i)] for i in outlier_indices]

    return outliers
