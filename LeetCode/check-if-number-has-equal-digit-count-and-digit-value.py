from collections import defaultdict
class Solution:
    """
    idx의 등장횟수가 num[idx]와 다르면 -> false
    다 같으면 true

    주의해야할 점은, 등장횟수는 int형인데 주어진 num은 str라서 int로 형변환을,
    dic의 key값은 숫자형 str값이라 str로 형변환을 해줘야한다는 점.
    """
    def digitCount(self, num: str) -> bool:
        dic = defaultdict(int)

        for n in range(len(num)):
            dic[num[n]]+=1
        for i in range(len(num)):
            if dic[str(i)] != int(num[i]):
                return False
        return True
