class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:

        """
        두 직사각형이 주어졌을때, 이 둘 사이의 관계를 통해서 알 수있다.
        두 직사각형이 안만나는 경우에 대해 예외처리를 해준다.
        -> 한 직사각형의 오른쪽이 다른 직사각형의 왼쪽보다 크다
            or 한 직사각형의 아래가 다른 직사각형의 위보다 크다. (두개 교차검증)

        해당 분기를 넘는다면, 겹치는 직사각형의 넓이를 구해주면 되는데,
        이건 4개의 x좌표, y좌표를 정렬한 다음 3번째 큰거 - 2번째 큰거를 해주면 된다.
        """

        if ax2<=bx1 or ax1>=bx2 or ay1>=by2 or ay2<=by1:
            return (ax2-ax1)*(ay2-ay1) + (bx2-bx1)*(by2-by1)
        x_arr = sorted([ax1,ax2,bx1,bx2])
        y_arr = sorted([by1,by2,ay1,ay2])

        x = x_arr[2]-x_arr[1]
        y = y_arr[2]-y_arr[1]

        return (ax2-ax1)*(ay2-ay1) + (bx2-bx1)*(by2-by1) - (x*y)
