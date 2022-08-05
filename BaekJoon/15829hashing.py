n=int(input())

s=input()

answer=0
for i in range(len(s)):
    sNum=ord(s[i])-96
    answer+=sNum*pow(31,i)


print(answer%1234567891)