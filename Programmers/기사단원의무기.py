"""
일반적인 약수로, 기사단의 input만큼 순회하면, 시간초과.
-> 약수의 갯수를 최적화해서 구해야함.
-> 제곱근까지 탐색하고, 나누어 떨어지면, 2개를 더해주면 됨.(다만 i*i != n인 경우)

그다음, 기사단 순회하면서 limit 초과하면 power로 고쳐주고, sum해서 return
"""
def solution(number, limit, power):
    answer = 0
    
    knight = [0 for _ in range(number+1)]
    def get_num(num):
        cnt = 0
        for i in range(1,int(num**(0.5))+1):
            if num%i == 0:
                cnt+=1
                if i**2 != num:
                    cnt+=1
        return cnt
    for i in range(1,number+1):
        knight[i] = get_num(i)
    
    for i in range(1,len(knight)):
        if knight[i]>limit:
            knight[i]=power
        
    return sum(knight[1:])
