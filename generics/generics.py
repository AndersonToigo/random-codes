from typing import TypeVar

T = TypeVar('T')

class Stack:
    def __init__(self, type: T):
        self.type = type
        self.items = []

    def push(self, item):
        if not isinstance(item, self.type):
            raise TypeError(f'Expected type {self.type}, got {type(item)}')
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def define_type(self, type: T):
        self.type = type

class TypedStack(Stack):
    def __init__(self, type: T):
        super().__init__(type)

    def push(self, item: T):
        super().push(item)

    def pop(self) -> T:
        return super().pop()

my_stack = TypedStack(int)
my_stack.push(1)
my_stack.push('hello')
