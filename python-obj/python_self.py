
class ClassA:
    def __init__(self):
        self.name = "abc"
        self.age = 123
    def start(self):
        get_self(handler = self)


def get_self(handler):
    print handler.name
    print handler.age


if __name__ == "__main__":
    a = ClassA()
    a.start()
