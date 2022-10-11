class Solution:
    """
   어떻게 구현할지 방법이 잘 생각이 안나서, 그냥 inorder형식으로 이분탐색트리를 list에 저장한다음,
   2중 for문을 돌려서 하나라도 k가 되는 순간 True를 return하고 다 안되면 False를 return하게끔 구현하였다.
   입력이 10**4라서 아슬아슬했는데, 됐다.
    """
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        arr = []
        def dfs(root):
            if root is None:
                return
            if root.left is not None:
                dfs(root.left)
            arr.append(root.val)
            if root.right is not None:
                dfs(root.right)
        dfs(root)
        
        idx = len(arr)//2

        # if arr[0]!= arr[len(arr)-1] and arr[0]+arr[len(arr)-1] == k:
        #     return True
        # print(arr)
        # for i in range(idx):
        #     start = i
        #     end = len(arr)-1
        #     while start<end:
        #         mid = (start+end)//2
        #         print(arr[i],arr[mid])
        #         if arr[i]+arr[mid]==k:
        #             return True
        #         elif arr[i]+arr[mid]<k:
        #             start = mid+1
        #         elif arr[i]+arr[mid]>k:
        #             end = mid-1
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i==j:
                    continue
                if arr[i]+arr[j]==k:
                    return True
        return False
