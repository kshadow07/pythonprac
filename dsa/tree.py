# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode):
        result = []
        stack = [root]


        while stack:
            node = stack.pop()
            if node:
                result.append(node.val)
                stack.append(node.right)
                stack.append(node.left)

        return result


root=TreeNode(3)
root.right=TreeNode(20)

 
solution=Solution()
result= solution.preorderTraversal(root)

for i in result:
    print(i)
