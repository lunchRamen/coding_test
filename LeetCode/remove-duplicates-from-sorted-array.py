class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        솔직히 set으로 자른다음 나머지를 붙이는게 왜 정답이 안되는지 이해가 안간다.
        다만, 공간복잡도를 1로 해야한다는 점때문에 copy로 객체 복사는 되지 않고,
        지우는게 배열 그 자체에서 처리하는 로직이라 그런거 같다.

        로직은 모든 배열을 순회할때까지
        연속된 같은 원소를 찾으면 remove하고, 없으면 i+=1
        그리고 l은 매 반복문 실행마다 갱신해준다.
        """
        
        i = 0
        l = len(nums)

        while i<l-1:
            if nums[i]==nums[i+1]:
                nums.remove(nums[i+1])
            else:
                i+=1
            l=len(nums)
        return len(nums)
