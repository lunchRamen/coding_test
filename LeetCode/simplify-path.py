class Solution:
    """
    주어진 path를 통해, "현재경로"를 알아내는 문제
    눈여겨 볼건 .. 하나밖에 없다. ..의 경우 stack을 pop시키고
    .가 아니거나 ''가 아닌경우 stack에 append하면 된다
    그리고 str.join의 기능중 str에 특정 문자열을 넣으면, join하는 배열의 원소 사이마다 넣어준다.
    """
    def simplifyPath(self, path: str) -> str:
        path_arr = path.split("/")


        stack = []

        for p in path_arr:
            if p=="..":
                if len(stack)>0:
                    stack.pop()
            
            elif p != "." and len(p)>0:
                stack.append(p)

        return "/"+"/".join(stack)
