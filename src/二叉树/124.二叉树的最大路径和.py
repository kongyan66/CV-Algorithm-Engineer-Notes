# 题目：路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。同一个节点在一条路径序列中
# 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。问最大路径和？

# 思路：后续遍历，去找每一个节点的贡献值，回溯的时候将得到最大值。
# https://leetcode.cn/problems/binary-tree-maximum-path-sum/solution/by-lin-shen-shi-jian-lu-k-2td7/

# 解法
class Solution:
    def __init__(self):
        self.res = -float('inf')

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.recursion(root)
        return self.res
    # 1.确定入参与返回值
    # 返回值每个子树从最高节点开始往下延伸的最大路径和。
    def recursion(self, root):
        if not root:
            return 0
        # 
        max_left = max(0, self.recursion(root.left))
        max_right = max(0, self.recursion(root.right))
        # 更新最大值  根节点值+左子树最大路径和+右子树最大路径和
        self.res = max(self.res, max_left + max_right + root.val)
        # 选择往左或者往右（这点很重要）
        return max(max_left, max_right) + root.val