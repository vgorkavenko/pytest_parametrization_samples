import pytest


@pytest.mark.parametrize(
  'os', [
    'ubuntu-20.04.4-server',
    'centos-8.4.2105',
    'windowsserver-2022-21H2'
  ]
)
@pytest.mark.parametrize('arch', ['x86', 'ARM', 'PowerPC'])
def test_hello_world(os, arch):
    server = prepare_infrastructure(os, arch)
    assert server.exec() == 'Hello, World!'


def prepare_infrastructure(os, arch):
    return Server(os, arch)


class Server:
    def __init__(self, os, arch):
        self.os = os
        self.arch = arch

    def exec(self):
        if self.os and self.arch:
            return 'Hello, World!'

