class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        """
        파이썬으로썬 너무 쉬운 문제.
        list -> string으로 변환시킬 수 있는 "".join()을 알고있느냐,
        파이써닉 코드를 위한 True code if 조건문 else False code를 이해하고있느냐 정도.
        파이썬 내장 라이브러리다보니, 속도도 빠름.
        """
        return True if "".join(word1) == "".join(word2) else False
