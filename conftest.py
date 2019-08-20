from pytest_socket import disable_socket


def pytest_runtest_setup():
    """
    This is run when setting up the tests.
    """
    # We don't want to allow access to sockets, to make sure we're not making calls to some website
    disable_socket()