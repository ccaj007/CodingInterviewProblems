'''
https://leetcode.com/problems/longest-repeating-character-replacement/description/

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 
Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.

solution:
https://www.youtube.com/watch?v=gqXU1UyA8pk&t=85s


'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        longest = 1
        for r in range(1, len(s)):
            if s[l] == s[r]:
                longest += 1

            else:
                l = r
                longest = 1
        return longest


s = "AABBBA"
k = 1
a = Solution()
print(a.characterReplacement(s, k))
