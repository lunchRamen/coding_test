class Solution:
    def numberOfSteps(self, num: int) -> int:

        answer: int =0

        while num:
            answer+=1
            if num%2==0:
                num/=2
                continue
            else:
                num-=1
                continue
        return answer
