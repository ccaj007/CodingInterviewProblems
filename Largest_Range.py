'''
https://www.youtube.com/watch?v=TgCKJU3JvO4
take an array of integers and returns an array of length representing the 
largest range of numbers contained in that array. The first number in the output
should be the first number in the range while the second number should be the 
last number in the range.

the output [2, 6] represents the range [2, 3, 4, 5, 6], which is a range 
length of 5. Note that numbers do not need to be ordered or adjacent in the array
to form a rnage. Assume that there will only be one largest range.

Sample input: [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
Sample output: [0, 7]
'''

'''
can sort the list but that is O(nlogn)

hashtable is 0(n)
'''

def largestRange(array):
    numbers = {x:0 for x in array}
    left = right = 0

    for number in array:
        if numbers[number] == 0:
            left_count = number - 1
            right_count = number + 1

            while left_count in numbers: # O(1) time
                numbers[left_count] = 1
                left_count -= 1

            left_count += 1

            while right_count in numbers:
                numbers[right_count] = 1
                right_count += 1

            right_count -= 1

            if (right-left) <= (right_count-left_count):
                right = right_count
                left = left_count
    
    return [left, right]

def largestConsecutive(nums):
    numSet = set(nums)
    longest = 0

    for n in numSet:
        if (n - 1) not in numSet:
            length = 1
            while (n + length) in numSet:
                length += 1
            longest = max(length, longest)
    return longest

a = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
print(largestRange(a))

print(largestConsecutive(a))