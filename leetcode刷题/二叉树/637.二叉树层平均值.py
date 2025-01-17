# 题目：简单 给定一个非空二叉树的根节点 root , 以数组的形式返回每一层节点的平均值。
# 思路：还是基于层序遍历，每层遍历完后对该暂存列表求一下平均值即可

class Solution1:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        from collections import deque
        results = []
        if root is None:
            return results
        que = deque([root])
        while que:
            result = []
            size = len(que)
            for _ in range(size):
                cur = que.popleft()
                result.append(cur.val)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            final_result = sum(result) / len(result)   # 唯一改动的地方
            results.append(final_result)
        return results
        
# review-2
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        results = []
        if not root:
            return results
        que = [root]
        while que:
            res = []
            for _ in range(len(que)):
                cur = que.pop(0)
                res.append(cur.val)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            results.append(sum(res) / len(res))
        return results