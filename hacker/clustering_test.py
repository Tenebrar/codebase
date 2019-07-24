import pytest
from pysistence import make_dict

from hacker.clustering import cluster, _cluster_points, _reevaluate_centers, _has_converged


def test_cluster():
    """ Check the cluster function returns the correct values """
    inputs = {
        'a': (4, 0, 0, 0),
        'b': (0, 4, 0, 0),
        'c': (0, 0, 4, 0),
        'd': (0, 0, 0, 4),
    }
    # By choosing 1 cluster, we guarantee the outcome must always be the same no matter the randomness
    amount_of_clusters = 1

    inputs = make_dict(inputs)  # Attempting to modify the input would cause an Exception

    result = cluster(inputs, amount_of_clusters)

    assert len(result) == 1
    assert sorted(result.get((1, 1, 1, 1))) == ['a', 'b', 'c', 'd']


def test_cluster_points():
    """ Tests that _cluster_points returns the correct value """
    inputs = {
        'a': (4, 0, 0, 0),
        'b': (0, 4, 0, 0),
        'c': (0, 0, 4, 0),
        'd': (0, 0, 0, 4),
    }
    # Centers are chosen so the result is unique
    centers = [(4, 4, 0, 0), (0, 0, 4, 4)]

    result, score = _cluster_points(inputs, centers)

    assert len(result) == 2
    assert sorted(result.get((4, 4, 0, 0))) == ['a', 'b']
    assert sorted(result.get((0, 0, 4, 4))) == ['c', 'd']

    assert score == 4 * 4  # The distance is 4 for all 4 vectors


def test_reevaluate_centers():
    """ Check that _reevaluate_centers returns the correct result """
    inputs = {
        'a': (4, 0, 0, 0),
        'b': (0, 4, 0, 0),
        'c': (0, 0, 4, 0),
        'd': (0, 0, 0, 4),
    }
    clusters = {
        (4, 4, 0, 0): ['a', 'b'],
        (0, 0, 4, 4): ['c', 'd'],
    }

    # The result is always deterministic from the input
    result = _reevaluate_centers(clusters, inputs)

    assert sorted(result) == [(0, 0, 2, 2), (2, 2, 0, 0)]


@pytest.mark.parametrize("test_input1,test_input2,expected", [
    ([(1,)], [(1,)], True),
    ([(1,), (2,)], [(1,), (2,)], True),
    ([(1,), (2,)], [(2,), (1,)], True),
    ([(1.0,), (2.,)], [(2,), (1,)], True),
    ([(1,), (2,)], [(1,)], False),
    ([(1,)], [(1,), (2,)], False),
])
def test_has_converged(test_input1, test_input2, expected):
    """
    Tests that _has_converged behaves as expected, especially when faced with values that should be considered the same
    """
    assert _has_converged(test_input1, test_input2) == expected
