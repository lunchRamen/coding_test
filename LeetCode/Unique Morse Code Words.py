class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        arr=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        dic=dict()
        start=97
        for i in arr:
            dic[chr(start)]=i
            start+=1
        answer=[]
        
        for word in words:
            temp=""
            for i in word:
                temp+=dic[i]
            answer.append(temp)
        answer=set(answer)
        return len(answer)
