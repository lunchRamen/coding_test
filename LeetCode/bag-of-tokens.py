class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score=0
        
        tokens.sort()
        start=0
        end=len(tokens)-1
        
        """
        토큰을 face up 할 수 있는 법 = power >= tokens[i]
        토큰을 face down 할 수 있는 법 = score >= 1
        
        토큰을 face up 할수도,(power<tokens[start])
        토큰을 face down 할수도,(score<=0) -> 근데 이 경우는 첫번째 조건문에 걸면, 그냥 끝날듯.
        없다면, while문을 탈출하고 끝난다.
        
        그리고 그 상태에서 score를 뱉으면 됨.
        
        통과해야되는 조건은 다음과 같다.
        1. start>end(이미 모든 토큰을 한번씩 썼다) -> break 후 return score
        2. power>=tokens[start] -> score+=1 power-=tokens[start] start+=1
            start idx를 한칸 옮기고, score증가, power 감소
        3. 만약 작다면, score>=1인지, 아니라면 break 후 score return
        4. 이 경우에도, 만약 start+=1 >=end인지 확인해야함.
            왜냐하면, 만약 한 개 남았는데 face down하면, maximize score를 할 수 없기때문
            나머지 경우 face down을 하고, 다음 while문 진행.
        """
        while True:
            if start>end:
                break
            
            if power>=tokens[start]:
                score+=1
                power-=tokens[start]
                start+=1
            
            else:
                if score>=1:
                    if start+1 >= end:
                        break
                    else:
                        score-=1
                        power+=tokens[end]
                        end-=1
                else:
                    break
        return score
