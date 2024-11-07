'''
given a sorted array of intergers arr and an integer target,
find the index of the first and last position of the target in array.
If target can't be found in arr, return [-1, -1]

input:
arr = [2, 4, 5, 5, 5, 5, 5,  7, 9, 9]
target = 5
output: [2, 6]
'''

def first_and_last(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            start = i
            while i+1 < len(arr) and arr[i+1] == target:
                i += 1
            return [start, i]
    return [-1, -1]

arr = [2, 4, 5, 5, 5, 5, 5,  7, 9, 9]
target = 5
print(first_and_last(arr, target))



