"""
dfs:차이가 1인 노드를 찾을때, 이미 방문했던 노드는 다시 방문하면 안되므로 이를 처리해주다가 dfs의 재귀가 끝나는 지점에서 차례로 다시 방문을 풀어주어야한다

bfs:같은 리프선상에 있는 노드를 큐에 넣는데, 이때 그다음 depth로 넘어갈때 큐에있는걸 하나씩 빼주는게 아니라 전체를 다 빼도록 하여 한번의 루프당 하나의 depth로 넘어갈수 있도록 해야한다. 
"""

"""DFS VERSION 1"""
visit=[] #해당 인덱스 방문 여부
result=[] #begin이 target이 되기까지 걸린 횟수.
def solution(begin, target, words):
    answer = 0
    
    for _ in range(len(words)):
        visit.append(0)
    
    if target not in words: #target이 words에 없다? 단어변환이 안됨 -> 0반환.
        return answer
    
    def dfs(word,depth): #재귀하는 단어, 변환한 횟수.
        if word==target: #재귀를 마칠 조건문. 재귀로 변한 단어가 target과 같다면,
                         #result에 변환횟수를 넣고 return.
            result.append(depth)
            return
        for i in range(len(words)): #words를 살펴보는데
            if visit[i]==1: #방문했으면 건너뛰고
                continue
            if checkDiff(word,words[i])==1: #재귀하는 단어와 words에 있는 단어가 1글자 차이라면
                visit[i]=1 #해당 인덱스 방문 체크.
                dfs(words[i],depth+1) #다음 재귀시킬 단어는 words[i]고, 변환횟수 1추가.
                visit[i]=0 #재귀가 끝나면 방문 여부를 0으로 초기화 시켜줌.
    dfs(begin,0)
    answer=min(result) #begin -> target으로 단어변환 시키는 경우가 많을 경우가 있을수 있어 최소 추출.
    return answer

def checkDiff(word,target):
    diff=0
    for i in range(len(word)):
        if word[i]!=target[i]:
            diff+=1
    return diff


"""BFS"""
from collections import deque

def solution(begin,target,words):
    global answer
    answer=0
    
    if target not in words:
        return answer
    
    def bfs(begin):
        global answer
        q=deque()
        q.append(begin) #큐에 begin "단어"를 넣음.
        
        while True:
            answer+=1 #일단 answer+=1 (q에 조작을 가할때마다 +=1씩.)
            cur=[]
            while q: #cur배열에 q를 순서대로 다 넣음
                cur.append(q.popleft())
                
            if target in cur: #만약 cur배열에 타겟이 있으면?
                return

            for i in range(len(cur)): #cur배열에 있는거랑 
                for j in range(len(words)): #words배열에 단어들을 비교.
                    if checkDiff(cur[i],words[j])==1: #만약 1글자 차이나면
                        q.append(words[j]) # q에 words[j]를 추가.
            #위에 2중 for문때문에 q에는 begin부터 한글자씩 차이나는 단어들이
            #q에 들어가게 된다.(q에 target이 들어갈때 까지.)
            #answer-1해주는 이유는 아직 2중 for문을 가지않고 if문으로 return됐을때도
            #answer는 +=1된 상태이기때문.

            for i in q: #q에 있는 원소들 중
                if i in words: #words에 단어가 있으면
                    words.remove(i) #삭제. (위에 2중 for문에서 쓸 필요가 없으니까.)
    bfs(begin)
    return answer-1 #while문에서 answer+=1 다음 target i cur문이 있으니까 -1을 해줘야함.

def checkDiff(word,target):
    diff=0
    for i in range(len(word)):
        if word[i]!=target[i]:
            diff+=1
    return diff


"""
DFS VERSION 2

버전1과 달라진점
1.words에 시작 단어를 추가하고
2.2중 for문으로 words의 단어들 중 i번째 단어와 1글자 차이나는 단어들을 node_dic[i]에 배열형태로.
(여기서 중요한점은, dict으로 해놨기때문에 단어로 매핑이 됨. node_dic["hit"]=["hot",] 이런식.)
3.그 다음 begin단어,target단어,node_dic(=i번째 단어와 한글자씩 다른 단어들이 있는 배열),방문여부
  변환횟수를 담아서 dfs를 돌림.
4.그래서 만약 begin==target이면 변환횟수(num을) num_list에 담음.
5.그래서 node_dic[begin]으로 해당 딕셔너리에 들어있는 단어들로 dfs를 dfs(i,target,words,visit,num+1)
  로 돌림.
=dfs와 bfs짬뽕 형식인듯. dict형식으로 배열을 구성한거 자체가.

-> node_dic에 words[i]번째 단어에 대해 해당 단어와 1글자씩 차이나는걸 인덱싱해서 저장.
   그래서 node_dic[begin]에 매핑되는 배열로 dfs를 재귀호출하면,
   node_dic[begin`]이렇게 계속 재귀호출 되면서 begin==target되면 num_list에 num이 추가됨

그래서 solution의 return문이 min(num_list).
"""


num_list=[]
def solution(begin,target,words):
    answer=0
    
    if target not in words:
        return answer
    
    words.append(begin)
    visit={}
    for i in words:
        visit[i]=False
    
    node_dic={}
    for i in words:
        node_dic[i]=[]
        
    for i in words:
        for j in words:
            if checkDiff(i,j)==1:
                node_dic[i].append(j)
    dfs(begin,target,node_dic,visit,0)
    return min(num_list)

def checkDiff(word,target):
    diff=0
    for i in range(len(word)):
        if word[i]!=target[i]:
            diff+=1
    return diff

def dfs(begin,target,node_dic,visit,num):
    visit[begin]=True
    if begin==target:
        num_list.append(num)
        return
    
    for i in node_dic[begin]:
        if visit[i]==True:
            continue
        else:
            dfs(i,target,node_dic,visit,num+1)
            visit[i]=False