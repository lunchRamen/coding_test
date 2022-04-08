import sys

input=sys.stdin.readline

"""
내가 생각한 풀이법
고객 1명을 늘리는데 필요한 가중치값이 작은 순서대로 정렬을 한 후,
가중치 값이 가장 작은(효율이 큰)걸로 n을 최대한 깎는다.
그 다음, 마지막 남은것에 대해선 가중치가 낮지만 절대적 값이
높을 수 있으므로 모든 배열을 돌면서 resultMoney+arr[i][0]을 한 다음,
min(temp)를해서 최소값을 추출해서 예제TC는 다 통과를 했었는데,
틀렸다고 나왔다.

왜인지 생각을 해봤을때, 가중치가 더 크지만
arr[i]의 n개 조합과 arr[i+1]의 m개 조합 중 후자가
합친 가중치 자체는 낮아지는 예외케이스가 있어서 그런듯.

->dp로 0부터 쌓아서 풀어봄.

각 호텔의 돈 늘어나는 사람을 기준으로
dp를 모두 도는데,


"""

INF = 1e9

c, n = map(int, input().split())
data = []

min_cost = [INF] * (c+100)
min_cost[0] = 0

for _ in range(n):
    # cost, cus
    data.append(list(map(int, input().split())))

# cost 작은 순서로 정리
data_sort = sorted(data, key = lambda x: x[0])


for cost, cus in data_sort:
    #입력받은 각 호텔들에 대해서
    for i in range(cus, c+100):
        #호텔 고객 명수에 따라, 최소값을 따져준다.
        #i명만큼 늘어났을때 드는 최소비용은
        #i명-호텔 고객 수 + 드는 비용(i-cus명에서 i명이 되는데 드는 비용)
        #과 min_cost[i]의 최솟값 비교.
        #min_cost는 최대값으로 만들어놔서 상관없고,
        #data_sort배열을 다 돌면서 모든 경우에 대해 최솟값을 도출.
        min_cost[i] = min(min_cost[i-cus] + cost, min_cost[i])
print(min_cost)
print(min(min_cost[c:]))

# arr.sort(key=lambda x:x[0]/x[1])

# money=arr[0][0] #최대 가중치
# people=arr[0][1]

# resultMoney=0

# while True:
#     if n<0:
#         n+=people
#         resultMoney-=money
#         break
#     if n==0:
#         break
#     n-=people
#     resultMoney+=money

# temp=[]
# if n==0:
#     temp.append(resultMoney)
# else:
#     for i in range(len(arr)):
#         tempN=n
#         tempResultMoney=resultMoney
#         while True:
#             if tempN<=0:
#                 break
#             tempN-=arr[i][1]
#             tempResultMoney+=arr[i][0]
#         temp.append(tempResultMoney)
            
# print(min(temp))

