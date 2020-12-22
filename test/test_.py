# encoding: utf-8
#
# 数组 [1, 7, 3, 6, 9, 2, 3, 5, 8, 22, 65]
# Q1: 写一个二分查找，找到7的位置(1)
# Q2: 这个个数组构建一个二叉搜索树：(打印根节点与根的子节点)
#


# def binarySearch(arr, target, l, r):
#     if r >= 1:
#         mid = int(1+(r-l)/2)
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] > target:
#             return binarySearch(arr, target, l, mid-1)
#         else:
#             return binarySearch(arr, target, mid+1, r)
#     else:
#         return -1
#
#
# class Tree:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None
#
#     def insert(self, root, val):
#         if root is None:
#             root = Tree(val)
#         elif val < root.val:
#             root.left = self.insert(root.left, val)
#         elif val >= root.val:
#             root.right = self.insert(root.right, val)
#         return root
#
#     def pr(self, root):
#         if root is None:
#             return
#         self.pr(root.left)
#         print(root.val, end=' ')
#         self.pr(root.right)
#
#
# if __name__ == "__main__":
#     a = [1, 7, 3, 6, 9, 2, 3, 5, 8, 22, 65]
#     # a.sort()
#     # print(a)
#     # print(binarySearch(a, 7, 0, len(a)-1))
#     b = Tree(a[0])
#     for i in range(1,len(a)):
#         b.insert(b, a[i])
#
#     b.pr(b)
import os
import time
import numpy as np
import math
a = np.zeros([6,7])
print(a)
print(type(a))
print(a.size)


def jug(m, n, tw):
    next_m = tw[0] + m
    next_n = tw[1] + n
    if m == 0:
        next_m = m+1
        tw[0] *= -1
    if m == 5:
        next_m = m-1
        tw[0] *= -1
    if n == 0:
        next_n = n+1
        tw[1] *= -1
    if n == 6:
        next_n = n-1
        tw[1] *= -1
    if m == 0 and n == 6:
        next_n = 5
        next_m = 0
        tw = [-1,-1]
    if m == 5 and n == 6:
        next_n = 5
        next_m = 5
        tw = [-1,1]
    return next_m, next_n, tw


def dou(a):
    x = np.random.randint(0, 5)
    y = np.random.randint(0, 6)
    while a[x][y] == 1:
        x = np.random.randint(0, 5)
        y = np.random.randint(0, 6)
    return x, y

x = 0
y = 0
tw = [1, 1]
li = [[x, y]]
flag = False
d1, d2 = dou(a)
a[d1][d2] = 2
while True:
    if flag:
        d1, d2 = dou(a)
        a[d1][d2] = 2
    for i in li:
        a[i[0]][i[1]] = 1
    os.system('cls')
    print(a)

    x, y, tw = jug(x,y,tw)
    li.append([x,y])
    if d1 == x and d2 == y:
        flag = True
    else:
        c = li.pop(0)
        a[c[0]][c[1]] = 0
        flag = False

    time.sleep(1)


