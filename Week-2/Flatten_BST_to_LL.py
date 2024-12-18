class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        def DFS(dfs, root):
            if not root:
                return
            dfs.append(root.val)
            if root.left:
                dfs = DFS(dfs, root.left)
            if root.right:
                dfs = DFS(dfs, root.right)
            return dfs

        dfs = []
        dfs = DFS(dfs, root)
        # print(dfs)
        if not dfs:
            return
        if len(dfs)==1:
            return root
        i = 1
        # root = TreeNode(dfs[0])
        root.val = dfs[0]
        temp = root
        # print(temp)
        while i<len(dfs):
            temp.left = None
            temp.right = TreeNode(dfs[i])
            # print(dfs[i])
            i+=1
            temp = temp.right
