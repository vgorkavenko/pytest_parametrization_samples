import pytest


@pytest.fixture(
  params=[('ubuntu-20.04.4-server', 'x86')], ids=['ubuntu-x86']
)
def server(request):
    prepared_server = prepare(request.param)
    return prepared_server


@pytest.mark.parametrize(
  'server',
  [('centos-8.4.2105', 'ARM')],
  ids=['centos-ARM'],
  indirect=True
)
def test_hello_world(server):
    assert server.exec() == 'Hello, World!'


def prepare(param):
    return Server(*param)


class Server:
    def __init__(self, os, arch):
        self.os = os
        self.arch = arch

    def exec(self):
        if self.os and self.arch:
            return 'Hello, World!'
