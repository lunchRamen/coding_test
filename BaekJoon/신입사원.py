import sys

input=sys.stdin.readline

"""
서류심사성적(arr[i][0])과 면접시험성적(arr[i][1])이

다른 모든 지원자와 비교했을때
arr[i][0]과 arr[i][1]중 적어도 하나가
다른 지원자보다 떨어지지 않는자만 선발.

내가 잘못 생각했던게,
주어진 숫자들은 "등수"임. "점수"가 아니라.

그리고 지원자의수가 100,000이라 완탐 못함(2중 for문 못돌림)
->첫번째로 구현한 2중 for문 제출하니 시간초과뜸.

다른 방법으로 구현해야함.
일단 arr[i][0]이나 arr[i][1]이 1인건 제외해도됨.(1등이니까 무조건 앞섬)

-> arr[i][0]이 1인거에서 arr[i][1]보다 작은것들 체크
-> arr[i][1]이 1인거에서 arr[i][0]보다 작은것들 체크.
이 두개 중 중복되는거 삭제.한 후 len(arr)-len(temp)하면 된다.


통과풀이.
arr[i][0]으로 sort를 하고,
arr[i][1]를 비교대상으로 삼아서
if arr[j][1]<arr[i][1]이라면
j번째사람은 서류는 낮지만, 면접은 높기때문에 통과한다.
그래서 통과한 사람들만 검색할 수 있음.
-> 이미 서류로는 정렬을 한번 했기때문에, 우리가 볼건 면접 등수만 따지면 됨.
그렇다면 합격하는 기준은?
서류 2등은 1등의 면접등수보다 높으면 된다.
이걸 반복하다보면,
서류 n등은 서류 1~n-1등중 면접이 가장 높은(=숫자가 가장 낮은)사람보다
면접 등수가 높으면 된다. 그래서 arr[i][1]이 더 작을때마다 갱신시켜주며,
합격자를 추가시키는 것.
"""

t=int(input())

while t:
    n=int(input())
    arr=[]
    for _ in range(n):
        arr.append(list(map(int,input().split())))
    arr.sort(key=lambda x:(x[0]))
    cnt=1
    p=arr[0][1]
    for i in range(1,n):
        if arr[i][1]<p:
            cnt+=1
            p=arr[i][1]
    print(cnt)
    #1등의 나머지 등수
    # num2=arr[0][1]
    # arr.sort(key=lambda x:x[1],reverse=True)
    # for i in range(len(arr)):
    #     if arr[i][1]>num2:
    #         temp.append(arr[i])
    #     else:
    #         break
    # arr.sort(key=lambda x:x[1])
    # num1=arr[0][0]
    # arr.sort(key=lambda x:x[0],reverse=True)
    # for i in range(len(arr)):
    #     if arr[i][0]>num1:
    #         temp.append(arr[i])
    #     else:
    #         break
    # temp2=list(map(tuple,temp))
    # temp=list(set(temp2))
    # print(temp)
    # print(len(arr)-len(temp))

    t-=1