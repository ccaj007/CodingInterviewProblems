'''
https://leetcode.com/problems/kth-largest-element-in-an-array/description/

given an array of integers arr and an intger k,
find the kth largest element

1 <= k <= |arr|

input:
arr = [4, 2, 9, 7, 5, 6, 7, 1, 3]
k = 4
ouput: 6
explanation:
1st largest element is 9
2nd is 7
3rd is 7
4th is 6
'''

arr = [4, 2, 9, 7, 5, 6, 7, 1, 3]
k = 4

def findKthLargest(nums: List[int], k: int) -> int:
    b = sorted(nums, reverse=True)
    return b[k-1]

print(kthlargest(arr, k))

# import random

# def test(nums, k):
#     pivot = random.choice(nums)
#     print(pivot)
#     left = [x for x in nums if x > pivot]
#     mid = [x for x in nums if x == pivot]
#     right = [x for x in nums if x < pivot]

#     print(f'{left= }, {mid= }, {right= }')

# test(arr, k)
