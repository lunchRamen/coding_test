class Solution:
    def maximum69Number (self, num: int) -> int:
        maxNum=num
        """
        그냥 매 자리 돌면서, 9면 6으로 6이면 9로 바꿔보면 됨.
        """

        strNum=str(num)

        for i in range(len(strNum)):
            if strNum[i]=="9":
                continue
            else:
                temp = strNum[:i]+"9"+strNum[i+1:]
                maxNum=max(maxNum,int(temp))

        return maxNum
