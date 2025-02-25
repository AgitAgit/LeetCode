# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def compare_arrays(self, arr1, arr2):
        if len(arr1) != len(arr2):
            return False
        for i in range(len(arr1)):
            if arr1[i] != arr2[i]:
                return False
        return True

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pList = []
        pDeQueue = deque()
        qList = []
        qDeQueue = deque()
        pDeQueue.append(p)
        
        while len(pDeQueue) > 0:
            if pDeQueue[0]:            
                pList.append(pDeQueue[0].val)
                pDeQueue.append(pDeQueue[0].left)
                pDeQueue.append(pDeQueue[0].right)
            else:
                pList.append("null")
            pDeQueue.popleft()
        qDeQueue.append(q)
        
        while len(qDeQueue) > 0:
            if qDeQueue[0]:            
                qList.append(qDeQueue[0].val)
                qDeQueue.append(qDeQueue[0].left)
                qDeQueue.append(qDeQueue[0].right)
            else:
                qList.append("null")
            qDeQueue.popleft()
        
        return self.compare_arrays(pList, qList)
