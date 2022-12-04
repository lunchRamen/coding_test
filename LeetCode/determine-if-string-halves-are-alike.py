class Solution:
    """
    문자열 s를 반 잘랐을때, 2개의 문자열에 등장하는 모음의 갯수가 같은지 판단하는 문제
    문자열 반으로 자르고, vowels를 set으로 만들어, 각 문자열에서 등장하는 횟수를 세주고, 같으면 True 다르면 False를 return.
    """
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

        a = s[:len(s)//2]
        b = s[len(s)//2:]

        numA =0
        numB =0

        for i in a:
            if i in vowels:
                numA+=1
        for i in b:
            if i in vowels:
                numB+=1
        
        if numA==numB:
            return True
        else:
            return False
