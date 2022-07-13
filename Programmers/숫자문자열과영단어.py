def solution(s):
    answer = 0
    numArr = {
        "zero":0,
        "one":1,
        "two":2,
        "three":3,
        "four":4,
        "five":5,
        "six":6,
        "seven":7,
        "eight":8,
        "nine":9}
    
    for num,number in numArr.items():
        if num in s:    #문자열에 해당 영어가 있는 경우
            numLen=len(num)
            i=0
            while True:
                if s[i:i+numLen]==num:
                    change=s[i:i+numLen]
                    changer=str(number)
                    s=s.replace(change,changer)
                    break
                else:
                    i+=1
    answer=int(s)
    return answer