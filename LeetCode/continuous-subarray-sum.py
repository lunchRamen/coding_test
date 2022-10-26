class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
      """
      특이한 구간합 문제.
      보통은 메모제이션으로 모든 부분합을 구한 다음, 각 부분합의 차를 이용해 구간합을 구하는데,
      그러면 여기선 시간초과가 난다.
      그래서 for문 하나로 통과할 수 있게끔 짜야하는데, 나머지연산을 통해 메모제이션을 한다.
      매 반복마다 s+=nums[i]와 s%=k를 하면서, 0~k-1의 나머지들에 몇번째 인덱스까지의 부분합이 들어가는지 구한다.
      만약 해당 나머지가 이미 dic에 있다면, dic[s]와 0~nums[i]까지의 합의 차가 k라는 뜻이므로,
      i-dic[s]>=2까지 체크하면 True를 return하고, 아니라면 메모제이션을 계속 진행해준다.
      """
        dic = dict()
        dic[0]=-1
        s=0

        for i in range(len(nums)):
            s+=nums[i]
            if k != 0:
                s%=k
            if s in dic:
                if i-dic[s]>=2:
                    return True
            else:
                dic[s]=i
        return False
