"""
큰수 만들기에서, 처음 생각한 풀이로는 백만자리에 해당하는 숫자에선
당연히 시간초과가 날 수 밖에 없다.
-> 그리디적 사고로 풀어야함.

총 버전 3까지 나옴
첫번째 버전은, number에서 k개만큼 뽑는 조합 중 max를 answer로 return하는것.
이건, 애초에 number가 100만개까지 있을수 있어서 시간초과가 많이 뜸.

두번째 버전은, k개를 변화시킬때까지 for문을 돌면서 number[i]<number[i+1]인 경우에 대해
number[i]를 지우는것.
왜 number[i]<number[i+1]라는 조건이 등장했냐면, 큰자릿수의 작은 숫자부터 제거를 해주는게 좋은데
이것에 대한 기준이 전 자리보다 작다면? 필요없다고 볼 수 있어서.
근데 이것도 10번케이스를 통과하지 못함

세번째 버전은 while문 안의 for문을 없애주는 것.
while의 조건으로써 i를 둬서, 삭제 한 경우 number[i]가 없어졌기 때문에, i+=1을 하면
두칸을 움직이는 거라, i-=2 또는 i-=1을 해줘야한다( i가 첫번째/아닌경우)
그래야 while문 끝에 있는 I+=1에 맞춰서 한칸만 오른쪽으로 이동하는 꼴이 된다.

만약, k개만큼을 충족하지 않은 경우라면 뽑아 놓은 number문자열에서 이미
가장 큰 숫자의 형태로 써져있기 때문에, number[:len(number)-k]만 해주면 된다.
"""
from itertools import combinations
def solution(number, k):
    answer = 0
#     temp=list(combinations(number,k))
    
#     for i in range(len(temp)):
#         t=number
#         for j in range(len(temp[i])):
#             t=t.replace(temp[i][j],"",1)
#         answer=max(answer,int(t))
    visit=[False for _ in range(len(number))]
    
    cnt=0
    prevMax=number[len(number)-1]
    for i in range(len(number)-2,-1,-1):
        if number[i]>=prevMax:
            continue
        else:
            prevMax=number[i]
            visit[i]=True
            cnt+=1
            if cnt==k:
                break
    t=""
    for i in range(len(visit)):
        if not visit[i]:
            t+=number[i]
    print(t)
    
    return str(answer)


def solution(number, k):
    answer = ''
    # while True:
    #     if k==0:
    #         break
    #     flag=False
    #     for i in range(len(number)-1):
    #         if number[i]<number[i+1]:
    #             flag=True
    #             number=number[:i]+number[i+1:]
    #             k-=1
    #             break
    #     if not flag:
    #         break
    i=0
    while i<len(number)-1 and k>0:
        if number[i]<number[i+1]:
            number=number[:i]+number[i+1:]
            k-=1
            if i>0:
                i-=2
            else:   #0번째 인덱스를 삭제했을때
                i-=1
        i+=1
    answer=number[:len(number)-k]
    return answer