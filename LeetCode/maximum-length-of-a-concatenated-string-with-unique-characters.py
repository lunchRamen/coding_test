class Solution:
    def maxLength(self, arr: List[str]) -> int:
        answer=0
        temp=[""]
        """
        arr에 있는 모든 배열을 돌려도 시간이 남는다. 모든 조합을 돌릴 예정.
        이중 반복문으로, arr을 돌리고, 임시배열을 돌리면서
        문자열 + 임시배열 문자열을 했을때, 중복이 없다면 -> 이걸 다시 임시배열에 넣고, max_len을 갱신한다.
        이걸 return해주면 됨.
        괜히 dic을 쓰면서 세주려고 하다가, 문제를 훨씬 꼬아버렸다.
        문제를 잘 읽어보면, "중복되지 않는 문자를 갖고있는 최대문자열의 길이"만 구하면 됐다.
        """
        
        for s in arr:
            for t in temp:
                word = s+t
                if len(s+t) != len(set(s+t)):
                    continue
                temp.append(word)
                answer=max(answer,len(word))
        return answer
