class MyStack:
    def __init__(self, initial = []):
        self.stack = initial
        # в качестве стека используется лист "наоборот": верхнее значение стека - последний элемент листа
        # заменить на dequeu?

    def IsEmpty(self):
        return not self.stack

    def push(self, el):
        self.stack.append(el)

    def pop(self):
        if self.IsEmpty():
            return None # or raise error?
        return self.stack.pop()

    def peek(self):
        if self.IsEmpty():
            return None # or raise error?
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def __str__(self):
        return str(self.stack)