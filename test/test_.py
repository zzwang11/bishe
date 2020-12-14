# encoding: utf-8
#
# 数组 [1, 7, 3, 6, 9, 2, 3, 5, 8, 22, 65]
# Q1: 写一个二分查找，找到7的位置(1)
# Q2: 这个个数组构建一个二叉搜索树：(打印根节点与根的子节点)
#


def binarySearch(arr, target, l, r):
    if r >= 1:
        mid = int(1+(r-l)/2)
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binarySearch(arr, target, l, mid-1)
        else:
            return binarySearch(arr, target, mid+1, r)
    else:
        return -1


class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, root, val):
        if root is None:
            root = Tree(val)
        elif val < root.val:
            root.left = self.insert(root.left, val)
        elif val >= root.val:
            root.right = self.insert(root.right, val)
        return root

    def pr(self, root):
        if root is None:
            return
        self.pr(root.left)
        print(root.val, end=' ')
        self.pr(root.right)


if __name__ == "__main__":
    a = [1, 7, 3, 6, 9, 2, 3, 5, 8, 22, 65]
    # a.sort()
    # print(a)
    # print(binarySearch(a, 7, 0, len(a)-1))
    b = Tree(a[0])
    for i in range(1,len(a)):
        b.insert(b, a[i])

    b.pr(b)

