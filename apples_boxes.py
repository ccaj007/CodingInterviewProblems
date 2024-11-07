'''
https://leetcode.com/problems/apple-redistribution-into-boxes/description/

You are given an array apple of size n and an array capacity of size m.

There are n packs where the ith pack contains apple[i] apples. 
There are m boxes as well, and the ith box has a capacity of 
capacity[i] apples.

Return the minimum number of boxes you need to select to redistribute 
these n packs of apples into boxes.

Note that, apples from the same pack can be distributed into different boxes.

Example 1:

Input: apple = [1,3,2], capacity = [4,3,1,5,2]
Output: 2
Explanation: We will use boxes with capacities 4 and 5.
It is possible to distribute the apples as the total capacity is greater than or equal to the total number of apples.

Example 2:

Input: apple = [5,5,5], capacity = [2,4,2,7]
Output: 4
Explanation: We will need to use all the boxes.

'''

'''
Apples can just add all the numbers in array; 10
Boxes sort it [8, 5, 1]
box 1 store 8 apples
box 2 store remainder 2 apples
'''

def minumumBoxes(apple: list[int], capacity: list[int]) -> int:
    total_apples = sum(apple)
    capacity.sort(key=lambda b: -b)
    num_boxes = 0
    
    for box_size in capacity:
        if total_apples > 0:
            total_apples -= box_size
            num_boxes += 1

    return(num_boxes)

apple = [9,8,8,2,3,1,6]
capacity = [10,1,4,10,8,5]
print(minumumBoxes(apple, capacity))