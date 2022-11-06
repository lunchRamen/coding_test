class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        """
        1이면 , 그냥 처음부터 끝까지 한개씩 뒤로보내보면서 계산해보면 됨
        2이상이면, 결국 k개중 사전순으로 가장 큰거를 뒤로 보내 제일 작을떄까지 반복할것이므로, s를 정렬해서 return해주면 됨.
        """

        if k>1:
            return "".join(sorted(s))

        else:
            return min(s[i:]+s[:i] for i in range(len(s)))
