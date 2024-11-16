'''
https://leetcode.com/problems/squares-of-a-sorted-array/description/

Given an integer array nums sorted in non-decreasing 
order, return an array of the squares of each number 
sorted in non-decreasing order.

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

solution: 
https://www.youtube.com/watch?v=FPCZsG_AkUg

'''

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        ans = []
        # for i in nums:
        #     ans.append(i*i)
        # return sorted(ans)

        l = 0
        r = len(nums) - 1
        while l <= r:
            if (nums[l]*nums[l]) > (nums[r] * nums[r]):
                 ans.append(nums[l]*nums[l])
                 l += 1
            else:
                ans.append(nums[r]*nums[r])
                r -= 1

        return ans[::-1]


        

nums = [-7,-3,2,3,11]
ans = Solution()
print(ans.sortedSquares(nums))
