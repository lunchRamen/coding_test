class Solution:
    def removeDuplicates(self, s: str) -> str:
        """
        우테코에서 비슷한 유형의 문제를 풀었었다.
        그때 당시는, 연속되는 문자를 찾으면, 그걸 뺀 substring으로 새로 붙인다음 break해서
        연속되는 문자가 없을때까지 while문을 돌리게 짰었는데,
        동일한 로직으로 짜니 시간초과가 난다.
        -> stack을 이용하면 O(n)으로 짤 수 있다.
        stack이 비어있거나, 현재 s[i]와 같지 않다면 추가한다.
        만약 stack[-1]과 s[i]가 같다면 pop시킨다.
        이렇게하면, 순서쌍이 없는 문자열들만 stack에 남기때문에, 이걸 반환하면 된다.
        """
        stack = []

        for i in range(len(s)):
            if not stack:
                stack.append(s[i])
                continue
            if stack[-1] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
        return "".join(stack)
