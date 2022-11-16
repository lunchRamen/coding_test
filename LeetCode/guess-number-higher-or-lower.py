# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:
import random
class Solution:
    def guessNumber(self, n: int) -> int:
        """
        처음엔 random 모듈을 통해서, 제출을 했는데 시간 초과가 떴다.
        아마 random.randint 자체에 대한 시간복잡도가 소요돼서 그런거같다
        어차피 구하려는건, 1~n중 guess(number)를 던졌을때 같은 값만 찾으면 되니, 이분탐색으로 돌리면 된다.
        start+end에 소괄호를 안쳐서 몫연산이 먼저되어 통과가 안됐었다.
        """


        start = 1
        end = n

        while start<=end:
            mid = (start+end)//2
            if guess(mid)==0:
                return mid
            elif guess(mid)==1:
                start = mid+1
            elif guess(mid)==-1:
                end = mid-1
