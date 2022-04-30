"""
LRU알고리즘이 적용된 캐시.
LRU의 특징은 가장 최근에 입력받은것들만 캐시에 남기는것.
(이미 캐시에 있더라도, 순서를 고려하기위해 없앴다가 다시 추가함)

그리고 여기서 주의할 점은, 대소문자 구분이 없다는 것.
그래서 cities[i].lower()한걸로 탐색을하고,

1.cache에 해당 도시가 있는 경우 / 없는 경우로 나누고
만약 있다면, 해당 도시를 지웠다가 다시 추가하면서 1초추가

만약 없다면, 현재 cache가 꽉 찼는지/아닌지로 다시 비교
만약 꽉 찼다면,(>=len(cache)) 추가한 다음, pop(0)하고, 시간추가
꽉 안찼다면, 그냥 추가하고 시간추가.
"""

def solution(cacheSize, cities):
    answer = 0
    
    cache=[]
    
    for i in range(len(cities)):
        city=cities[i].lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer+=1
        else:
            if len(cache)>=cacheSize:
                cache.append(city)
                cache.pop(0)
                answer+=5
            else:
                cache.append(city)
                answer+=5
            
    return answer