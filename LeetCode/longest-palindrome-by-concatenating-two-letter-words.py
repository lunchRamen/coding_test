from collections import defaultdict
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:

        """
        조건 처리가 까다로웠다.
        일단 펠린드롬 문자열로 들어올 수 있는 2가지 경우가 있다.
        1.서로 다른 문자
        2.서로 같은 문자

        1의 경우, 해당 문자열을 reverse한게 dic에 있다면, 두 value값 중 작은걸 추가해주면 된다.
        2의 경우가 문제인데, 펠린드롬으로 만들 수 있는 같은 문자열은 "홀수개 하나만 가능"하다.
        그렇다는건, 짝수개로 맞춰줘야 같은문자인 경우 펠린드롬에 들어갈 수 있다는 것이다.

        더 최적화를 했다면 dic탐색하는 1번의 for문으로 끝났을거같은데, 방법이 생각나지않아
        첫번째 반복문엔 같은문자중 가장 큰 홀수 value를 찾고,
        두번째 반복문엔 하나 빼고 나머지는 value-1을 더해줬다.

        조건문 중 빼먹었던 두번째 반복문에 value%2==1을 빼먹어서 헤맸다.
        """

        dic = defaultdict(int)

        for word in words:
            dic[word]+=1

        answer = 0
        same_odd_word_max = 0
        for key,value in dic.items():
            if key[0] != key[1]:
                reverse_key = key[::-1]
                if reverse_key in dic:
                    min_num = min(value,dic[reverse_key])
                    answer+=min_num
            else:
                if value%2==0:
                    answer+=value
                else:
                    same_odd_word_max=max(same_odd_word_max,value)

        flag = False
        for key,value in dic.items():
            if key[0]==key[1] and value%2==1:
                if value != same_odd_word_max:
                    answer+=value-1
                else:
                    if flag:
                        answer+=value-1
                    flag=True


        return answer*2 + same_odd_word_max*2
