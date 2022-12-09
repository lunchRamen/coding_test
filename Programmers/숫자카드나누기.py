"""
철수, 영희의 카드뭉치들의 수를 통해 각각 최대공약수를 구하고,
각각 서로의 카드뭉치를 탐색하며, gcd철수가 영희 카드중 나누어떨어지면, 0으로 만들고 break
gcd영희가 철수 카드중 나누어 떨어지면, 0으로 만들고 break해서
철수 영희중 최대값을 return하면 된다.

"최대공약수"란 모든 숫자에 대해, 공통적으로 나누어 떨어지는 수 중 최대값을 의미
이 최대공약수의 약수들 중 상대편 카드뭉치에서 하나도 안나눠떨어지는 수의 최대값을 저장하고
이 최대값들 중 큰 값을 return.
"""
def solution(arrayA, arrayB):
    answer = 0
    def getNum(a,b):
        while b:
            a,b=b,a%b
        return a
    
    def getGcd(array):
        gcd_num = array[0]
        for i in range(1,len(array)):
            gcd_num = getNum(gcd_num,array[i])
        return gcd_num

    gcdA = getGcd(arrayA)
    gcdB = getGcd(arrayB)
    
    def get_arr(num):
        arr = []
        for i in range(2,num+1):
            if num%i==0:
                arr.append(i)
        return arr
    gcdA_arr = get_arr(gcdA)
    gcdB_arr = get_arr(gcdB)
    max_A = 0
    max_B = 0
    
    for j in range(len(gcdB_arr)):
        flag = True
        for i in range(len(arrayA)):
            if arrayA[i]%gcdB_arr[j] == 0:
                flag=False
                break
        if flag:
            max_B = gcdB_arr[j]
               
    for j in range(len(gcdA_arr)):
        flag = True
        for i in range(len(arrayB)):
            if arrayB[i]%gcdA_arr[j] == 0:
                flag=False
                break
        if flag:
            max_A = gcdA_arr[j]
    
    return max(max_A,max_B)
