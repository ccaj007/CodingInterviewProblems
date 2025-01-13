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

solution:
https://www.youtube.com/watch?v=XEmy13g1Qxc&t=916s
QuickSelect
'''

arr = [4, 2, 9, 7, 5, 6, 7, 1, 3]
k = 4

def findKthLargest(nums: list[int], k: int) -> int:

    # b = sorted(nums, reverse=True)
    # return b[k-1]

    k = len(nums) - k

    def quickSelect(l, r):
        pivot, p = nums[r], l
        for i in range(l, r):
            if nums[i] <= pivot:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1
        nums[p], nums[r] = nums[r], nums[p]

        if p > k:   return quickSelect(l, p - 1)
        elif p < k: return quickSelect(p + 1, r)
        else:       return nums[p]

    return quickSelect(0, len(nums) - 1)

print(findKthLargest(arr, k))


