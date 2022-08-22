class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        cnt=0
        if n==1:
            return True
        if n<=0:
            return False
        while True:
            if n==1:
                break
            if n%4!=0:
                return False
            n//=4
            cnt+=1
        #print(cnt)
        #if n<0 and cnt%2==0:
        #    return False
        return True
