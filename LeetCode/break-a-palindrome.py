class Solution:

    def breakPalindrome(self, palindrome: str) -> str:
        """
        개인적으로 어떤 알고리즘, 자료구조를 써서 풀어야할지 생각이 잘 안나서,
        구현으로 풀었다.
        경우의 수는 3가지
        1. 주어진 펠린드롬이 길이가 1일때
        2. 펠린드롬이 모두 같은 문자로 이루어져있을때
        3. 펠린드롬이 다른 문자로 이루어져있을때

        2번과 3번은 각 경우에따라 3가지로 또 나뉜다
        1) s[i]가 a인 경우, 사전적으로 더 작게 만들 수 없으므로 넘어간다
        2) 만약 s[i]를 사전적으로 더 작게 만들었을때, 그 문자열이 펠린드롬이라면 넘어가야한다.
        3) 만약 s[i]를 바꿨다면, 더이상 바꿀 필요가 없다.

        또한 만약 위에 로직을 다 거쳤을때, 문자열이 변한게 아무것도 없다면
        -> "펠린드롬을 깨서"사전적으로 더 작게 만들 수 없다는것이므로
        2순위인 펠린드롬을 꺠고, 사전적으로 가장 조금 크게 만들어야한다.
        -> 맨뒤부터 알파벳을 하나씩 올려보고, 또 펠린드롬 체크를 한 다음 팰린드롬이 꺠지면, 이걸 정답으로 채택한다.

        분명 뭔가 기발한 생각으로 간단하게 구현이 가능할거같은데, 나는 생각이 안나서 노가다 구현.
        """
        def check(s):
            mid = len(s)//2

            for i in range(mid):
                if s[i] != s[len(s)-1-i]:
                    return False
            return True
        
        dic = dict()

        for p in palindrome:
            if ord(p) not in dic:
                dic[ord(p)]=1
            else:
                dic[ord(p)]+=1
        
        if len(palindrome)==1:
            return ""

        string = list(palindrome)

        if len(dic)==1:
            if ord('a') not in dic:
                for s in range(len(string)):
                    if ord(string[s])==97:
                        continue
                    flag = False
                    for i in range(97,97+26):
                        if ord(string[s])>i:
                            temp = string[s]
                            string[s] = chr(i)
                            if check(string):
                                string[s]=temp
                                continue
                            else:
                                flag=True
                                break
                    if flag:
                        break
            else:
                for s in range(len(string)-1,-1,-1):
                    temp = string[s]
                    string[s] = chr(ord(string[s])+1)
                    if check(string):
                        string[s]=temp
                        continue
                    else:
                        break
                
        else:
            for s in range(len(string)):
                if ord(string[s])==97:
                    continue
                flag = False
                for i in range(97,97+26):
                    if ord(string[s])>i:
                        temp = string[s]
                        string[s] = chr(i)
                        if check(string):
                            print(string)
                            string[s]=temp
                            continue
                        else:
                            flag=True
                            break
                if flag:
                    break
            if "".join(string) == palindrome:
                for s in range(len(string)-1,-1,-1):
                    temp = string[s]
                    string[s] = chr(ord(string[s])+1)
                    if check(string):
                        string[s]=temp
                        continue
                    else:
                        break
        return "".join(string)
