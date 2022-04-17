import pytest


@pytest.mark.parametrize(
    ('os', 'arch'), [
        ('ubuntu-20.04.4-server', 'x86'),
        ('ubuntu-20.04.4-server', 'ARM'),
        ('ubuntu-20.04.4-server', 'PowerPC'),
        ('centos-8.4.2105', 'x86'),
        ('centos-8.4.2105', 'ARM'),
        ('centos-8.4.2105', 'PowerPC'),
        ('windowsserver-2022-21H2', 'x86'),
        ('windowsserver-2022-21H2', 'ARM')
    ]
)
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
