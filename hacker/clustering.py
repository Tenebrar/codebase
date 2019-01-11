import numpy as np
import random
from typing import Dict, List, Any, Tuple


def cluster(inputs: Dict[Any, Tuple], amount_of_clusters: int, iterations: int=1) -> Dict[Tuple, List[Any]]:
    """
    Run a clustering algorithm on the input vectors.

    This is Lloyd's algorithm, may be improved by using k-means++ for better initialization.
    Repeated samplings (and returning the best) were already added, which is a standard improvement.

    :param inputs: a mapping of objects to be clustered (any object) to their vector representation (a tuple)
    :param amount_of_clusters: The amount of desired output clusters
    :param iterations: The number of times to run the basic algorithm, to improve the results
    :return: a mapping of center vectors (tuples) to a list of objects (same type as the input objects) that
    are in the cluster defined by that vector
    """
    best_clusters = None
    best_score = 2**16
    for _ in range(iterations):
        # Select random samples from the input to be the initial centers
        centers = random.sample(list(inputs.values()), amount_of_clusters)

        while True:
            # Assign all points in the inputs to clusters
            clusters, _ = _cluster_points(inputs, centers)
            # Reevaluate centers
            old_centers = centers
            centers = _reevaluate_centers(clusters, inputs)

            if _has_converged(centers, old_centers):
                break

        clusters, score = _cluster_points(inputs, centers)
        if score < best_score:
            best_score = score
            best_clusters = clusters

    return best_clusters


def _cluster_points(inputs: Dict[Any, Tuple], centers: List[Tuple]) -> Dict[Tuple, List[Any]]:
    """
    Determine for each input which center is closest to it

    :param inputs: a mapping of objects to be clustered (any object) to their vector representation (a tuple)
    :param centers: a list of center vectors (tuples)
    :return: a mapping of center vectors (tuples) to a list of objects (same type as the input objects) that
    are in the cluster defined by that vector
    """
    clusters = {}  # type: Dict[Tuple, Any]
    score = 0
    for obj, vector in inputs.items():
        distances = [(center, np.linalg.norm(np.array(vector) - np.array(center))) for center in centers]
        best_center, best_score = min(distances, key=lambda t: t[1])
        score += best_score
        try:
            clusters[best_center].append(obj)
        except KeyError:
            clusters[best_center] = [obj]
    return clusters, score


def _reevaluate_centers(clusters: Dict[Tuple, List[Any]], inputs: Dict[Any, Tuple]) -> List[Tuple]:
    """
    Finds the new centers based on the current clustering (take the average of each cluster)

    :param clusters: a mapping of center vectors (tuples) to a list of objects (same type as the input objects)
     that are in the cluster defined by that vector
    :param inputs: a mapping of objects to be clustered (any object) to their vector representation (a tuple)
    :return: a list of center vectors (tuples)
    """
    new_centers = []
    for cluster in clusters.values():
        new_centers.append(tuple(np.mean([np.array(inputs[v]) for v in cluster], axis=0)))
    return new_centers


def _has_converged(centers: List[Tuple], old_centers: List[Tuple]) -> bool:
    """
    Verify that two sets of center vectors are the same

    :param centers: a list of center vectors (tuples)
    :param old_centers: a list of center vectors (tuples)
    :return: Whether the two sets of center vectors are the same
    """
    return set(centers) == set(old_centers)
