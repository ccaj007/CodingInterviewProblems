'''
https://leetcode.com/problems/longest-consecutive-sequence/description/?envType=problem-list-v2&envId=xi4ci4ig

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

solution:

First turn the input into a set of numbers. That takes O(n) and then we can ask in O(1) 
whether we have a certain number.

Then go through the numbers. If the number x is the start of a streak 
(i.e., x-1 is not in the set), then test y = x+1, x+2, x+3, ... and 
stop at the first number y not in the set. The length of the streak 
is then simply y-x and we update our global best with that. 
Since we check each streak only once, this is overall O(n). 
This ran in 44 ms on the OJ, one of the fastest Python submissions.

'''
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = set(nums)
        best = 0
        for x in nums:
            if x - 1 not in nums:
                y = x + 1
                while y in nums:
                    y += 1
                best = max(best, y - x)
        return best

nums = [100,4,200,1,3,2]
s = Solution()
print(s.longestConsecutive(nums))
