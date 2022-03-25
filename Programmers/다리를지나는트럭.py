"""
여기서 내가 놓쳤던 핵심은, 1초마다 트럭은 1만큼씩 갈수 있고, 다리의 길이(bridge_length)를 건너려면,
애초에 bridge_length초가 걸린다는것.
이걸을 해결하는 아이디어 중 하나는 in_bridge에 0을 다 넣어놓고
하나씩 터트리는데 만약 터트린게 0이 아니라면, completed배열에 넣어주는것.

위 조건이 끝난 후에 이제
트럭을 다리에 한대 더 올리느냐 마느냐를 따져주는데,
만약 대기중인 트럭이 있고,
다리를 건너는 중인 트럭들의 무게 합 + 대기중인 0번째 트럭이 문제에서 제시된 weight보다 작거나 같다면
in_bridge에 truck_weight.pop(0)시킨걸 넣어준다.
만약 초과됐으면? 0을 넣어줌. 이것도 핵심.
0을 터트려줌으로써 시간은 지나지만 트럭은 아직 다리를 건너고 있음을 표현해주는데 다리에 트럭을 추가하지 못하는 경우
그럼에도 다리에 진입한 트럭들은 가고 있고, 완료로 넘어가거나 하는 경우에도 "무게"를 비교함에 있어서 적절하게 도와주는 숫자가 0.
"""
def solution(bridge_length, weight, truck_weights):
    second = 0  #시간
    completed = []  #완료
    in_bridge = [0] * bridge_length #다리
    size = len(truck_weights)   #길이
    
    
    while len(completed) != size:
        second += 1 #일단 1초 추가
        top = in_bridge.pop(0)  #다리에 있는거 하나 가져옴
        if top != 0:    #만약 다리에 건너는중인 차 무게가 0이 아니라면 =
            completed.append(top)
        if len(truck_weights) > 0: 
            if sum(in_bridge) + truck_weights[0] <= weight:
                in_bridge.append(truck_weights.pop(0))
            else:
                in_bridge.append(0)
    return second