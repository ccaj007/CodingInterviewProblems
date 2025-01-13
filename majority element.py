'''
https://leetcode.com/problems/majority-element/?_bhlid=fad2c5c31ffa135ecc7faae6370c6b9d440702b4


Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3

Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

'''
from collections import Counter

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        x = Counter(nums)
        for num, count in x.items():
            if count > len(nums) // 2:
                return num


nums = [2,2,1,1,1,2,2]
a = Solution()
print(a.majorityElement(nums))