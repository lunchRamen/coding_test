import sys

input=sys.stdin.readline

summary=0
dic=dict()

while True:
    tree=input().rstrip()
    if not tree:
        break
    if tree in dic:
        dic[tree]+=1
        summary+=1
    else:
        dic[tree]=1
        summary+=1


dic=sorted(dic.items())

for key,value in dic:
    per=round((value/summary)*100,4)
    print(key,"%.4f" %per)





