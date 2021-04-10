class Stack():
    memory = []

    def __init__(self):
        pass

    def push(self, el):
        self.memory.append(el)

    def pop(self):
        return self.memory.pop(-1)
        # no negative numbers so not checking list size

    def peek(self):
        return self.memory[-1]

    def is_empty(self):
        return len(self.memory) == 0
