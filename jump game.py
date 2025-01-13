'''
https://leetcode.com/problems/jump-game/description/

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

 
solution:
https://www.youtube.com/watch?v=Yan0cv2cLy8

'''


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        # goal_post = len(nums) -1

        # for i in range(len(nums) -1, -1, -1):
        #     x = nums[i] + i
        #     if x >= goal_post:
        #         goal_post = i

        # return True if goal_post == 0 else False

        gas = 0
        for n in nums:
            if gas < 0:
                return False
            elif n > gas:
                gas = n
            gas -= 1

        return True

nums = [2,3,1,1,4]
a = Solution()
print(a.canJump(nums))

