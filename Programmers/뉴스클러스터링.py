import copy

a = [1,2,2,3,4,5]
b = [1,1,2,3,4,6]
print(a,b)

a_temp = a.copy()
a_result = a.copy()
"""
합집합
arr2의 원소가 temp에 없다?
->합집합에 들어간다.(a_result)
arr2의 원소가 temp에 있다?
->temp에 i를 지운다.
->다음번 b의 원소가 이전에 있는 원소와 동일한데, 만약 a_temp에 원소를
없애지 않는다면, 다음 for문 돌때 합집합에 이미 원소가 있기때문에 통과함.

-> 합집합 for문의 if문은 a에 없는걸 더해주기 위함(합집합)
-> else문은 b의 중복된 집합원소를 추가시켜주기위해 교집합인 경우를 삭제해줌.
->이렇게 되면 a_temp는 b와 교집합인것들이 하나씩 사라지므로, 다음 for문에서
b가 동일한 원소를 더 가지고 있을 경우에 합집합에 추가하는 로직이 된다.
"""
for i in b:
    if i not in a_temp:
        a_result.append(i)  #합집합
    else:
        a_temp.remove(i)    #차집합
print(a_temp,a_result)

result=[]
temp=a.copy()
"""
교집합= a를 복사한 temp배열에 i가 있다면, 해당 원소를 없애고
result에 원소를 더해준다.

->차집합과 교집합을 구해줌.
"""
for i in b:
    if i in temp:  
        temp.remove(i)
        result.append(i)    #교집합
print(result,temp)

"""
결론적으로, 다중집합에서 교집합과 합집합은
b의 원소가 temp에 있냐,없냐에 따라서 합집합,교집합을 만들어준다.
여기서 합집합의 경우 a를 복사해온 상태에서 b의 원소가 temo에 없으면
추가해주는 동작.
교집합의 경우 공집합에서 시작해서 b의 원소가 temp에 있으면 추가해주는 동작.

그 다음 temp의 원소들을 지우는데
합집합의 경우 b의 원소가 temp에 있는 경우
교집합도 동일하다.
왜냐하면, a의 배열과 교집합인것들을 빼가면서 검사를 해야(i in temp)
합집합의 원소들을 추릴 수 있기 때문.
그래서 temp의 최종형태는 차집합이 나옴.

-> b를 돌면서 a와 교집합이 없는상태의 배열(temp)와 비교했을때
temp에 없는 원소면 합집합 배열에 추가.
temp에 있으면 temp의 원소 삭제(교집합이 없는 상태로 만들려고)

반대로 a와 교집합이 없는 상태로 만들어서
temp에 있으면, 배열에 추가하고, 해당 배열을 삭제해서 교집합과
차집합을 만든다.
"""
