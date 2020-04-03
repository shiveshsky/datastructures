from abc import ABC, abstractmethod


class A(object):
    def __init__(self, *args, **kwargs):
        print('A')
        pass

    @abstractmethod
    def demo(self, context):
        pass


class B(A, ABC):
    def __init__(self, *args, **kwargs):
        print("Parent")
        if kwargs.get('tenant_id'):
            print('tenant: ', kwargs.get('tenant_id'))
        else:
            raise Exception("tenant not passed")

    @abstractmethod
    def demo(self, context):
        pass


class C(B):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('C')

    def demo(self, context):
        print('implemented')


print(C(tenant_id=1))

