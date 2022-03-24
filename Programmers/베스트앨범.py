"""
장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
->이게 지금 문제인듯.

이걸 cnt로 따져서 cnt가 0 1 2일때 나눠서 1일때를 분기로 여러 조작으로
만약 재생수로 정렬했는데 같은 값들이 index 1번째부터 ~k번째같이 같을때를 처리해주려고 했는데
결론적으로 실패함.
"""
from collections import defaultdict

def solution(genres, plays):
    answer = []
    temp=defaultdict(list)
    
    for key,value in zip(genres,plays):
        temp[key].append(value)
    temp2=dict()
    for key in sorted(temp):
        temp2[key]=sorted(temp[key],reverse=True)
    
    
    temp3=sorted(temp2.items(), key=lambda x: sum(x[1]), reverse=True)
    
    
    for i in range(len(temp3)):
        cnt=0
        for j in range(len(temp3[i][1])):
            if cnt==2:
                break
            if cnt==1:
                if len(temp3[i][1])==2:
                    for k in range(len(plays)):
                        if temp3[i][1][j]==plays[k]:
                            answer.append(k)
                            cnt+=1
                if len(temp3[i][1])>=3:
                    if temp3[i][1][j]==temp3[i][1][j+1]:
                        minIndex=10001
                        l=j
                        while l<len(temp3[i][1]):
                            for k in range(len(plays)):
                                if temp3[i][1][l]==plays[k]:
                                    minIndex=min(minIndex,k)
                                l+=1
                        answer.append(minIndex)
                        cnt+=1
            if cnt==0:
                for k in range(len(plays)):
                    if temp3[i][1][j]==plays[k]:
                        answer.append(k)
                        cnt+=1
    return answer

"""
정답코드.
딕셔너리를 2개씀. -> 이게 핵심.
장르별 재생횟수,노래인덱스 딕셔너리 하나
장르별 재생횟수의 합 딕셔너리 하나
해서 두번재 딕셔너리를 x[1]로 sort하고, 첫번째 딕셔너리에 갖다 쓰는데,
첫번재 딕셔너리같은 경우는 value가 2차배열이라 key로 접근한 다음 value의 배열 객체에 접근 가능한데,
이걸 각 장르별 재생횟수는 내림차순, 만약 재생횟수가 같다면 인덱스를 오름차순으로 정렬.
이렇게 각 장르별(key) value를 위에 2개의 정렬기준으로 정렬하면, 그냥 2개만 뽑으면 됨.


첫번째꺼는 장르:[[i번째 노래 재생횟수:i],[j번째 노래 재생횟수:j]] 이런식으로.

두번째꺼는 장르:[총 재생횟수]
하는법은 첫번째 딕셔너리의 keys들을 꺼내서(장르들)
-> 각 장르들에 대한 재생횟수를 얻을 수 있음. 객체[0]으로.
그래서 genre_rank[genre]=plays_sum으로 두번재 딕셔너리 완성.

그다음, 1번째 index기준 내림차순으로 정렬을 함 -> 장르별 재생횟수 합이 큰 순서대로 정렬 됨.

그다음, genre_rank를 통해서 dic을 뽑아 낼 수 있는데,
dic의 경우
{
    genre:[[plays[i],i],[plays[j],[j]]]
} 이런식이고
genre_rank는
{
    genre:sum(plays)
} 형태.
근데 genre_rank를 dict이 (key,value)로 들어간 list형태로 변환 시켰기때문에, index형태로 접근이 가능함.
그래서 song_rank는 dic의 genre key에 매핑되는 value들을, 곡 재생수는 내림차순으로, 고유번호는 오름차순으로 정렬시킨 리스트.
그러면, plays[i]기준으로도 오름차순 정렬이 되었으니, 그냥 앞에서부터 2개 넣으면 끝남..
"""
def solution(genres, plays):
    answer = []
    #dic 딕셔너리에 입력 저장- { 장르1: [[노래1 재생 횟수 :노래1 고유 번호],[노래2 재생 횟수: 노래2 고유번호]...]} 형식으로
    dic={}
    for i in range(len(genres)):
        if genres[i] in dic:
            dic[genres[i]].append([plays[i],i])
        else : 
            dic[genres[i]] = [[plays[i],i]]

    #genre_rank 딕셔너리에 각 장르의 모든 곡의 총 재생 횟수 저장- {장르 1 : 모든 장르 1곡의 총 재생 횟수 ,장르 2 : 모든 장르 2곡의 총 재생 횟수...}
    genre_rank ={}
    for genre in dic.keys():
        songs = dic[genre]
        plays_sum = 0
        for song in songs:
            plays_sum+=song[0]
        genre_rank[genre] = plays_sum
    #genre_rank를 재생 횟수가 큰 순으로 정렬 
    genre_rank = sorted(genre_rank.items(), key=lambda x: x[1],reverse=True)
    
    # genre_rank에 저장되어 있는 장르 순으로 dic에서 해당 장르를 key로 가진 value를 확인
    for genre in genre_rank:
        #2차원 배열인 value를 다중 조건으로 정렬 (첫번째 인자인 곡 재생 수를 기준으로 내림차순 정렬 후,
        #                                     두번째 인자인 곡 고유 번호를 기준으로 오름차순 정렬)
        song_rank=sorted(dic[genre[0]], key=lambda x:(-x[0],x[1]))
        best_two = 0
        # 정렬된 배열을 하니씩 확인하면서 answer에 고유 번호를 순서대로 저장 , 만약 한 장르의 곡이 두 곡 저장되면 해당 장르에서 반복 중지
        for song in song_rank:
            answer.append(song[1])
            best_two +=1
            if best_two == 2:
                break

    return answer