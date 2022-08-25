class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        dic=dict()
        for i in range(len(magazine)):
            if magazine[i] in dic:
                dic[magazine[i]]+=1
            else:
                dic[magazine[i]]=1
        for i in ransomNote:
            if i not in dic:
                return False
            if i in dic:
                if dic[i]<=0:
                    return False
                else:
                    dic[i]-=1
        return True
