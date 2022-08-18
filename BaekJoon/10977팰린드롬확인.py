import sys

s=input()

answer=1
for i in range(len(s)//2):
    if s[i]!=s[len(s)-1-i]:
        answer=0
        break

print(answer)