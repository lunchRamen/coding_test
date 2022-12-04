from collections import defaultdict
class Solution:
    """
    두개의 문자열이, "치환될 수 있는가"에 대한 문제.
    치환의 과정은, 문자 두개를 swap하고, 빈도수가 같은 문자들을 바꾸고 등등의 과정이 있지만
    제일 중요한것은, 두 문자열에 등장하는 문자들의 빈도수가 완전히 같아야하고, 치환될 수 있는 문자열들이 완전히 같아야 한다는 것.
    -> dict으로 key는 문자들 value는 빈도수가 등장하는데, 각각 배열로 만들어서 두개가 같은지 판단하고, 길이가 같은지 판단하여 맞으면 true, 아니면 false를 return한다.
    """
    def closeStrings(self, word1: str, word2: str) -> bool:

        dic1 = defaultdict(int)
        dic2 = defaultdict(int)

        for i in word1:
            dic1[i]+=1
        for i in word2:
            dic2[i]+=1
        
        arr1 = sorted(dic1.values())
        arr2 = sorted(dic2.values())

        char1 = sorted(dic1.keys())
        char2 = sorted(dic2.keys())

        if arr1 == arr2 and len(word1)==len(word2) and char1 == char2:
            return True
        else:
            return False
