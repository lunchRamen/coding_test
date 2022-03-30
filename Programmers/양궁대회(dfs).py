"""
bfs와 동작 자체는 똑같음
해당 과녁에 어피치 +1 만큼 쏜다 or 안쏘고 넘긴다

이걸 큐에 담아서 탈출조건을 걸지
함수에 담아서 탈출조건을 걸지가 차이점.

dfs에 담겨있는 인자는
어피치 과녁,라이언과녁,남은 화살갯수,현재 과녁

그래서 i==11(=0번째과녁)
n!=0 (화살이 아직 남았다면)
남은 화살을 0점 과녁에 다 꽂고
라이언의 과녁과 어피치의 과녁을 점수로 환산해 비교하는
calcScoreDiff를 호출해서 비교.
모든 과녁을 돌면서 둘다 맞히지 않았으면 넘어가고
어피치가 같거나 더 많이 맞췄으면 어피치에 점수를,
라이언이 더 많이 맞췄으면 라이언에 점수를 더해서
lion-apeach를 return 해준다.

만약 계산한 결과가 <=0이라면? 더이상 볼 필요가 없음-> continue
해당 조건문을 통과했단건 라이언이 점수가 더 높단거니까
result를 라이언과녁을 복사해서 놓고,
해당 차이가 maxDiff와 비교해서 크다면 answer를 새롭게 갱신해주고
같다면 answer.append로 해준다.

그래서 위에 i==11에따른 조건 처리를 다 끝냈다면
이제 재귀를 돌리면 되니까

어피치의 i번째 과녁이 남은 화살갯수보다 적다면,
해당 과녁 먹고 재귀를

어피치 화살갯수가 더 많다면,
해당과녁은 넘김.

그리고 같은 maxGap일 경우, 가장 낮은 과녁판을 많이 맞힌 걸 return해주는걸
answer.sort(key=lambda x:x[::-1],reverse=True)로 표현했는데,
answer에 담긴 maxGap의 여러 배열들을 맨뒤에서부터 돌면서,내림차순으로
정렬을 해주면 되는데, 왜냐하면

answer에 담긴 배열의 경우 다
[x,x,x,x,x,x,x,x,x,x,x]의 11개의 원소가 담긴 원소일 것이고,
해당 원소에서 가장 뒤에쪽([::-1])부터 많은걸(내림차순)원하기 때문에
answer의 배열의 원소(=inner배열)들을 가장 뒤에서부터 많은 순서대로 정렬을
해주면, 우리가 원하는 가장 낮은 점수를 가장 많이 맞힌 경우를 return하게 된다.
그래서 return answer[0]을 해주면 됨.

"""

import copy
MAX_SCORE_DIFF = 0
answers = []
# 라이언과 어피치의 점수 차이를 계산하는 함수
def calcScoreDiff(info, myshots):
    apeach, lion = 0, 0
    for i in range(11):
        if (info[i], myshots[i]) == (0, 0):
            continue
        if info[i] >= myshots[i]:
            apeach += (10 - i)
        else:
            lion += (10 - i)
    return lion - apeach
def dfs(info, myshots, n, i):
    global MAX_SCORE_DIFF, answers
    if i == 11:
        if n != 0:
            myshots[10] = n
        scoreDiff = calcScoreDiff(info, myshots)
        if scoreDiff <= 0:
            return
        result = copy.deepcopy(myshots)
        if scoreDiff > MAX_SCORE_DIFF:
            MAX_SCORE_DIFF = scoreDiff
            answers = [result]
            return
        if scoreDiff == MAX_SCORE_DIFF:
            answers.append(result)
            return
    # 점수 먹는 경우
    if info[i] < n:
        myshots.append(info[i] + 1)
        dfs(info, myshots, n - info[i] - 1, i + 1)
        myshots.pop()
        # 점수 안먹는 경우
    myshots.append(0)
    dfs(info, myshots, n, i + 1)
    myshots.pop()
def solution(n, info):
    global MAX_SCORE_DIFF, answers
    dfs(info, [], n, 0)
    if answers == []:
        return [-1]
    answers.sort(key = lambda x : x[::-1], reverse=True)
    return answers[0]