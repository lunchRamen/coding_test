from itertools import permutations
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        strN=str(n)
        
        arr=list(permutations(strN,len(strN)))
        
        if n==1:
            return True
        for i in arr:
            if i[0]=='0':
                continue
            temp="".join(i)
            temp=int(temp)
            flag=True
            while temp:
                if temp==1:
                    break
                if temp%2==1:
                    flag=False
                    break
                temp//=2
            if flag:
                return True
                
        
        return False
