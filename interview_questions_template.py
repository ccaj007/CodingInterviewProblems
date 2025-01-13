'''
https://www.youtube.com/watch?v=Peq4GCPNC5c&t=843s


given two strings, s1 and s2, check if they are anagrams of each other

anagrams if they are made of the same characters with the same frequency

s1 = "danger"
s2 = "garden"

'''

'''
given a sorted array of intergers arr and an integer target,
find the index of the first and last position of the target in array.
If target can't be found in arr, return [-1, -1]

input:
arr = [2, 4, 5, 5, 5, 5, 5,  7, 9, 9]
target = 5
output: [2, 6]
'''

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
'''

'''
given a binary tree root, check if it's symmetric around its center
(a mirror of itself)
'''


'''
generate parenthesses
https://leetcode.com/problems/generate-parentheses/description/

given an integer n, generate all the valid combinations of n pairs
of parentheses

input: n = 3
output:
["((()))", "(()())", "(())()", "()(())", "()()()"]

'''

'''
 gas station
 https://leetcode.com/problems/gas-station/description/

 There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique.

 

Example 1:

Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.

Example 2:

Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.
'''

'''
course schedule
https://leetcode.com/problems/course-schedule/description/

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
ou are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return true if you can finish all courses. Otherwise, return false.

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

'''

'''
kth permutation

with the range of numbers from 1 to n inclusive, we can make n! permutations.
By labeling them in order starting from 1, you are asked to return the kth permutation.

input:
n = 3
k = 3
output: "213"
explanation:
        1. "123"
        2. "132"
kth ->  3. "213"
        4. "231"
        5. "312"
        6. "321"
'''

'''
minimum window substring
https://leetcode.com/problems/minimum-window-substring/description/

Given two strings s and t of lengths m and n respectively, return the minimum window
substring of s such that every character in t (including duplicates) is included in the window. 
If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.
 
Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

'''

'''
largest rectangle in histotram
https://leetcode.com/problems/largest-rectangle-in-histogram/description/

Given an array of integers heights representing the histogram's bar height 
where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Input: heights = [2,4]
Output: 4

'''





