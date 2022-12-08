class Solution:
    """
    text에 주어진 공백의 갯수를 세고, 그 갯수를 단어의 수만큼 나눠서 공백을 단어 사이에 끼워넣는다
    나누어 떨어지지 않는경우, 맨 마지막 단어 뒤에 나머지 공백을 붙여서 계산한다.
    """
    def reorderSpaces(self, text: str) -> str:
        space_cnt = 0
        for t in text:
            if t==" ":
                space_cnt+=1

        arr=text.split(" ")

        while "" in arr:
            arr.remove("")
        print(arr)
        
        try:
            space_amount = space_cnt//(len(arr)-1)
            space_end = space_cnt%(len(arr)-1)
        except:
            space_amount = 0
            space_end = space_cnt

        return (" "*space_amount).join(arr)+" "*space_end
