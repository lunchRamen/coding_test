from collections import defaultdict
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        """
        투 포인터로 풀려했으나, "부분합"문제가 아니라, "부분배열"문제라서 적합하지 않다.
        우리가 구하려는건, nums1의 부분수열과 nums2의 부분수열중 "가장 긴 공통되는 부분수열"을 찾으려는것
        -> DP로 풀어야한다.
        
        2차원 dp를 만들어,
        dp[i][j] = nums1의 i번째와 nums2의 j번째 원소까지 공통되는 부분수열의 최대값을 저장한다.
        i나 j가 0인경우엔, 1로 세팅을 하고, 나머지는 0으로 세팅한다.
        그래서 nums[i]==nums[j]인 경우엔 dp[i-1](nums1[i-1]번째까지의 최대합)[j-1](nums2[j-1]까지의 최대합) +1 이되는것.
        = nums1배열의 i-1번째까지, nums2의 j-1까지의 공통 부분수열의 최장길이 +1(nums1[i]==nums2[j]니까)가 되는것.
        이걸 각 조건문에 걸릴때마다 answer를 갱신시켜주면 정답이 된다.
        
        input조건이 len(nums1)<=1000이라 2중 for문 시간초과가 안나야하는데, 릿코드 현재 문제인듯.
        """
        answer = 0
        dp = [[0]*len(nums1) for _ in range(len(nums1))]
        
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    if i ==0 or j == 0:
                        dp[i][j]=1
                    else:
                        dp[i][j]=dp[i-1][j-1]+1
                    answer = max(answer,dp[i][j])  
        return answer
        
