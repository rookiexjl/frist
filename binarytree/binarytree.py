# coding:utf-8
'''
Created on 2016年9月21日

@author: admin
'''

# coding:utf-8
class TreeNode(object):
    def __init__(self, x, leftNode=None, rightNode=None):
        self.val = x
        self.left = leftNode
        self.right = rightNode

    def __str__(self):
        return str(self.val)


class Solution(object):
    def invert_tree(self, node):
        """
        :type node: TreeNode
        :rtype: TreeNode
        """
        if node:
            node.left, node.right = node.right, node.left
            if node.left:
                node.left = self.invert_tree(node.left)
            if node.right:
                node.right = self.invert_tree(node.right)
        return node


def print_tree(node=None, is_child=False, deep=3):
    if not node and is_child:
        return

    if not is_child:
        print node

    if not node.left and not node.right:
        return

    print "%s> " % node, node.left, node.right
    print_tree(node.left, is_child=True)
    print_tree(node.right, is_child=True)


if __name__ == '__main__':
    root = TreeNode(
        4,
        TreeNode(2, TreeNode(1), TreeNode(3)),
        TreeNode(7, TreeNode(6), TreeNode(9))
    )

    print_tree(root)
    print '====='
    solution = Solution()
    invert_node = solution.invert_tree(root)
    print_tree(invert_node)
