class StockSpanner:
    """
    내가 생각했던 로직이, monotinic stack의 로직임을 알았지만, 그것을 코드로 적용하지는 못했다.

    price를 입력받았을때, stack[-1]보다 크거나 같다면, 반대인 경우가 나올때까지 pop시키고, pop시킨 숫자+1(나)를 return시키는 로직을 생각했다.
    다만, 이렇게 되면 예외처리해줘야할 부분이 많았다.

    내가 생각한것과 가장 크게 다른 두가지는 지운 갯수를 int형 변수가 아닌 list로 가지고 있어서 더해주는 점
    두번째는 stack과 list에 더해주는 시점이 while문 바깥이라는 점이다.

    첫번째로 인해, 해당 변수를 다루는데 있어 예외처리(지우면서, 지운갯수가 계속 갱신되는 경우, 지웠는데 지운갯수가 초기화되는 경우)를 막아줄 수 있다.
    두번째로 인해, 동일한 추가 시점을 제공한다.
    이로인해 정답이 완성됨.

    풀이법은 알았는데 풀지 못해 많이 아쉽다.
    """

    def __init__(self):
        self.stack=[]
        self.lst=[]        

    def next(self, price: int) -> int:
        if len(self.stack)==0:
            self.stack.append(price)
            self.lst.append(1)
            return 1
        
        cnt = 1
        while self.stack:
            if self.stack[-1] <= price:
                self.stack.pop()
                cnt+=self.lst.pop()
            else:
                break
        self.stack.append(price)
        self.lst.append(cnt)
        return cnt
