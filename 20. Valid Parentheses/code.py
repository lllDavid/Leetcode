class Solution:
    def isValid(self, s: str) -> bool:
        class Stack:
            def __init__(self):
                self.items = []

            def push(self, item):
                self.items.append(item)

            def pop(self):
                if not self.is_empty():
                    return self.items.pop()
                return None

            def peek(self):
                if not self.is_empty():
                    return self.items[-1]
                return None

            def is_empty(self):
                return len(self.items) == 0

        stack = Stack()

        for char in s:
            if char in '({[':
                stack.push(char)
            elif char in ')}]':
                top = stack.pop()
                if not self.is_match(top, char):
                    return False

        return stack.is_empty()

    def is_match(self, open_char, close_char):
        return (open_char == '(' and close_char == ')') or \
               (open_char == '{' and close_char == '}') or \
               (open_char == '[' and close_char == ']')