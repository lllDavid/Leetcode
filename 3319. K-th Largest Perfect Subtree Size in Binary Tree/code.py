# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        sizes = []
        def dfs(node):
            if not node:
                return (True, 0, 0)
            l_perf, l_h, l_s = dfs(node.left)
            r_perf, r_h, r_s = dfs(node.right)

            is_perfect = l_perf and r_perf and l_h == r_h
            height = l_h + 1
            size = l_s + r_s + 1

            if is_perfect:
                sizes.append(size)
            return (is_perfect, height, size)

        dfs(root)
        if len(sizes) < k:
            return -1
        sizes.sort(reverse=True)
        return sizes[k-1]