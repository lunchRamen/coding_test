import sys
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        first = sys.maxsize
        second = sys.maxsize

        """
        first, second를 max로 설정해놓고, for문을 돌리면서
        first를 먼저 설정(i<=first)
        그 다음 second를 설정 (i<=second and first<i) 첫번째보단 크고, 두번째보단 작거나 같을때
        그 다음 third를 설정 (first<second<i) -> third=i 찾음

        생각하기 어렵다.
        """

        for i in nums:
            if i<=first:
                first = i
            elif i<=second and first<i:
                second = i
            elif first < second < i:
                return True
        
        return False
