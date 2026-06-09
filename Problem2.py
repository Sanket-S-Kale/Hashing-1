## Problem 2:
# Given two strings s and t, determine if they are isomorphic.
# Two strings are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

# Example 1:
# Input: s = "egg", t = "add"
# Output: true

# Example 2:
# Input: s = "foo", t = "bar"
# Output: false

# Example 3:
# Input: s = "paper", t = "title"
# Output: true
# Note:
# You may assume both s and t have the same length.


# Time Complexity: O(n)
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sMap = dict()   # for s -> t mappting
        tMap = dict()   # for t -> s mapping
        n = len(s)

        for idx in range(n):
            charS = s[idx]
            charT = t[idx]

            sMapChar = sMap.get(charS, -1)
            # check if char in s maps to the same char in t
            if sMapChar != -1:
                if sMapChar != charT:
                    return False
            else:   # add to the map if seeing it for the first time
                sMap[charS] = charT
            
            tMapChar = tMap.get(charT, -1)
            # check if char in t maps to the same char in s
            if tMapChar != -1:
                if tMapChar != charS:
                    return False
            else:   # add to the map if seeing it for the first time
                tMap[charT] = charS
        
        return True   # if all mappings are good, the strings are isomorphic