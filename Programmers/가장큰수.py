"""
input이 10만이라, 2중 for문은 쓰면 안됨.
시간복잡도는 커봤자 nlogn정도까지 가능.

내 문제풀이는 순열로 모든 조합을 뽑은 다음에, 내림차순으로 정렬해서 [0]을 출력하는건데,
이러면 numbers 길이가 너무 길어서 적합하지 않음.

-> 정렬 하나로 끝내야함.
여기서 numbers 원소의 크기에 집중할 필요가 있따
0<=numbers[i]<=1000이다.
대부분의 numbers[i]는 커봤자 3자리수에 머문다는 걸 알 수 있음.
그래서 파이썬 문자열 비교 알고리즘의 특성(첫번째 문자부터 해당 문자의 아스키값으로 정렬)을 이용,
정렬한다.

그리고 모두 0이 되는 경우는 00000000...=0이기때문에
temp[0]이 0이 되는 경우만 예외케이스 처리해주면 된다.
"""


def solution(numbers):
    answer = ''
    temp=[]
    for i in range(len(numbers)):
        temp.append(str(numbers[i]))
    temp.sort(key=lambda x: x*3,reverse=True)
    # nPr=list(permutations(temp,len(temp)))
    # strList=[]
    # for idx in nPr:
    #     t=""
    #     for i in range(len(idx)):
    #         t+=idx[i]
    #     strList.append(t)
    # strList.sort(reverse=True)
    if temp[0]=="0":
        return "0"
    else:
        for i in temp:
            answer+=str(int(i))
    return answer