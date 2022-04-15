
"""
이분탐색.
times를 정렬한 후,
최선의 상황과 최악의 상황을 상정하고

low가 high보다 커지는 순간의
answer의 middle값을 가져온다.

이게 어떻게 되냐?
low와 high의 middle값을 정해서,
middle 값을 times[i]로 나눈값(=middle 시간동안 심사 가능한 사람 수)
를 다 더해봤을때,
해당 값이 n보다 크다면 high를 mid-1로 조정해주고
                작다면 low를 mid+1로 상향시켜줘서 검색 범위를 절반씩 좁힌다.

0~최악의 경우(제일 오래걸리는 심사대에서 모든사람이 검사)부터 시작해서
해당 값을 2로 나눈 몫을 middle로 잡고,

middle을 왜 구하냐면, 최악의 경우//2를 했을때가
평균 시간으로 잡은거라 평균시간을 각 심사대에서 심사했을때
몇명을 심사 할 수 있느냐에 대해서 구하려고.
몫으로 하는 이유도 나누어 떨어지는 최선의 경우만 취하려고.

이렇게 구해진 middle 시간동안 심사할 수 있는 사람들인 check를 n과 비교해봤을때
check가 n보다 크거나 같다면?
right를 middle로 조정해서 범위를 좁히고

check가 n보다 작다면?
left를 middle+1로 조정해서 범위를 좁힌다.

이렇게 진행하는데, while문에 left!=right이 되면 안되는 이유는
left와 right는 애초부터 다르기때문이고 left가 right과 같아지는 시점을
하기 위해선 left<right을 해야 left와 right가 증감하면서 범위가 좁혀진다.

그리고 실제로 출력해보면 check==n이여도 right=middle로 조정이 되는데
left<right 조건을 탈출하기 위해서 right를 한칸씩 좁혀들어가는 것.
"""

def solution(n, times):
    answer = 0
    times.sort()
    
    left=times[0]
    right=times[len(times)-1]*n
    
    while left < right:
        middle=(left+right)//2
        check=0
        for i in range(len(times)):
            check+= middle // times[i]
        if check >=n:
            right=middle
        else:
            left=middle+1
    answer=left  
    return answer