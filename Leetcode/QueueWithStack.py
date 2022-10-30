class MyQueue:

    def __init__(self):
        self.back = []
        self.front = []
        

    def push(self, x: int) -> None:
        self.back.append(x)
        
    def pop(self) -> int:
        if self.front:
            return self.front.pop()
        else:
            while self.back:
                self.front.append(self.back.pop())
            return self.front.pop()

    def peek(self) -> int:
        if self.front:
            return self.front[-1]
        else:
            while self.back:
                self.front.append(self.back.pop())
            return self.front[-1]

    def empty(self) -> bool:
        if self.front or self.back:
            return False
        return True