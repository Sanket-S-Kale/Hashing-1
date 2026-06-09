## Problem 3:
# Given a pattern and a string str, find if str follows the same pattern.
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

# Example 1:
# Input: pattern = "abba", str = "dog cat cat dog"
# Output: true

# Example 2:
# Input:pattern = "abba", str = "dog cat cat fish"
# Output: false

# Example 3:
# Input: pattern = "aaaa", str = "dog cat cat dog"
# Output: false

# Example 4:
# Input: pattern = "abba", str = "dog dog dog dog"
# Output: false
# Notes:
# You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.

# Time Complexity: O(n) Where n is the length of the pattern
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        wordsLen = len(words)
        patternLen = len(pattern)

        # if the numner of words in the string and lenght of pattern doesn't match
        # then its not a full match and return early
        if wordsLen != patternLen:
            return False
        
        patternMap = {} # to keep track of char in pattern -> work in str
        mappedWords = set() # to make sure no 2 chars are mapped to the same word

        # iterate over the pattern character by character
        for i in range(len(pattern)):
            pChar = pattern[i]
            patternMapVal = patternMap.get(pChar, -1)
            word = words[i]

            # if we have the char in the map, make sure it matches the current word
            # if not its not a full match
            if patternMapVal != -1:
                if patternMapVal != word:
                    return False
            # if the char is not in the map, but the word is in the set
            # it means the word is mapped to a different char, and is not a full match
            elif word in mappedWords:
                return False
            else:   # add the char -> word mapping to the map, and the word to the set
                patternMap[pChar] = word
                mappedWords.add(word)

        return True   # if we don't return False early, that means its a full match   