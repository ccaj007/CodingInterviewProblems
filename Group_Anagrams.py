'''
https://leetcode.com/problems/group-anagrams/description/

Given an array of strings strs, group the anagrams
together. You can return the answer in any order.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

    There is no string in strs that can be rearranged to form "bat".
    The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
    The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

'''

from collections import defaultdict

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    
    anagram_map = defaultdict(list)
    result = []

    for word in strs:
        sorted_word = tuple(sorted(word))
        anagram_map[sorted_word].append(word)
        # anagram_map[tuple(sorted(word))].append(word)
        
    for value in anagram_map.values():
        result.append(value)
    
    # [result.append(value) for value in anagram_map.values()]
    return result

    # return(list(anagram_map.values()))
    
    

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))