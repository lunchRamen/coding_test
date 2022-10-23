class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        """
        1~n까지 있는 숫자 중 두번 들어가있는 숫자와, 빼먹은 숫자를 차례대로 배열로 return해주는 문제.
        dic으로 각 숫자를 체크한다음,
        만약 없거나, 체크된게 2번이라면 추가한다.
        여기서 주의할 점은, arr[0]이 두번 체크된거, arr[1]이 없는거로 들어가야한다는 점.
        .append를 쓰면 순서가 꼬일수 있으므로 미리 2개의 공간을 할당한 다음, 각 idx에 추가한다.
        """

        arr = [0,0]
        dic = dict()
        max_num = len(nums)
        for num in nums:
            if num in dic:
                dic[num]+=1
            else:
                dic[num]=1
        
        for i in range(1,max_num+1):
            if i not in dic:
                arr[1]=i
            else:
                if dic[i]==2:
                    arr[0]=i


        return arr
