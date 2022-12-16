class MyQueue:
    """
    stack(list)를 이용해서 queue 구현하기.
    pop과 peek에 대해서 처리를 잘 해주면 된다.
    그리고 if 조건문에서 list의 empty는
    "무언가 들어있으면 True, 아무것도 없으면 False"이다.
    """
    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        return self.queue.pop(0)

    def peek(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        if self.queue:
            return False
        else:
            return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
