def solution(n, arr1, arr2):
    answer = []
    
    #단순 구현. 10진수를 2진수로 바꾸고, 2진수에 맞게끔 # 혹은 공백문자의 문자열로 만든다음, 두개의 문자열을 비교하며 정답문자열을 구현.
    
    arr1Str=["" for _ in range(n)]
    arr2Str=["" for _ in range(n)]
    
    for i in range(len(arr1)):
        temp=arr1[i]
        tempStr=""
        while temp:
            num=temp%2
            tempStr+=str(num)
            temp=temp//2
        while True:
            if len(tempStr)==n:
                break
            tempStr+="0"
        tempStr=tempStr[::-1]
        for t in tempStr:
            if t=="1":
                arr1Str[i]+="#"
            else:
                arr1Str[i]+=" "
    
    for i in range(len(arr2)):
        temp=arr2[i]
        tempStr=""
        while temp:
            num=temp%2
            tempStr+=str(num)
            temp=temp//2
        while True:
            if len(tempStr)==n:
                break
            tempStr+="0"
        tempStr=tempStr[::-1]
        for t in tempStr:
            if t=="1":
                arr2Str[i]+="#"
            else:
                arr2Str[i]+=" "
    for i in range(len(arr1Str)):
        temp=""
        for j in range(len(arr1Str[i])):
            if arr1Str[i][j]=="#" or arr2Str[i][j]=="#":
                temp+="#"
            if arr1Str[i][j]==" " and arr2Str[i][j]==" ":
                temp+=" "
        answer.append(temp)
    return answer
