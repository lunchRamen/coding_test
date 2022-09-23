class Solution:
    def reverseWords(self, s: str) -> str:
        """
        각 문자열을 split한 다음,
        [::-1]로 뒤집어주고, answer에 문자 + 띄어쓰기로 붙인다음,
        마지막 띄어쓰기 없애주면 됨.
        """
        
        arr = s.split(" ")
        answer = ""
        for string in arr:
            temp = string[::-1]
            answer+=temp+" "
        answer=answer[:len(answer)-1]
        return answer        
