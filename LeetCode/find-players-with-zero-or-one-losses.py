from collections import defaultdict
class Solution:
    """
    사람들을 2그룹으로 나눈다.
    1. 한번도 지지 않은 사람
    2. 한번만 진 사람
    2번은 쉽다. 그냥 dict로 패배한 횟수를 세서, 1인 사람들을 추가시켜놓으면 된다.
    1번이 따져줘야하는데,
    일단 모든 user들에 대해 set으로 모아둔 다음, loser에 대한 count를 다 진행한 다음의 dict에 대하여
    user인데 lose에 기록되지 않은 사용자의 경우, 0으로 초기화 해준다.
    그런 후, lose[user]==0인것에 대해 추가해주면 된다.
    또한, 각각 오름차순 정렬후 return.
    """
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lose = defaultdict(int)
        user = set()

        for winner,loser in matches:
            user.add(winner)
            user.add(loser)
            lose[loser]+=1
        
        for u in user:
            if u not in lose:
                lose[u]=0
        
        answer = [[],[]]

        for key,value in lose.items():
            if value == 1:
                answer[1].append(key)
        
        for u in user:
            # 매치에 참가한 유저중, 패가 1이 아닌것
            if u in lose and lose[u]==0:
                answer[0].append(u)
        answer[0].sort()
        answer[1].sort()
        return answer
