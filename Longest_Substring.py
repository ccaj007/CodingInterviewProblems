'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
https://www.youtube.com/watch?v=sUicrnHwA0s

Given a string s, find the length of the longest
substring
without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

def lengthOfLongestSubstring(s: str) -> int:
    sub = {}
    cur_sub_start = 0
    cur_length = 0
    longest = 0

    for i, letter in enumerate(s):

        if letter in sub and sub[letter] >= cur_sub_start:
            cur_sub_start = sub[letter] + 1
            cur_length =  i - sub[letter]
            sub[letter] = i

        else:
            sub[letter] = i
            cur_length += 1
            if cur_length > longest:
                longest = cur_length

    return(longest)

s = "abcabcbb"
print(lengthOfLongestSubstring(s))