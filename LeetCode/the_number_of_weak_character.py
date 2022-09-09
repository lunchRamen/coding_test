class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key= lambda x : (-x[0],x[1]))
        """
        일단, 최악의 케이스를 따졌을때, 정렬 이후엔 무조건 반복문 하나로 해결해야한다.
        dic을 썼든 뭘 썼든 반복문 2개를 돌리는 순간 시간 초과나는 케이스가 존재.
        
        answer에 추가 될 조건
        
        a1 < a2
        d1 < d2
        
        만약 오름차순으로 구현한다면,
        여러가지를 시도해봤는데 잘 안됐다.
        attack그룹이 올라갈때마다, 
        
        왜냐하면, 오름차순이라면 attack이 올라갈때마다, defense default를 뭐로 잡을지 달라지기때문
        그에 반해 내림차순이라면, attack을 고려하지 않고, maxDefense를 두면
        원소가 지날때마다 각 attack group에서 가장 높은 maxDefense와 비교하기때문에
        attack이 내려갈때마다 defense default를 뭐로 잡을지 고민하지 않아도 된다. -> 이미 maxDefense가 default.
        
        로직 자체는 간단하게 만약 defense<maxDefense면 answer+=1(방어력도 낮다면, weak)
        defense>=maxDefense라면 maxDefense를 업데이트 시켜준다.
        
        
        """
        
        maxDefense = 0
        answer=0
        for a,d in properties:
            if d<maxDefense:
                answer+=1
            else:
                maxDefense=d
            
        return answer
