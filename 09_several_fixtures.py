import pytest


def test_hello_world(server, install_browser):
    assert server.exec() == 'Hello, World!'


@pytest.fixture(
    params=['ubuntu-20.04.4-server'], ids=['ubuntu']
)
def os(request):
    return request.param


@pytest.fixture()
def server(os):
    prepared_server = prepare(os)
    return prepared_server


@pytest.fixture()
def install_browser(os):
    installed_browser = install(os)
    return installed_browser


def prepare(param):
    return Server(param)


def install(param):
    return Browser(param).install()


class Server:
    def __init__(self, os):
        self.os = os

    def exec(self):
        if self.os:
            return 'Hello, World!'


class Browser:
    def __init__(self, os):
        self.os = os

    def install(self):
        return self
