'''
https://leetcode.com/problems/longest-common-prefix/description/

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".


Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


'''

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        res = ""
        # for i in range(min(len(i) for i in strs)):
        #     for s in strs:
        #         if s[i] != strs[0][i]:
        #             return res
        #     res = res + strs[0][i]

        # return res

        shortest = min(strs, key=len)
        for i, letter in enumerate(shortest):
            for other in strs:
                if other[i] != letter:
                    return shortest[:i]
        return shortest

strs: list[str] = ["flower","flow","flight"]
s = Solution()
print(s.longestCommonPrefix(strs))
