class Solution:
    """
    같은 길이를 가진 문자열 s1,s2,baseStr가 주어진다.
    우리는 s1[i]와 s2[i]가 동일한 값으로 친다.
    -> s1과 s2를 통해 동일한 값들의 집합들을 구했다면,
    baseStr를 동일한 문자열들의 집합들로 바꿨을 때 가장 작은 문자열이 return되도록.

    union-find로
    s1과 s2에 대해 make-set & union하고
    baseStr에 대해 가장 작은 문자열로 find한다.

    동등한 disjoint-set에 대해 대표문자열을 나타내기 위해
    key(대표 문자) = value(같은 집합에서 가장 작은 문자)로 dict을 만든다.

    find연산의 경우 dict에 key값이 저장되지 않은 경우
    parent[x] = x로 초기화를 하고

    x != parent[x] 인 경우, 해당 disjoint-set의 루트노드까지 타고 올라간다.
    = find(parent[x]). 근데 우린 루트노드를 union에서
    같은 disjoint-set중 가장 작은 대표값으로 하기때문에
    가장 작은 문자를 가진 루트노드로 find가 타고 올라간다.

    그 다음 union의 경우
    find(x), find(y)를 하고 "문제에 주어진 조건으로" 문자를 비교했을 때
    더 작은 문자로 parent[find(x or y)]를 갱신한다.
    이렇게 되면 disjoint-set의 대표값들이 union된다.

    이렇게 find-union함수를 만들고

    s1에 대해 순회하며
    find(s1[i]) != find(s2[i])이라면
    각각의 disjoint-set을 union하고,

    이렇게 union된 parent를
    baseStr를 순회하면서 find(bastStr[i])로 가장 작은 문자값으로 할당해주면 된다.
    """
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:

        parent = dict()

        def find(x: str) -> str:
            if x not in parent:
                parent[x] = x
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x:str, y:str) -> None:
            xr,yr = find(x),find(y)
            if xr==yr:
                return None
            if xr<yr:
                parent[yr] = xr
            else:
                parent[xr] = yr
            return None

        for i in range(len(s1)):
            if find(s1[i]) != find(s2[i]):
                union(s1[i],s2[i])
        
        answer = ""
        for s in baseStr:
            answer+=find(s)
        return answer
