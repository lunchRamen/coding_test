class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        """
        아스키코드를 활용하였다.
        sentence의 소문자를 세어봤을때 1미만이라면 False를, 다 1이상이라면 True를 return한다.
        이걸 더 빠르게 하려면 딕셔너리를 쓰면 되지만, input이 1000이라 26*1000해도 괜찮을거같아 성공.
        """
        for i in range(97,97+26):
            if sentence.count(chr(i)) < 1:
                return False
        return True
