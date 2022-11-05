from collections import defaultdict
class Solution:
    def reverseVowels(self, s: str) -> str:
        """
        a,e,i,o,u에 해당하는 곳의 위치와 값을 기억해둔다(dic)
        
        이후 딕셔너리를 돌면서, 문자열의 순서를 바꾼다.
        절반만 바꾸면 안되는 이유
        -> 양쪽이 바뀌어야 되는데, 절반만 돌면 절반만 바뀜.
        만약 절반으로 다 돌리고 싶으면, 양쪽을 다 바꿔주면 됨.
        """
        dic=defaultdict(str)
        cnt = 0
        for i in range(len(s)):
            if s[i] in ["a","e","i","o","u","A","E","O","I","U"]:
                cnt+=1
                dic[i]=s[i]

        s_list = list(s)
        
        
        arr = list(dic.items())
        
        for i in range(len(arr)//2):
            key = arr[i][0]
            value = arr[i][1]
            
            s_list[key]=arr[len(arr)-1-i][1]
            s_list[arr[len(arr)-1-i][0]]=value
        return "".join(s_list)
            
