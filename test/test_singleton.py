import pytest

from creational_patterns.singleton.singleton import ResourceManagerExample
from creational_patterns.singleton.threadsafe_singleton import TsResourceManagerExample


def test_singleton():
    x = ResourceManagerExample()
    y = ResourceManagerExample()
    assert id(x) == id(y)


def test_resource_example_case():
    system = ResourceManagerExample(resource=100)
    assert system.resource == 100

    x = ResourceManagerExample()
    assert id(x) == id(system)
    x.use_resource(30)
    assert x.resource == 70
    y = ResourceManagerExample()
    assert id(x) == id(y)
    assert y.resource == 70
    x.return_resource(20)
    assert x.resource == y.resource == 90

    with pytest.raises(Exception):
        x.use_resource(100)


def test_threadsafe_singleton():
    x = TsResourceManagerExample()
    y = TsResourceManagerExample()
    assert id(x) == id(y)


def test_tsresource_example_case():
    system = TsResourceManagerExample(resource=100)
    assert system.resource == 100

    x = TsResourceManagerExample()
    assert id(x) == id(system)
    x.use_resource(30)
    assert x.resource == 70
    y = TsResourceManagerExample()
    assert id(x) == id(y)
    assert y.resource == 70
    x.return_resource(20)
    assert x.resource == y.resource == 90

    with pytest.raises(Exception):
        x.use_resource(100)
