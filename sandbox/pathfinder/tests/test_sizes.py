from sandbox.pathfinder.sizes import Size


def test_ordering() -> None:
    """ Tests comparison works properly """
    assert Size.FINE < Size.DIMINUTIVE < Size.TINY < \
           Size.SMALL < Size.MEDIUM < Size.LARGE < \
           Size.HUGE < Size.GARGANTUAN < Size.COLOSSAL
