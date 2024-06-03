import threading


class Singleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if not cls._instance:  # This is the only difference
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
        return cls._instance


singleton = Singleton()
new_singleton = Singleton()

print(singleton is new_singleton)

print(singleton, new_singleton)

while True:
    pass
