class Solution:
    def countAndSay(self, n: int) -> str:

        arr = []

        arr.append("1")
        arr.append("11")
        arr.append("21")
        arr.append("1211")
        """
        dp로 풀었다.
        n=30밖에 안주어졌지만, 숫자를 카운팅하는거 자체는 상당히 긴 문자열이 나온다. 그래도 n이 워낙작으니 풀리겠다 싶었다.
        보기에서 n=4까지 줬기때문에 여기까진 채워넣고,
        4~30까지 반복문을 돌린다.
        temp로 arr[i-1]를 가져오고,
        숫자가 달라지는 분기점마다 str(cnt)+temp[idx]를 한 다음 cnt=1 idx+=1로 초기화하고 continue
        여기서 주의할 점은 인덱스 오류가 나는 분기점인 idx==len(temp)-1에서는 끝까지 돈거라 str(cnt)+temp[idx]를 하고 break
        하면 된다.
        이후 tempArr를 arr에 append하고 return arr[n-1]하면 끝.
        """

        for i in range(4,30):
            temp = arr[i-1]
            idx = 0
            tempArr=[]
            cnt = 1
            while idx<len(temp):
                if idx == len(temp)-1:
                    tempArr.append(str(cnt)+temp[idx])
                    break
                if temp[idx]!=temp[idx+1]:
                    tempArr.append(str(cnt)+temp[idx])
                    cnt = 1
                    idx+=1
                    continue
                idx+=1
                cnt+=1
            arr.append("".join(tempArr))
        return arr[n-1]
