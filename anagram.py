'''
given two strings, s1 and s2, check if they are anagrams of each other

anagrams if they are made of the same characters with the same frequency

'''
s1 = "danger"
s2 = "garden"

def are_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)

from collections import Counter

def are_anagrams2(s1, s2):
    if len(s1) != len(s2):
        return False
    return Counter(s1) == Counter(s2)
        
    


print(are_anagrams2(s1, s2))
