'''
https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

Given a string containing digits from 2-9 inclusive, 
return all possible letter combinations that the number could represent. 
Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is 
given below. Note that 1 does not map to any letters.
 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:

Input: digits = ""
Output: []

Example 3:

Input: digits = "2"
Output: ["a","b","c"]

 

Constraints:

    0 <= digits.length <= 4
    digits[i] is a digit in the range ['2', '9'

solution: https://www.youtube.com/watch?v=0snEunUacZY
'''

def letterCombinations(digits: str) -> list[str]:
    res = []
    digittoChar = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    def backtrack(i, currStr):
        if len(currStr) == len(digits):
            res.append(currStr)
            return
        for c in digittoChar[digits[i]]:
            backtrack(i + 1, currStr + c)

    if digits:
        backtrack(0, "")

    return res

digits = "23"
print(letterCombinations(digits))
