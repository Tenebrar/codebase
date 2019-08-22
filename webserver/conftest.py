from django.core.cache import cache
from pytest import fixture


@fixture(autouse=True)
def clear_cache_after_test_run():
    """
    In order to prevent state leaking across tests, we clear the cache after each one
    """
    yield
    cache.clear()
