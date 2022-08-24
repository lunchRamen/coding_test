class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False
        
        while n:
            if n==1:
                break
            if n%3!=0:
                return False
            n//=3
        return True
