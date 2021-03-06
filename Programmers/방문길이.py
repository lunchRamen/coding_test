"""
이 문제에서 제일 중요한건 선분의 방문에 있어서
왼->오를 통해서 방문한것과 왼<-오를 통해서 방문한게
같다는 것을 구현해야함.

이것은, visit에 선분을 구성하는 양 점을 추가하는데
점에 있어서 좌표값의 x,y가 좌표1<좌표2가 되게끔 visit에 추가를 한다면
만약 왼(0,0) 오(0,1)이라면
왼->오 = (0,0),(0,1)
오->왼 = (0,1),(0,0)이 되어 중복처리가 안된것을
좌표평면 처리를 x와y의 값이 작은 순으로 처리를해줘서
오->왼도 (x,y),(x-1,y)로 해주는 시작정점,도착정점을
         (x-1,y),(x,y)로 해당 선분에 대한 두 정점을 규칙에 맞게끔 visit에 추가.

이렇게 되면, 해당 선분을 구성하는 두 정점에 대해서 (작은좌표),(큰좌표)순으로
"중복없이" 추가되기때문에, 우리가 원하는 예외처리를 포함한다.
"""
def solution(dirs):
    visit = set()
    x = 0; y = 0
    for d in dirs:
        if d == 'U' and y < 5:
            visit.add(((x, y), (x, y+1)))
            y += 1
            
        elif d == 'D' and y > -5:
            visit.add(((x, y-1), (x, y)))
            y -= 1
            
        elif d == 'R' and x < 5:
            visit.add(((x, y), (x+1, y)))
            x += 1
            
        elif d == 'L' and x > -5:
            visit.add(((x-1, y), (x, y)))
            x -= 1
    return len(visit)

print(solution("ULURRDLLU"))