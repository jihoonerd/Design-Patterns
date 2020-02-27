from threading import Thread, Lock


class SingletonMeta(type):

    _instances = {}
    _lock = Lock()

    def __call__(cls, *args, **kwargs):

        with cls._lock:
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__()
        return cls._instances[cls]


class TsResourceManagerExample(metaclass=SingletonMeta):
    def __init__(self, resource=100):
        self._resource = resource

    @property
    def resource(self):
        return self._resource

    def use_resource(self, demand=10):
        if self._resource - demand < 0:
            raise Exception("Not enough resource. Cannot proceed")
        self._resource -= demand

    def return_resource(self, res=10):
        self._resource += res
