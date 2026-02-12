from injector import Injector,inject

class A:
    pass

@inject
class B:
    def __init__(self, a:A):
        self.a = a

injector = Injector()
b_instance = injector.get(B)
print(b_instance.a)