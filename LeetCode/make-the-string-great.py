class Solution:
    def makeGood(self, s: str) -> str:

        """
        인접한 두개의 문자가 대-소문자거나 소-대문자로 엮여있으면, 그걸 계속 없애는것.
        그냥 더이상 인접하는게 체크 안될때까지, 하나 발견할때마다 자르고 break한다.
        """
        answer=""
        
        while True:
            flag = True
            for i in range(len(s)-1):
                if abs(ord(s[i])-ord(s[i+1]))==32:
                    flag=False
                    s=s[:i]+s[i+2:]
                    break
            if flag:
                break
        answer=s
        return answer
