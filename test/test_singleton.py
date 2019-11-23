from creational_patterns.singleton.singleton import ResourceManagerExample


def test_singleton():
    x = ResourceManagerExample()
    x.use_resource()
    print(x._resource)
    y = ResourceManagerExample()
    print(y._resource)
    y.use_resource()
    x.use_resource()
    print(y._resource)
    print(x._resource)
    
    assert id(x) == id(y)
    