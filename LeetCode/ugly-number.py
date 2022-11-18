class Solution:
    """
    2,3,5로만 소인수분해가 되는지 물어보는 문제.
    2,3,5로 더이상 안나눠지면, False를 return
    2,3,5로 계속 나눈 결과값이 1이 나오면, True return

    음수와 0,1에 대해선 예외처리를 해줘야한다.
    음수는 2,3,5로만 나누어 떨어질 수 없고
    0은 소인수분해가 되지 않으며
    1은 소인수가 없기떄문. 
    """
    def isUgly(self, n: int) -> bool:
        
        if n == 0:
            return False
        if n == 1:
            return True

        while n != 1:
            flag = True
            if n/2 == int(n/2):
                n = n//2
                flag = False
            elif n/3 == int(n/3):
                n = n//3
                flag = False
            elif n/5 == int(n/5):
                n = n//5
                flag = False
            
            if flag:
                return False

        return True
